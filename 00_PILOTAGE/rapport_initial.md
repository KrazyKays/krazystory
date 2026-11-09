# Rapport initial — diagnostic des sources

> Rédigé le 2026-11-09. Les détails figurent dans les documents référencés ; ce rapport en donne la synthèse.

## A. Inventaire

- **Documents trouvés :** 42 fichiers dans `SOURCES/` (13 textes Markdown, 29 images PNG), plus `AGENTS.md`.
- **Documents analysés intégralement :** les 42.
- **Documents partiellement analysés ou inexploitables :** aucun.
- **Nature des informations :**
  - pitch et principes (`resume.md`, `principes.md`) ;
  - univers (`lore.md`) ;
  - chronologie chiffrée (`timeline.md`) ;
  - fiches des deux héros (`details A.md`, `details B.md`) ;
  - scénario en 5 arcs (`scenario/`) ;
  - idées libres (`idees.md`) ;
  - planches visuelles générées (personnages, artefact, armes, système de mana).
- **Volume :** environ 30 Ko de texte. Le matériau est dense mais court : c'est une **base de conception**, pas encore un plan de roman.

Détail : `inventaire_sources.md`.

## B. Synthèse

### Prémisse
Une **vieille érudite** (A), bloquée toute sa vie par des bases martiales médiocres, active à 93 ans un artefact oublié et revient au jour de sa naissance avec tous ses souvenirs. Sans le savoir, elle entraîne avec elle l'âme d'un **grand maître mort il y a 2000 ans** (B), qui se réincarne au même instant dans un nouveau-né. B n'existait pas dans la première vie de A : sa présence fait dévier le futur que A croit connaître. Les deux héros coopèrent pour empêcher les catastrophes à venir, chacun ignorant le secret de l'autre.

### Grandes catégories d'idées
1. **Système de cultivation** : noyau, cercles imbriqués, progression chiffrée, paliers, mesure par gemme, puissance ×10 par cercle. C'est la partie la plus développée.
2. **Deux parcours symétriques** : dur/souple, puissance/vitesse, proche/distance, retour dans son propre corps / réincarnation dans le corps d'un autre, savoir du futur / savoir du passé.
3. **L'artefact et le mana temporel** : moteur du concept, à l'origine de leur avantage commun.
4. **Histoire du monde** : colonisation d'un continent de monstres, grand assaut orchestré par la guilde de l'ombre, simplification des arts martiaux.
5. **Intrigue de prévention** : un futur catastrophique connu (prise de la ville par la guilde, ultime assaut) à déjouer.
6. **Vie à l'académie** : examen, élite, noblesse, rivaux, expédition.

### Concepts récurrents
Le mana de l'artefact, les bases et fondations (le défaut de A, la force de B), les limites et leur dépassement, le secret, la guilde de l'ombre, le temple.

### Relations entre les idées
- **Fil le plus solide :** le rival de B, rallié à la guilde avec une version dérivée de l'art de B `[lore.md:34]`, et la guilde qui détruit le futur de A `[lore.md:41]`. Le passé de B et le futur de A sont donc reliés **par le même antagoniste**. C'est le principal levier d'unité du récit, et il n'est pas encore exploité dans les arcs.
- **Deuxième fil :** le temple. A y a trouvé les ossements de B ; tous deux veulent y retourner (arc 5).
- **Troisième fil :** l'effet papillon. Les actes de B, qui n'existait pas dans la première vie de A, faussent ses prédictions.

## C. Problèmes détectés

Détail complet : `05_COHERENCE/contradictions.md`.

