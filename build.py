"""Build the static site (site/) for GitHub Pages.

Folder layout (one folder per file type):
    docs/       -> .pdf   (copied as is)
    notebooks/  -> .ipynb (converted to HTML with nbconvert)
    scripts/    -> .py    (copied; highlighted in the browser)

Usage:  python build.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site"
CONTENT = OUT / "content"

# folder -> (file extension, type label)
SOURCES = {
    "docs": (".pdf", "pdf"),
    "notebooks": (".ipynb", "notebook"),
    "scripts": (".py", "python"),
}


def convert_notebook(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, "-m", "nbconvert", "--to", "html",
         "--output", dest.name, "--output-dir", str(dest.parent), str(src)],
        check=True, capture_output=True,
    )


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    CONTENT.mkdir(parents=True)

    entries = []
    for folder, (ext, kind) in SOURCES.items():
        for src in sorted((ROOT / folder).rglob(f"*{ext}")):
            if any(p.startswith((".", "__")) for p in src.relative_to(ROOT).parts):
                continue  # skip .ipynb_checkpoints, __pycache__, hidden files
            rel = src.relative_to(ROOT)
            if kind == "notebook":
                served = rel.with_suffix(".html")
                convert_notebook(src, CONTENT / served)
            else:
                served = rel
                (CONTENT / served).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, CONTENT / served)
            entries.append({
                "name": rel.name,
                "path": rel.as_posix(),
                "url": "content/" + served.as_posix(),
                "type": kind,
            })
            print(f"  {kind:8} {rel}")

    (OUT / "files.json").write_text(json.dumps(entries, indent=2), encoding="utf-8")
    for asset in (ROOT / "viewer").iterdir():
        shutil.copy2(asset, OUT / asset.name)
    (OUT / ".nojekyll").touch()
    print(f"Built {len(entries)} files -> {OUT}")


if __name__ == "__main__":
    main()
