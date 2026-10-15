# STATUS (Fork A, resumed 2026-10-15 14:40 local)
0. ORCD fetch (job 25939932) — FAILED: scp twice "Permission denied (keyboard-interactive)", no live ControlMaster; ssh not retried. Local bench used instead.
0b. Oxigraph store was left half-rebuilt at 13:06 — rebuilt (store.py) — done. Also stale: graph/abide_extension.ttl (11:05, 12 classes; current code gives 13 incl. ReportedCohort) — caught by clean room; validate_linkml, scope, publications, store, ego, coverage, competency, key_numbers, report rerun locally at 16:10 — done
1. query timings — superseded by owner decision: engine comparison dropped; benchmark removed from rebuild.sh, README and report; timings moved to archive/ (not shipped)
2. Q8–Q15 gold (code/competency.py extended: Q15 claim count fixed via GROUP BY, Q9 executed/data-source list, result-file citations) — done: comparison/gold_answers.json, results/competency_answers.json, queries/optimized/Q8–Q15*.rq (+Q13_*.rq, Q14.rq, Q10.txt)
3. ORCD vs local — done (as "not compared": ssh failed twice, recorded): results/orcd_vs_local.json
4. README sections — done: README.txt
5. Zip + clean-room verify — done: ../ABIDE_Collaboration_Knowledge_Graph.zip; results/clean_room_verify.json (215/218 key numbers match, 3 run-time only; gold Q1–Q15 identical; publications.py User-Agent bug fixed)
6. Final report — done (handed back)
