-- Export a .pptx to PDF with Microsoft PowerPoint (macOS).
--   osascript scripts/export_pdf.applescript /abs/path/deck.pptx /abs/path/deck.pdf
on run argv
	set srcFile to POSIX file (item 1 of argv)
	set dstPath to (item 2 of argv)
	tell application id "com.microsoft.Powerpoint"
		open srcFile
		delay 3
		save active presentation in dstPath as save as PDF
		close active presentation saving no
	end tell
end run
