from pathlib import Path
import ctypes

FONT_FOLDER = Path(__file__).parent.parent / "data" / "resources" / "fonts"

def load_fonts():
    for font_file in FONT_FOLDER.glob("*.ttf"):
        ctypes.windll.gdi32.AddFontResourceExW(
            str(font_file),
            0x10,
            0
        )
