# Journal des modifications

## 2026-11-09 — Promotion en canon des sources sans conflit (Q-01)

**Décision de l'auteur :** « Promeut en canon tout ce qui n'a pas de conflit. »

**Application :**
- 109 énoncés `[SOURCE]` passent en `[CANON]` dans `01_UNIVERS/` (artefact, arts martiaux, armes, mana, histoire), `02_PERSONNAGES/` (A, B, secondaires), `03_CHRONOLOGIE/chronologie.md` et `04_INTRIGUE/` (arcs, principes narratifs).
- 13 énoncés restent `[SOURCE]`, car ils relèvent d'une contradiction ouverte : `arts_martiaux.md` l.11, 13, 14 (C-03) ; `mana_et_cultivation.md` l.10, 11 (C-10), l.19, 20 (C-14) ; `B.md` l.8, 27 (C-09), l.13 (C-11), l.21 (C-04) ; `A.md` l.14, 19 (C-12).
- Blocs mixtes : les en-têtes des activations de l'artefact (`artefact.md` §3 et §4) et les « Déroulé » des arcs (`arcs.md`) passent en `[CANON]` avec la mention « hors points ouverts / hors points marqués `[CONFLIT]` ». Dans `artefact.md` §3, l'errance de « plus de 2000 ans » reçoit le marqueur `[CONFLIT C-09]`, qui manquait.
- Ne sont pas concernés : `[INTERPRÉTATION]`, `[HYPOTHÈSE]`, `[PROPOSITION]`, `[MANQUANT]`. Le tableau des cultivations garde ses cases † en `[INTERPRÉTATION]`.
- Q-01 retirée de `questions_ouvertes.md` ; `README.md` (règle et état d'avancement) et `aide_memoire.html` mis à jour.

**Sources modifiées :** aucune.

## 2026-11-09 — Publication de l'aide-mémoire sur GitHub Pages

**Ajout :** `.github/workflows/pages.yml` et `.github/scripts/build_pages.py`. À chaque modification de `aide_memoire.html` ou des images poussée sur `main`, GitHub Actions construit le site (page + miniatures des images) et le publie sur GitHub Pages. Le site est public, comme le dépôt.
**Autres fichiers modifiés :** `.gitignore` (dossier `_site/` généré). **Sources modifiées :** aucune.

## 2026-11-09 — Aide-mémoire visuel du projet

**Ajout :** `00_PILOTAGE/aide_memoire.html`, page de synthèse à la manière d'une cheatsheet (onglets, recherche plein texte, filtre par statut, galerie avec visionneuse). Elle résume la base de connaissances dans son état actuel, sans y ajouter d'information ; les statuts (`[CANON]`, `[SOURCE]`, etc.) et les références `[fichier:ligne]` sont conservés. Les images sont lues directement dans `SOURCES/images/`.
**Statut :** document de consultation ; les fiches de la base font foi. À régénérer quand la base évolue.
**Autres fichiers modifiés :** `00_PILOTAGE/README.md` (arborescence). **Sources modifiées :** aucune.

## 2026-11-09 — Résolution de C-16 et retrait des données périmées

**Décision de l'auteur intégrée (`[CANON]`) :** C-16, piste a. « Voisine » signifie « la ville la plus proche » : la capitale est à plusieurs jours de route du village de A, qui reste isolé. E-02 et PC-2 restent inchangés. La mention « village en périphérie de la capitale » (C-07) est retirée.

**Retrait des données périmées (demandé par l'auteur) :**
- `contradictions.md` : fiches résolues réduites à la décision (analyses initiales retirées, consultables dans git) ; fiches ouvertes regroupées, avec les trois pistes proposées pour chacune.
- `questions_ouvertes.md` : questions répondues retirées (Q-02, Q-03, Q-04, Q-06, Q-09, Q-12, Q-23) ; seules les parties restantes de Q-07, Q-10, Q-14 et Q-15 sont conservées. Chaque réponse retirée figure déjà dans la fiche concernée.
- `rapport_initial.md` : sections C à E remplacées par les seuls problèmes et recommandations encore valables.
- `chronologie.md` : mentions « fin du récit ? », note de correction et lecture pondérée de l'endurance (non retenue) retirées.
- `modifications_sources_a_faire.md` : tableau S-01 à S-04 (déjà appliquées) retiré.
- Autres retouches : `lieux.md`, `histoire_monde_et_factions.md`, `mana_et_cultivation.md`, `artefact.md`, `arcs.md`, `idees_et_scenes.md`, `principes_narratifs.md` (T-02, T-03), `catastrophes_propositions.md` (« proposés », « À décider », « Proposition »), `README.md`.

**Non modifiés volontairement :** ce journal (historique) ; `03_CHRONOLOGIE/courbes_A_B.html` (la lecture pondérée y reste consultable, marquée « non retenue ») ; `inventaire_sources.md`.
**Sources modifiées :** aucune.

## 2026-11-09 — Résolution de C-05, C-07, C-13 et C-15

**Décisions de l'auteur intégrées (`[CANON]`) :**
- C-15 (pistes a + c) : « toujours perfectible » est la réputation, fausse, de l'art de B ; le plafond du 10e cercle est la faille que le maître veut cacher. Seule la taille des cercles souples reste perfectible (plus de mana, donc plus de durée d'utilisation) ; leur nombre plafonne à 10.
- C-05 (piste a) : l'artefact n'a qu'une fonction, la méditation hors du temps ; les inscriptions sont imagées. Seule l'âme devient immortelle, car on peut la développer à l'infini dans l'artefact ; le corps reste soumis au temps.
- C-13 (piste c) : noyau = réservoir, cercle = niveau ; « cœur de mana » est le terme archaïque de l'époque de B, que seul B emploie à l'époque du récit, et que A finit par remarquer.
- C-07 (piste a) : la ville voisine est la capitale ; le village de A est en périphérie ; le groupe 1 de l'examen réunit les candidats de la capitale, nobles ou non.

**Nouveaux points :** C-16 (la décision C-07 heurte E-02, « cible isolée, loin de la capitale », et PC-2) ; Q-24 (développement de l'âme) ; Q-25 (moment où A remarque « cœur de mana »). Classement d'importance proposé non appliqué, faute de validation. Source supplémentaire de C-09 relevée : `arc 1.md:11`.

**Fichiers modifiés :** `05_COHERENCE/contradictions.md`, `05_COHERENCE/questions_ouvertes.md`, `01_UNIVERS/artefact.md`, `01_UNIVERS/glossaire.md`, `01_UNIVERS/arts_martiaux.md`, `01_UNIVERS/mana_et_cultivation.md`, `01_UNIVERS/lieux.md`, `01_UNIVERS/histoire_monde_et_factions.md`, `02_PERSONNAGES/B.md`, `03_CHRONOLOGIE/chronologie.md`, `04_INTRIGUE/arcs.md`, `00_PILOTAGE/modifications_sources_a_faire.md` (S-09 à S-13), `00_PILOTAGE/README.md`.
**Non modifié volontairement :** `04_INTRIGUE/catastrophes_propositions.md` (E-02 et PC-2 restent en l'état jusqu'à la décision sur C-16).
**Sources modifiées :** aucune.

## 2026-11-09 — Petite sœur de B, ironie dramatique

**Décisions de l'auteur intégrées (`[CANON]`) :**
- La petite sœur de B est née dans les deux vies ; seule sa trajectoire change (N-03).
- L'ironie dramatique liée à la 1re personne est assumée.

**Fichiers modifiés :** `04_INTRIGUE/catastrophes_propositions.md`, `04_INTRIGUE/principes_narratifs.md`, `03_CHRONOLOGIE/chronologie.md`, `02_PERSONNAGES/personnages_secondaires.md`.
**Sources modifiées :** aucune.

## 2026-11-09 — Catastrophes validées, point de vue, artefact brisé, mise à jour de la base

**Décisions de l'auteur intégrées (`[CANON]`) :**
- Catastrophes de la première vie de A : principes PC-1 à PC-6, événements E-01 à E-07 et N-01 à N-04 validés (`04_INTRIGUE/catastrophes_propositions.md`). → Q-09 clos.
- Première vie de A : jamais à l'académie ; famille en vie jusqu'à ses 16 ans. Le prince meurt dans la première vie. La mère de B quitte la politique dans la première vie.
- 1re personne pour chaque héros ; `[HYPOTHÈSE]` 3e personne pour les scènes réunissant A et B.
- L'artefact est brisé ; le mana de sa réserve est désormais en A et en B. → Q-23 clos ; Q-05 réduit à la raison de l'asymétrie.
- Longévité par la cultivation : interprétation confirmée.

**Mise à jour de la base (autorisée par l'auteur) :** retrait des mentions périmées (« 50 ans », C-01/C-02 encore listés comme ouverts, Q-03/Q-04, « aucun canon »). Ajout de la contradiction C-15 (art « toujours perfectible » / limite du 10e cercle), relevée précédemment mais non consignée.

**Fichiers modifiés :** `04_INTRIGUE/catastrophes_propositions.md`, `05_COHERENCE/questions_ouvertes.md`, `05_COHERENCE/contradictions.md`, `01_UNIVERS/artefact.md`, `01_UNIVERS/arts_martiaux.md`, `01_UNIVERS/mana_et_cultivation.md`, `02_PERSONNAGES/A.md`, `02_PERSONNAGES/personnages_secondaires.md`, `03_CHRONOLOGIE/chronologie.md`, `04_INTRIGUE/principes_narratifs.md`, `04_INTRIGUE/arcs.md`, `00_PILOTAGE/README.md`, `00_PILOTAGE/modifications_sources_a_faire.md`, `06_MANUSCRIT/README.md`.
**Non modifié volontairement :** `00_PILOTAGE/rapport_initial.md` (diagnostic daté, conservé tel quel).
**Sources modifiées :** aucune.

## 2026-11-09 — Portée du récit, style, Todag, artefact

**Décisions de l'auteur intégrées (`[CANON]`) :**
- Le récit va au-delà de 28–29 ans, grâce aux ellipses ; fin non fixée. A et B apprennent la vérité l'un sur l'autre au cours du récit, après de longs doutes (P-11).
- Point de vue alterné A/B ; ellipses entre des moments charnières très développés ; format web novel ; inspirations : *Tales of Demons and Gods*, *The Beginning After the End*.
- Todag = *Tales of Demons and Gods* ; seule la notion de « marées de monstres » est à éviter (P-10).
- L'artefact ne fonctionne plus dans la seconde ligne temporelle (réserve vidée lors du retour) ; aucune âme de B n'erre ; les ossements de B sont au temple.

**Fichiers créés :** `04_INTRIGUE/catastrophes_propositions.md` (propositions non validées, réponse à Q-09).
**Fichiers modifiés :** `05_COHERENCE/questions_ouvertes.md` (Q-06, Q-12, Q-14, Q-15 ; Q-23 ajoutée), `01_UNIVERS/artefact.md`, `04_INTRIGUE/principes_narratifs.md`, `04_INTRIGUE/arcs.md`, `03_CHRONOLOGIE/chronologie.md`, `06_MANUSCRIT/README.md`.
**Sources modifiées :** aucune.

## 2026-11-09 — Correction des sources et premier commit

**Sources modifiées (autorisation exceptionnelle de l'auteur) :**
- `SOURCES/timeline.md:5` : 50 → 70 années de cultivation (S-01).
- `SOURCES/scenario/arc 1.md:5` : « en seulement 50 ans » → « en seulement 70 ans » (S-02) ; « doublant ainsi son efficacité » → « ce qui accélérait sa progression » (S-03).
- `SOURCES/scenario/arc 3.md:11` : « cultiver deux fois plus vite que la normal » → « obtient donc deux fois plus de mana que la normale pour le même effort » (S-04).

Les numéros de ligne sont inchangés. Les modifications facultatives S-05 à S-08 n'ont pas été appliquées.
**Git :** premier commit de l'ensemble du projet (sources et base de connaissances), poussé sur `origin/main`.

## 2026-11-09 — Résolution de C-02

**Décisions de l'auteur intégrées (`[CANON]`) :**
- Première vie de B : 10 cercles en **70 ans** (au lieu de 50) ; seul un génie peut atteindre 10 cercles.
- Les cercles 8, 9 et 10 se cultivent un par un.
- Le bonus du sommeil est qualitatif, non chiffré.
- La cultivation allonge la durée de vie.

**Interprétation :** j'ai compris « je valide les deux points » comme « oui, la cultivation allonge la durée de vie ». *(Confirmé par l'auteur le 2026-11-09.)*

**Fichiers créés :** `00_PILOTAGE/modifications_sources_a_faire.md`.
**Fichiers modifiés :** `05_COHERENCE/contradictions.md` (C-02 résolu), `05_COHERENCE/questions_ouvertes.md` (Q-03 clos ; Q-21 et Q-22 ajoutés), `01_UNIVERS/mana_et_cultivation.md`, `02_PERSONNAGES/B.md`, `02_PERSONNAGES/personnages_secondaires.md`, `03_CHRONOLOGIE/chronologie.md`, `03_CHRONOLOGIE/courbes_A_B.html` (republié).
**Sources modifiées :** aucune ; 4 corrections sont à faire par l'auteur.

## 2026-11-09 — Consommation du mana et profil de combat

**Décisions de l'auteur intégrées (`[CANON]`) :**
- Une technique consomme du mana en quantité brute (endurance lue en quantité, non pondérée). → Q-04 clos.
- A peut combiner ses deux noyaux dans une même technique (×2 en puissance).
- Principe P-09 : les chiffres servent la cohérence ; le lecteur doit simplement sentir les deux profils (A : puissance, résistance, durée ; B : subtilité, tactique, coups très puissants mais brefs).

**Fichiers modifiés :** `01_UNIVERS/mana_et_cultivation.md`, `04_INTRIGUE/principes_narratifs.md`, `05_COHERENCE/questions_ouvertes.md`, `03_CHRONOLOGIE/courbes_A_B.html` (republié : réglages par défaut alignés sur les décisions).

## 2026-11-09 — Décisions sur la cultivation et courbes comparatives

**Décisions de l'auteur intégrées (`[CANON]`) :**
- A possède deux **noyaux**, dont les cercles évoluent en miroir : deux fois plus de mana pour le même effort, durées standard. → C-01 résolu.
- Règle « **accès et réserve** » : posséder un cercle donne accès à son rang ; les techniques puisent dans la réserve de ce cercle.

**Correction d'une erreur de l'assistant :** la règle de B avait été mal comprise (« n cercles en n années au total »). Règle exacte : chaque groupe de cercles coûte le numéro de son cercle le plus élevé, et les groupes s'additionnent. C-02 a été réécrit ; il reste ouvert sur le bonus du sommeil.

**Fichiers créés :** `03_CHRONOLOGIE/courbes_A_B.html` (publié en artefact privé).
**Fichiers modifiés :** `01_UNIVERS/mana_et_cultivation.md`, `02_PERSONNAGES/A.md`, `03_CHRONOLOGIE/chronologie.md`, `05_COHERENCE/contradictions.md`, `05_COHERENCE/questions_ouvertes.md`.
**Sources modifiées :** aucune.

## 2026-11-09 — Initialisation du projet

**Intervention :** analyse complète des sources et création de la base de connaissances.

**Fichiers créés :**
- `00_PILOTAGE/` : `README.md`, `inventaire_sources.md`, `rapport_initial.md`, `journal_modifications.md`
- `01_UNIVERS/` : `mana_et_cultivation.md`, `arts_martiaux.md`, `armes_de_mana.md`, `artefact.md`, `histoire_monde_et_factions.md`, `lieux.md`, `glossaire.md`
- `02_PERSONNAGES/` : `A.md`, `B.md`, `personnages_secondaires.md`
- `03_CHRONOLOGIE/` : `chronologie.md`
- `04_INTRIGUE/` : `principes_narratifs.md`, `arcs.md`, `idees_et_scenes.md`
- `05_COHERENCE/` : `contradictions.md`, `questions_ouvertes.md`
- `06_MANUSCRIT/` : `README.md`
- `07_REFERENCES_VISUELLES/` : `catalogue_images.md`

**Fichiers sources modifiés :** aucun.

**Décisions de l'auteur intégrées :** aucune (aucun élément n'a encore le statut `[CANON]`).

**En attente :** décisions sur les contradictions C-01 à C-14 et sur les questions Q-01 à Q-20.
