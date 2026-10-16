# /// script
# requires-python = ">=3.11"
# dependencies = ["qrcode[pil]>=7.4"]
# ///
"""QR code for the talk's repository, drawn on the title slide."""
from pathlib import Path
import qrcode

URL = "https://github.com/ReproNim/llm-workshop-kg"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
qr.add_data(URL)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save(Path(__file__).resolve().parent / "repo_qr.png")
