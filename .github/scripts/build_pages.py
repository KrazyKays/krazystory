"""Construit le site GitHub Pages à partir de l'aide-mémoire.

- _site/index.html : copie de 00_PILOTAGE/aide_memoire.html, dont les images
  pointent vers le dossier img/ du site au lieu de ../SOURCES/images/.
- _site/img/*.jpg : miniatures (640 px) des images de SOURCES/images/.

Les fichiers du dépôt ne sont pas modifiés.
"""
import os
import re
import sys
import unicodedata

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_HTML = os.path.join(ROOT, "00_PILOTAGE", "aide_memoire.html")
SRC_IMG = os.path.join(ROOT, "SOURCES", "images")
OUT = os.path.join(ROOT, "_site")


def slug(name):
    # Même règle que la fonction slug() de la page.
    name = re.sub(r"\.png$", "", name)
    name = unicodedata.normalize("NFD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", name.lower()))


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
    print(f"Site construit : index.html + {count} images")


if __name__ == "__main__":
    main()