### Contradictions (14 fiches)
| Importance | Fiches |
|---|---|
| **Haute** | **C-01** : A cultive-t-elle 2 fois plus vite ou possède-t-elle 2 fois plus de mana ? (la chronologie suit le rythme normal). **C-02** : 10 cercles en 50 ans pour B, incompatible avec le rythme de son art en seconde vie (n cercles en n années). |
| Moyenne | C-03 (art « très répandu » mais perdu), C-04 (moment où B trouve la solution), C-05 (fonction de l'artefact), C-07 (B né dans la ville voisine mais membre du groupe des nobles de la capitale), C-13 (noyau / cercle / cœur employés l'un pour l'autre). |
| Faible | C-06, C-08, C-09, C-10, C-11, C-12, C-14. |

### Informations manquantes (les plus structurantes)
1. **La liste et les dates des catastrophes de la première vie de A.** C'est le moteur annoncé du récit `[resume.md:35]`, et il est entièrement vide.
2. Les arcs après l'expédition, et la fin.
3. La famille de A (« A ecrire »).
4. Les noms : aucun personnage, lieu ou pays n'est nommé.
5. La géographie (village, ville voisine, capitale, temple).
6. L'état de la guilde de l'ombre à l'époque du récit.
7. Les choix d'écriture (point de vue, ton, format).

### Ambiguïtés
- Quantité de mana ou puissance : ce que mesure la gemme, et comment comparer A et B (Q-04). Avec la règle du ×10 par cercle, B devient nettement plus puissant que A dès 15 ans ; le bonus ×2 de A pèse peu en comparaison.
- Asymétrie du mana de l'artefact : A reçoit un noyau complet, B des « résidus » (Q-05).
- Sort de l'artefact dans la seconde ligne temporelle (Q-06).

### Doublons
Paragraphe répété dans `arc 2.md` (l.3 et l.5) ; récit de l'artefact en trois versions ; prémisse répétée dans plusieurs fichiers (sans divergence). Aucun doublon problématique.

### Chronologie et continuité
- Les progressions chiffrées de A et de B sont **cohérentes en interne** (vérifiées année par année), à C-01 et C-02 près.
- Aucune catastrophe n'est datée dans la première vie de A.
- Les âges de l'expédition (arc 5) et de la rencontre de l'ennemi puissant (`idees.md`) ne sont pas fixés.

### Risques éditoriaux (hors contradictions)
- **T-01** : le principe « un minimum de personnes ouvertement mauvaises » se heurte aux rivaux « détestables » et aux nobles « très hautains ». C'est une question de dosage.
- **T-02** : si « Todag » désigne *Tales of Demons and Gods*, la guilde qui orchestre les monstres et infiltre le pouvoir pour faire tomber la ville en est très proche. Ce point mérite une décision consciente.

## D. Questions à te poser

20 questions classées par priorité dans `05_COHERENCE/questions_ouvertes.md`. Les **bloquantes** (priorité 1) :

1. **Q-01** : promouvoir en canon tout ce qui n'est pas en conflit, d'un bloc, ou valider thème par thème ?
2. **Q-02 / C-01** : le double noyau double-t-il la vitesse ou la quantité ?
3. **Q-03 / C-02** : comment expliquer les 50 ans de B ?
4. **Q-04** : équilibre de puissance entre A et B ; est-il voulu que B la dépasse nettement ?
5. **Q-09** : quelles catastrophes, et quand ?
6. **Q-15** : point de vue, ton, format, texte de référence pour le style ?

## E. Organisation proposée

**Mise en place lors de cette phase :**
- Arborescence de 8 dossiers numérotés à côté de `SOURCES/`, qui reste intact (voir `README.md`).
- Système de statuts (`[SOURCE]`, `[CANON]`, `[HYPOTHÈSE]`, `[INTERPRÉTATION]`, `[PROPOSITION]`, `[CONFLIT]`, `[MANQUANT]`) et référence systématique `[fichier:ligne]`.
- Journal des modifications.

**Recommandations `[PROPOSITION]` :**
1. **Versionner les sources avec git.** Le dépôt existe mais ne contient aucun commit ; un premier commit protégerait les originaux contre toute perte ou modification involontaire. Je ne le fais pas sans ton accord.
2. **Trancher d'abord C-01, C-02 et Q-04** : ils conditionnent toute la mécanique de puissance et les scènes de combat.
3. **Établir la liste des catastrophes (Q-09)** avant de structurer les arcs 3 à 5 : l'intrigue en dépend.
4. **Fixer un glossaire** (noyau / cercle / cœur ; retour / réincarnation) avant toute rédaction.
5. **Ajouter une fiche par personnage secondaire** dès qu'il est nommé ou validé.
6. Plus tard, un **plan chapitre par chapitre** dans `06_MANUSCRIT/README.md`, une fois les arcs stabilisés.
