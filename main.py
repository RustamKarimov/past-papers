"""
Main program responsible for generating past paper videos
prepared by using Manim.
"""

from subprocess import run

from settings import file_settings as fs

DISABLE = True

SUBJECT = "Physics"
YEAR = "2022"
QUESTION = "7"
SUB_QUESTION = "2"
FILE = fs.BASE_DIR / SUBJECT / YEAR / f"Question_{QUESTION}" / f"question_{QUESTION}_{SUB_QUESTION}.py"
SCENE = f"Question_{QUESTION}_{SUB_QUESTION}"
QUALITY = "l"
CUSTOM_FOLDERS = "--custom_folders"
DISABLE_CACHING = "--disable_caching" if DISABLE else ""

if __name__ == "__main__":
    run(["manim", FILE, SCENE, f"-pq{QUALITY}", CUSTOM_FOLDERS, DISABLE_CACHING])
