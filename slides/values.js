// Formats slide values from experiment result files listed in values_map.json.
// scripts/check_slide_values.py applies the same formats, so the two must change together.

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const MAP = JSON.parse(fs.readFileSync(path.join(__dirname, "values_map.json"), "utf8"));

const cache = {};
const load = (rel) => (cache[rel] ??= JSON.parse(fs.readFileSync(path.join(ROOT, rel), "utf8")));
// Flat files (key_numbers.json) use dotted keys; nested files are walked one key at a time.
const get = (obj, dotted) => (dotted in obj ? obj[dotted] : dotted.split(".").reduce((o, k) => {
  if (o == null || !(k in o)) throw new Error(`missing key '${k}' in path '${dotted}'`);
  return o[k];
}, obj));

const MINUS = "−";
const FORMATS = {
  int: (x) => Math.round(x).toLocaleString("en-US"),
  round: (x) => String(Math.round(x)),
  dec2: (x) => x.toFixed(2),
  dec3: (x) => x.toFixed(3),
  pct0: (x) => (x * 100).toFixed(0),
  pct1: (x) => (x * 100).toFixed(1),
  signed2: (x) => (x < 0 ? MINUS : "") + Math.abs(x).toFixed(2),
};

// Row count of a CSV/TSV, optionally where one column equals a value (simple files only: no quoted delimiters).
function countRows(entry) {
  const lines = fs.readFileSync(path.join(ROOT, entry.source), "utf8").split(/\r?\n/).filter((l) => l.length);
  const sep = entry.source.endsWith(".csv") ? "," : "\t";
  const header = lines[0].split(sep);
  const rows = lines.slice(1).map((l) => l.split(sep));
  if (!entry.column) return rows.length;
  const i = header.indexOf(entry.column);
  if (i < 0) throw new Error(`no column '${entry.column}' in ${entry.source}`);
  return rows.filter((r) => r[i] === String(entry.equals)).length;
}

function value(entry) {
  if (entry.format === "count") return FORMATS.int(countRows(entry));
  const data = load(entry.source);
  if (entry.format === "sub") return FORMATS.int(get(data, entry.path) - get(data, entry.path2));
  const fmt = FORMATS[entry.format];
  if (!fmt) throw new Error(`unknown format '${entry.format}' for ${entry.id}`);
  return fmt(get(data, entry.path));
}

const BY_ID = Object.fromEntries(MAP.values.map((e) => [e.id, e]));

// V("a.edges") -> "5,428"
function V(id) {
  const entry = BY_ID[id];
  if (!entry) throw new Error(`values_map.json has no entry '${id}'`);
  return value(entry);
}

module.exports = { V, ROOT };
