"""Construit le site GitHub Pages à partir de l'aide-mémoire.

- _site/index.html : copie de 00_PILOTAGE/aide_memoire.html, dont les images
  pointent vers le dossier img/ du site au lieu de ../SOURCES/images/.
- _site/img/*.jpg : miniatures (640 px) des images de SOURCES/images/.
- Le manuscrit (textes de 06_MANUSCRIT/, hors README, notes et _versions/)
  est injecté dans la constante MANUSCRIT de la page, pour l'onglet Lecture.
  Ordre de lecture : ordre alphabétique des chemins (00_prologues/,
  arc_01_.../ch_01_..., etc.).

Les fichiers du dépôt ne sont pas modifiés.
"""
import json
import os
import re
import sys
import unicodedata

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_HTML = os.path.join(ROOT, "00_PILOTAGE", "aide_memoire.html")
SRC_IMG = os.path.join(ROOT, "SOURCES", "images")
SRC_MS = os.path.join(ROOT, "06_MANUSCRIT")
OUT = os.path.join(ROOT, "_site")


def slug(name):
    # Même règle que la fonction slug() de la page.
    name = re.sub(r"\.png$", "", name)
    name = unicodedata.normalize("NFD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", name.lower()))


def part_label(folder):
    # "00_prologues" -> "Prologues" ; "arc_01_enfances" -> "Arc 01 — enfances"
    m = re.match(r"^arc_(\d+)_?(.*)$", folder)
    if m:
        rest = m.group(2).replace("_", " ").strip()
        return f"Arc {m.group(1)}" + (f" — {rest}" if rest else "")
    label = re.sub(r"^\d+_", "", folder).replace("_", " ").strip()
    return label[:1].upper() + label[1:] if label else "Manuscrit"


def manuscript():
    """Textes du manuscrit, dans l'ordre de lecture."""
    chapters = []
    for dirpath, dirnames, filenames in os.walk(SRC_MS):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith((".", "_")))
        for name in sorted(filenames):
            if not name.endswith(".md") or name == "README.md" or name.endswith("_notes.md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, SRC_MS).replace(os.sep, "/")
            lines = open(path, encoding="utf-8").read().splitlines()
            title, status, i = os.path.splitext(name)[0], "", 0
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and lines[i].startswith("# "):
                title = lines[i][2:].strip()
                i += 1
            # En-tête de travail (blockquote de statut, puis séparateur) : retiré du texte lu.
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith(">")):
                m = re.search(r"Statut\s*:\s*`([^`]+)`", lines[i])
                if m:
                    status = m.group(1).strip()
                i += 1
            if i < len(lines) and lines[i].strip() == "---":
                i += 1
            text = "\n".join(lines[i:]).strip()
            if not text:
                continue
            prose = re.sub(r"^\s*(-{3,}|#+.*)\s*$", "", text, flags=re.M)
            words = len(re.findall(r"[\w’'-]+", prose))
            folder = rel.split("/")[0] if "/" in rel else ""
            chapters.append({"id": rel, "partie": part_label(folder) if folder else "Manuscrit",
                             "titre": title, "statut": status, "mots": words, "texte": text})
    chapters.sort(key=lambda c: c["id"])
    return chapters


def main():
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)

    html = open(SRC_HTML, encoding="utf-8").read()
    for old, new in (
        ('const IMG_BASE = "../SOURCES/images/";', 'const IMG_BASE = "img/";'),
        ("const IMG_EXT = null;", 'const IMG_EXT = ".jpg";'),
    ):
        if old not in html:
            sys.exit(f"Ligne introuvable dans aide_memoire.html : {old}")
        html = html.replace(old, new)

    chapters = manuscript()
    old = "const MANUSCRIT = [];"
    if old not in html:
        sys.exit(f"Ligne introuvable dans aide_memoire.html : {old}")
    data = json.dumps(chapters, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace(old, f"const MANUSCRIT = {data};")

    # Le squelette que la page suppose (doctype, charset, viewport).
    head = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
    body_at = html.index("</style>") + len("</style>")
    html = head + html[:body_at] + "\n</head>\n<body>\n" + html[body_at:] + "\n</body>\n</html>\n"
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)

    count = 0
    for name in sorted(os.listdir(SRC_IMG)):
        if not name.lower().endswith(".png"):
            continue
        im = Image.open(os.path.join(SRC_IMG, name)).convert("RGB")
        im.thumbnail((640, 640))
        im.save(os.path.join(OUT, "img", slug(name) + ".jpg"), quality=80, optimize=True)
        count += 1
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"Site construit : index.html + {count} images + {len(chapters)} texte(s) du manuscrit")


if __name__ == "__main__":
    main()
