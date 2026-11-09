# Base de connaissances du projet — Mode d'emploi

> Document de pilotage. Créé le 2026-11-09 lors de la phase d'initialisation.

## 1. Arborescence

| Dossier | Rôle |
|---|---|
| `SOURCES/` | **Sources originales de l'auteur. Jamais modifiées, déplacées ni renommées sans son autorisation explicite.** |
| `00_PILOTAGE/` | Mode d'emploi, inventaire, rapport de diagnostic, journal des modifications. |
| `01_UNIVERS/` | Système de mana, arts martiaux, armes, artefact, histoire du monde et factions, lieux, glossaire. |
| `02_PERSONNAGES/` | Fiches de A, de B et des personnages secondaires. |
| `03_CHRONOLOGIE/` | Chronologie des événements et progression de la cultivation. |
| `04_INTRIGUE/` | Principes narratifs, arcs, idées et scènes potentielles. |
| `05_COHERENCE/` | Contradictions recensées et questions ouvertes. |
| `06_MANUSCRIT/` | Textes narratifs (vide pour l'instant : aucune rédaction avant validation). |
| `07_REFERENCES_VISUELLES/` | Catalogue commenté des images de `SOURCES/images/`. |

## 2. Statuts des informations

Chaque information de la base porte l'un des statuts suivants, conformément à `AGENTS.md` §6.

| Statut | Signification |
|---|---|
| `[SOURCE]` | Énoncé présent dans tes notes, repris fidèlement. **Pas encore validé comme canon.** |
| `[CANON]` | Information que tu as explicitement validée. |
| `[HYPOTHÈSE]` | Élément présenté comme incertain dans les sources (point d'interrogation, formulation hésitante). |
| `[INTERPRÉTATION]` | Ma lecture d'un passage ambigu ou un calcul déduit des sources. À confirmer. |
| `[PROPOSITION]` | Suggestion de ma part. Jamais considérée comme décidée. |
| `[CONFLIT C-xx]` | Sources incompatibles. Les deux versions sont conservées ; voir `05_COHERENCE/contradictions.md`. |
| `[MANQUANT]` | Information absente des sources et nécessaire tôt ou tard. |

Promotion vers `[CANON]` : uniquement après ta validation explicite, avec une entrée dans le journal.

## 3. Références aux sources

Format : `[fichier:ligne]`, chemins relatifs à `SOURCES/`.
Exemples : `[lore.md:25]`, `[arc 3.md:11]`, `[details B.md:11]`, `[img: artefact 2.png]`.

Les numéros de ligne correspondent à l'état des fichiers au 2026-11-09. Si tu modifies une source, les références peuvent se décaler : signale-le-moi pour que je les mette à jour.

## 4. Méthode de collaboration

### Quand tu m'envoies des idées brutes
1. Je reformule ce que j'ai compris, en séparant le sens certain des ambiguïtés.
2. Je propose une mise en forme (note structurée, passage, fiche).
3. Je signale les impacts : contradictions avec l'existant, conséquences sur la chronologie, sur les personnages, etc.
4. Rien n'entre dans la base sans ta validation. Une idée validée est intégrée avec le statut adapté et journalisée.

### Quand tu me demandes de rédiger
1. Je vérifie les fiches concernées avant d'écrire.
2. Je rédige dans `06_MANUSCRIT/` en respectant tes consignes de style.
3. Je joins une note séparée : choix effectués, éléments ajoutés que tu n'avais pas précisés (signalés comme tels), points de cohérence.

### Quand tu me demandes une relecture
Je classe les remarques en quatre catégories (AGENTS.md §5) : erreurs objectives, problèmes de rédaction, problèmes narratifs, suggestions éditoriales.

### Nouvelles sources
Dépose tes nouvelles notes dans `SOURCES/` (ou donne-les-moi directement dans la conversation). J'ajouterai le fichier à l'inventaire et je l'intégrerai à la base.

## 5. État d'avancement

| Étape | État |
|---|---|
| Inventaire des sources | Terminé — 13 textes et 29 images, tous examinés intégralement |
| Structuration de la base | Terminé (première version) |
| Diagnostic initial | Terminé — voir `rapport_initial.md` |
| Résolution des contradictions | En cours — C-01, C-02, C-05, C-07, C-13, C-15 et C-16 résolus ; voir `05_COHERENCE/contradictions.md` |
| Catastrophes de la première vie de A | Structure validée — `04_INTRIGUE/catastrophes_propositions.md` |
| Rapport initial | Diagnostic du 2026-11-09, épuré de ses éléments périmés |
| Rédaction du manuscrit | Non commencée (volontairement) |
