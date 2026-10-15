-- Export a .pptx to PDF with Microsoft PowerPoint (macOS).
--   osascript scripts/export_pdf.applescript /abs/path/deck.pptx /abs/path/deck.pdf
on run argv
	set src to item 1 of argv
	set dst to item 2 of argv
	tell application id "com.microsoft.Powerpoint"
		open POSIX file src
		delay 3
		save active presentation in POSIX file dst as save as PDF
		close active presentation saving no
	end tell
end run
