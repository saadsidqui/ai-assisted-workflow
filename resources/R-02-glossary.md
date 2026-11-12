---
id: R-02
title: Glossaire
card: .ai/project/spec/curriculum/resources/R-02-glossary-seed.md
status: review
last_verified: "2026-11-10"
native_review: done 2026-11-11
---

<!-- Policy and author-settled terms: .ai/project/decisions/0014-terminology-policy.md, 0015-glossary-terms-settled-by-the-author.md and 0016-fictional-engagement.md. Names of the program's parts: 0012-program-names.md. Every GDT link was opened on 2026-11-10. -->

# Glossaire

Ce glossaire fixe les termes du programme « Travailler avec l’IA ». Chaque terme a une seule forme dans les leçons, les diapositives, les notes de présentation et les documents d’accompagnement. En cas de doute, ce glossaire fait foi.

## Politique terminologique

1. Le Grand dictionnaire terminologique (GDT) de l’Office québécois de la langue française privilégie un terme pour la notion : on l’emploie. Le terme anglais figure une fois, en italique, à la première mention.
2. Le GDT n’a pas de fiche pour la notion : on emploie un mot courant du français, s’il dit exactement la même chose.
3. Sinon, on garde le terme anglais, en italique à la première mention.
4. Les noms de produits, de fichiers, de commandes et de paramètres ne se traduisent pas.
5. Un terme, une seule forme. Quand le GDT privilégie plusieurs termes, le glossaire en retient un.

Chaque entrée renvoie à la fiche du GDT consultée, avec sa date de mise à jour et la date de consultation. La mention « aucune fiche du GDT » indique qu’une recherche faite à la date donnée n’a trouvé aucune fiche pour cette notion.

## Noms des parties du programme

Les parties du programme portent ces noms dans tous les documents en français.

| Anglais | Français |
|---|---|
| Common core | Tronc commun |
| Engineering track | Parcours Génie logiciel |
| Product and experience track | Parcours Produit et expérience |
| Business and people track | Parcours Gestion et affaires |
| Overlays | Modules transversaux |

## Étapes de la boucle de travail

La boucle de travail compte huit étapes. Elles portent ces noms dans tous les documents en français, toujours dans cet ordre.

| Anglais | Français |
|---|---|
| Frame | Cadrer |
| Give context | Donner le contexte |
| Ask | Demander |
| Inspect | Examiner |
| Iterate | Itérer |
| Verify | Vérifier |
| Approve | Approuver |
| Capture | Conserver |

## Termes

Les entrées suivent l’ordre alphabétique du terme retenu.

### agent

- **Anglais :** *agent*.
- **Définition :** modèle qui travaille en boucle avec des outils pour atteindre un objectif : il planifie, agit, vérifie et recommence.
- **Exemple :** l’agent compare les chiffres de trois rapports et prépare un tableau, qu’il vous soumet avant tout envoi.
- **Règle :** 1.
- **Source :** GDT, fiche [« agent intelligent »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8394387/agent-intelligent), mise à jour en 2018, consultée le 10 novembre 2026.
- **Introduit dans :** C-01 et C-08.
- **Emploi :** « agent » seul suffit en contexte. Pour la catégorie de systèmes, voir « IA agentive ».

### application

- **Anglais :** *application*, le produit construit autour du modèle.
- **Définition :** produit construit autour du modèle, comme une application de clavardage ou une extension d’environnement de développement.
- **Exemple :** le même modèle peut répondre dans l’application de clavardage de l’équipe et dans l’extension de votre éditeur de code.
- **Règle :** 1.
- **Source :** GDT, fiche [« outil d’intelligence artificielle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26574413/outil-dintelligence-artificielle), mise à jour en 2024, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** le GDT privilégie aussi « application d’intelligence artificielle » et « outil d’intelligence artificielle ». Le glossaire retient « application », car « outil » désigne ce que l’application laisse le modèle utiliser (voir ce terme).

### assistant

- **Anglais :** *assistant*.
- **Définition :** application d’IA avec laquelle vous conversez en langage courant pour accomplir une tâche.
- **Exemple :** vous demandez à l’assistant de résumer un compte rendu de réunion en cinq points, puis vous vérifiez chaque point.
- **Règle :** 1.
- **Source :** GDT, fiche [« assistant virtuel »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26541739/assistant-virtuel), mise à jour en 2023, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** « assistant virtuel » à la première mention, puis « assistant ».

### autorisation

- **Anglais :** *permission*. Les réglages *allow*, *ask* et *deny* se disent « autoriser », « demander » et « refuser ».
- **Définition :** droit accordé à un agent d’effectuer une action précise, comme lire un fichier ou lancer une commande.
- **Exemple :** les réglages autorisent la lecture des fichiers, demandent une confirmation avant toute commande et refusent l’accès au dossier des secrets.
- **Règle :** 1, et 4 pour les noms de paramètres, qui restent en anglais.
- **Source :** GDT, fiche [« autorisation d’accès »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8374340/autorisation-dacces), mise à jour en 1999, consultée le 10 novembre 2026.
- **Introduit dans :** E-03.2.

### bac à sable

- **Anglais :** *sandbox*.
- **Définition :** environnement isolé où un agent peut exécuter du code ou des commandes sans toucher au reste du système.
- **Exemple :** vous laissez l’agent essayer sa correction dans un bac à sable avant de l’appliquer au projet.
- **Règle :** 1.
- **Source :** GDT, fiche [« bac à sable »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26520079/bac-a-sable), mise à jour en 2022, consultée le 10 novembre 2026.
- **Introduit dans :** E-03.3.
- **Emploi :** le GDT privilégie aussi « espace de test ». Le glossaire retient « bac à sable ».

### branche

- **Anglais :** *branch*.
- **Définition :** ligne de développement parallèle dans un dépôt, qui permet de préparer des modifications sans toucher à la version principale.
- **Exemple :** l’agent travaille sur une branche à part, et vous examinez ses modifications avant de les fusionner.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour le sens de la gestion de versions (recherche du 10 novembre 2026).
- **Introduit dans :** E-02.

### classification de sécurité

- **Anglais :** *data classification*.
- **Définition :** niveau attribué à une donnée selon sa valeur et la protection qu’elle exige, par exemple public, interne ou confidentiel.
- **Exemple :** avant de joindre un document à une requête, vous vérifiez sa classification de sécurité dans la politique de l’organisation.
- **Règle :** 1.
- **Source :** GDT, fiche [« classification de sécurité »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8358398/classification-de-securite), mise à jour en 2004, consultée le 10 novembre 2026.
- **Introduit dans :** C-07.
- **Emploi :** « classification » seul suffit en contexte. Les niveaux varient d’une organisation à l’autre.

### commit

- **Forme retenue :** *commit*, en italique à la première mention.
- **Définition :** enregistrement, dans un dépôt, d’un ensemble de modifications accompagné d’un message qui les décrit.
- **Exemple :** après chaque petite étape vérifiée, vous créez un *commit* qui explique ce qui a changé et pourquoi.
- **Règle :** 4, nom d’une commande de Git (`git commit`).
- **Source :** GDT, fiche [« archiver »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8870443/archiver), mise à jour en 2002, consultée le 10 novembre 2026. Le GDT privilégie le verbe « archiver » et déconseille « commit ».
- **Introduit dans :** E-02.
- **Emploi :** « archiver » figure une fois, à la première mention, comme terme du GDT. Comme verbe, écrivez « créer un commit ».

### connecteur

- **Anglais :** *connector*.
- **Définition :** lien qui donne à une application d’IA accès aux données d’un autre système, comme une messagerie ou un dossier partagé.
- **Exemple :** avant d’activer le connecteur de la messagerie, vous vérifiez quelles données il pourra lire et envoyer.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** C-05 et C-07.

### consigne

- **Anglais :** *brief*, au sens de la demande qu’on adresse à l’assistant.
- **Définition :** demande structurée que vous adressez à l’assistant : l’objectif, le contexte, les contraintes et le résultat attendu.
- **Exemple :** votre consigne précise le public visé et la longueur maximale du texte.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026). La fiche [« énoncé de projet »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8403165/enonce-de-projet) vise le *project brief*, une autre notion.
- **Introduit dans :** C-04.
- **Emploi :** « donner une consigne » rend *to brief*. Le terme anglais figure une fois, à la première mention. Le gabarit réutilisable de C-04 s’appelle le « gabarit de consigne ».

### critères d’acceptation

- **Anglais :** *acceptance criteria*.
- **Définition :** conditions vérifiables qu’un résultat doit remplir pour être jugé terminé.
- **Exemple :** le récit utilisateur fixe trois critères d’acceptation, dont un délai de réponse inférieur à deux secondes.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026). La fiche [« critère d’acceptation »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/3298690/critere-dacceptation) (AFNOR, 1977) vise le contrôle par échantillonnage, une autre notion.
- **Introduit dans :** P-02.

### date limite des connaissances

- **Anglais :** *knowledge cutoff*.
- **Définition :** date après laquelle le modèle n’a plus de données d’entraînement, si bien qu’il ignore les faits plus récents.
- **Exemple :** pour un règlement modifié le mois dernier, vous fournissez le nouveau texte, car il est postérieur à la date limite des connaissances.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** C-01.

### demande de fusion

- **Anglais :** *pull request* (PR).
- **Définition :** demande d’intégrer les modifications d’une branche à la branche principale, après examen et tests.
- **Exemple :** l’agent ouvre une demande de fusion, et une personne de l’équipe la relit avant de l’accepter.
- **Règle :** 1.
- **Source :** GDT, fiche [« demande de fusion »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26584234/demande-de-fusion), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** E-02.
- **Emploi :** le GDT donne aussi l’anglais *merge request*.

### demande d’offres de services

- **Anglais :** *request for proposals* (RFP).
- **Définition :** demande par laquelle un client invite quelques firmes à lui soumettre une offre de services pour un contrat.
- **Exemple :** la demande d’offres de services de Location Pavois énumère six exigences et fixe la date limite des réponses.
- **Règle :** 2.
- **Source :** aucune fiche de l’OQLF pour cette notion (recherche du 10 novembre 2026). Le GDT reproduit deux fiches sans terme privilégié : [« demande d’offres de services »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/507660/demande-doffres-de-services) (ICCA, 2006) et [« demande de propositions »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26511021/demande-de-propositions) (FMI, 2011).
- **Introduit dans :** B-04.
- **Emploi :** la réponse est une « offre de services » (voir ce terme). Au GDT, « appel d’offres » rend *call for tenders*, une autre procédure.

### dépôt

- **Anglais :** *repository*, *repo*.
- **Définition :** espace où sont conservés les fichiers d’un projet avec l’historique de leurs versions.
- **Exemple :** le dépôt contient le code du projet et le fichier d’instructions de l’agent.
- **Règle :** 1.
- **Source :** GDT, fiche [« dépôt de code source »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26584236/depot-de-code-source), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** E-02.
- **Emploi :** « dépôt » seul suffit en contexte.

### diff

- **Forme retenue :** *diff*, en italique à la première mention.
- **Définition :** affichage des lignes ajoutées, supprimées ou modifiées entre deux versions d’un fichier.
- **Exemple :** avant d’accepter la correction, vous lisez le *diff* ligne par ligne.
- **Règle :** 3, et 4 pour la commande `git diff`.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** E-02.

### document d’accompagnement

- **Anglais :** *handout*.
- **Définition :** document d’une page remis aux personnes participantes, qu’elles gardent pour appliquer la séance dans leur travail.
- **Exemple :** le document d’accompagnement sur la boucle de travail reprend en une page les étapes vues en séance.
- **Règle :** 1.
- **Source :** GDT, fiche [« document d’accompagnement »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26559981/document-daccompagnement) (FranceTerme, 2021), consultée le 10 novembre 2026.
- **Introduit dans :** C-04.
- **Emploi :** le GDT privilégie aussi « document d’appui ». Le glossaire retient « document d’accompagnement ». Le mot « fiche » désigne seulement une fiche de module ou une fiche du GDT.

### document de passation

- **Anglais :** *handover document*.
- **Définition :** document qui transmet un système livré à l’équipe qui l’exploitera : son fonctionnement, son administration et ce qu’il faut surveiller.
- **Exemple :** à la livraison, le chargé de projet remet le document de passation à l’équipe informatique du client.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour cette notion (recherche du 10 novembre 2026).
- **Introduit dans :** X-03.
- **Emploi :** de la même famille que « passation ». La note de passation transmet le travail d’une session à la suivante; le document de passation transmet un système à l’équipe du client.

### énoncé de projet

- **Anglais :** *project brief*.
- **Définition :** court document qui présente un projet : son but, son public, ses contraintes et ses échéances.
- **Exemple :** vous joignez l’énoncé de projet à chaque nouvelle conversation pour que l’assistant connaisse le contexte.
- **Règle :** 1.
- **Source :** GDT, fiche [« énoncé de projet »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8403165/enonce-de-projet), mise à jour en 1992, consultée le 10 novembre 2026.
- **Introduit dans :** C-05.
- **Emploi :** à distinguer de la « consigne », qui décrit une tâche confiée à l’assistant.

### entraînement

- **Anglais :** *training*.
- **Définition :** processus au cours duquel un modèle ajuste ses paramètres à partir d’un très grand volume de données.
- **Exemple :** le modèle n’a pas vu les documents internes de l’organisation pendant son entraînement, donc il ne les connaît pas.
- **Règle :** 1.
- **Source :** GDT, fiche [« entraînement »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26574362/entrainement), mise à jour en 2024, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** le GDT réserve « apprentissage » au terme générique.

### fenêtre de contexte

- **Anglais :** *context window*.
- **Définition :** quantité maximale d’information que le modèle prend en compte à la fois : requête, conversation et documents joints.
- **Exemple :** dans une très longue conversation, les premiers échanges peuvent sortir de la fenêtre de contexte.
- **Règle :** 1.
- **Source :** GDT, fiche [« fenêtre de contexte »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26580666/fenetre-de-contexte), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01 et C-05.
- **Emploi :** le GDT privilégie aussi « longueur de contexte ». Le glossaire retient « fenêtre de contexte ».

### fichier d’instructions

- **Anglais :** *instruction file*.
- **Définition :** fichier placé dans un projet, que l’agent lit au début de chaque session pour connaître les règles de travail.
- **Exemple :** le fichier d’instructions rappelle à l’agent de lancer les tests avant de proposer une modification.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** E-03.1.

### fine-tuning

- **Forme retenue :** *fine-tuning*, en italique à la première mention.
- **Définition :** entraînement complémentaire d’un modèle existant sur un ensemble restreint de données, pour l’adapter à une tâche ou à un domaine.
- **Exemple :** le fournisseur propose un *fine-tuning* du modèle sur les réponses validées du service à la clientèle.
- **Règle :** 3.
- **Source :** aucune fiche du GDT pour la notion en intelligence artificielle (recherche du 10 novembre 2026). La fiche [« apprentissage par transfert »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26577039/apprentissage-par-transfert) (FranceTerme, 2024) correspond à l’anglais *transfer learning*, une notion voisine.
- **Introduit dans :** C-01 (sujet facultatif).

### flux de travaux

- **Anglais :** *workflow*.
- **Définition :** suite d’étapes organisées selon des règles établies, qui mène à un produit ou à un service.
- **Exemple :** dans le flux de travaux de l’équipe, chaque texte produit avec l’IA passe par une révision humaine avant publication.
- **Règle :** 1.
- **Source :** GDT, fiche [« flux de travaux »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8362151/flux-de-travaux), mise à jour en 2009, consultée le 10 novembre 2026.
- **Introduit dans :** C-04.
- **Emploi :** « travaux » au pluriel, comme au GDT.

### génération augmentée par récupération

- **Anglais :** *retrieval-augmented generation*.
- **Définition :** méthode qui fournit au modèle des passages tirés de sources externes au moment de la requête, pour fonder sa réponse.
- **Exemple :** l’application documentaire de l’organisation utilise la génération augmentée par récupération : elle cite les pages d’où vient chaque réponse.
- **Règle :** 1.
- **Source :** GDT, fiche [« génération augmentée par récupération »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26584182/generation-augmentee-par-recuperation), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** le sigle « RAG », que le GDT admet dans ce domaine, suit le terme à la première mention.

### grand modèle de langage

- **Anglais :** *large language model* (LLM).
- **Définition :** modèle entraîné sur une très grande quantité de texte, qui produit la suite la plus plausible d’un texte donné.
- **Exemple :** le grand modèle de langage rédige un premier jet du courriel, que vous corrigez avant de l’envoyer.
- **Règle :** 1.
- **Source :** GDT, fiche [« grand modèle de langage »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26570880/grand-modele-de-langage), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** le sigle « LLM » figure à la première mention seulement. Ensuite, le terme complet ou « modèle ».

### hallucination

- **Anglais :** *hallucination*.
- **Définition :** contenu faux ou inventé qu’un modèle présente comme un fait.
- **Exemple :** l’assistant cite un article de loi qui n’existe pas : c’est une hallucination, que vous repérez en vérifiant la source.
- **Règle :** 1.
- **Source :** GDT, fiche [« hallucination d’IA »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26571221/hallucination-dia), mise à jour en 2023, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.

### hook

- **Forme retenue :** *hook*, en italique à la première mention. Quand il désigne un paramètre d’un outil, il s’écrit comme dans l’outil.
- **Définition :** commande qui s’exécute automatiquement à un moment précis du travail de l’agent, par exemple après chaque modification de fichier.
- **Exemple :** un *hook* lance les tests après chaque modification de l’agent.
- **Règle :** 3, et 4 pour le nom d’un paramètre.
- **Source :** aucune fiche du GDT pour le sens logiciel (recherche du 10 novembre 2026).
- **Introduit dans :** E-03.2.

### IA agentive

- **Anglais :** *agentic AI*.
- **Définition :** IA conçue pour poursuivre un objectif de façon autonome : elle planifie, utilise des outils et découpe le travail en sous-tâches.
- **Exemple :** un service d’IA agentive réserve une salle et invite les personnes, puis attend votre approbation.
- **Règle :** 1.
- **Source :** GDT, fiche [« intelligence artificielle agentive »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26578856/intelligence-artificielle-agentive), mise à jour en 2026, consultée le 10 novembre 2026.
- **Introduit dans :** C-02.
- **Emploi :** forme longue « intelligence artificielle agentive » à la première mention. Le GDT privilégie aussi « IA agentique ». Le glossaire retient « agentive ».

### IA générative

- **Anglais :** *generative AI*.
- **Définition :** IA qui produit du contenu nouveau, comme du texte, des images ou du son, à partir d’une requête.
- **Exemple :** l’équipe des communications utilise l’IA générative pour proposer trois titres, puis elle en choisit un.
- **Règle :** 1.
- **Source :** GDT, fiche [« intelligence artificielle générative »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26561649/intelligence-artificielle-generative), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** forme longue « intelligence artificielle générative » à la première mention.

### infiltration de requête

- **Anglais :** *prompt injection*.
- **Définition :** attaque qui cache des instructions malveillantes dans un contenu que le modèle lit, pour détourner son comportement.
- **Exemple :** une page Web contient un texte invisible qui ordonne à l’agent d’envoyer vos fichiers : c’est une infiltration de requête.
- **Règle :** 1.
- **Source :** GDT, fiche [« infiltration de requête »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26570960/infiltration-de-requete), mise à jour en 2023, consultée le 10 novembre 2026.
- **Introduit dans :** C-07.
- **Emploi :** le GDT privilégie aussi « infiltration d’invite ». Le glossaire retient « requête » (voir ce terme).

### intelligence artificielle

- **Anglais :** *artificial intelligence* (AI).
- **Définition :** domaine de l’informatique qui conçoit des systèmes capables de tâches associées à l’intelligence humaine, comme comprendre ou rédiger un texte.
- **Exemple :** l’organisation encadre l’usage de l’intelligence artificielle par une politique que chaque équipe doit connaître.
- **Règle :** 1.
- **Source :** GDT, fiche [« intelligence artificielle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26552508/intelligence-artificielle) (FranceTerme, 2018), consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** « IA » après la première mention.

### itération

- **Anglais :** *iteration*.
- **Définition :** nouveau passage dans la boucle de travail : vous examinez le résultat, précisez la consigne et relancez la demande.
- **Exemple :** après deux itérations, le résumé respecte la longueur demandée et cite les bonnes sources.
- **Règle :** 2.
- **Source :** GDT, fiche [« itération »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26559190/iteration), mise à jour en 2022, consultée le 10 novembre 2026. Elle vise le sens des méthodes agiles. Le programme emploie le mot au sens courant : un tour de plus dans la boucle de travail.
- **Introduit dans :** C-04.

### jeton

- **Anglais :** *token*.
- **Définition :** unité de base que traite le modèle : un mot, une partie de mot ou un signe de ponctuation.
- **Exemple :** la longueur d’un document se mesure en jetons, et chaque jeton compte dans la limite du modèle comme dans la facture.
- **Règle :** 1.
- **Source :** GDT, fiche [« jeton »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26584108/jeton), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.

### mandat

- **Anglais :** *engagement*, au sens du travail confié par un client.
- **Définition :** travail confié par un client à une équipe, avec un objectif et une durée définis.
- **Exemple :** au début du mandat, l’équipe vérifie quelles applications d’IA le client autorise.
- **Règle :** 2.
- **Source :** aucune fiche de l’OQLF pour ce sens (recherche du 10 novembre 2026). Les fiches [« lettre de mission »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/502256/lettre-de-mission) et [« mission de conseil en gestion »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/506006/mission-de-conseil-en-gestion) viennent d’un dictionnaire de comptabilité (ICCA, 2006), sans terme privilégié.
- **Introduit dans :** X-03.

### modèle

- **Anglais :** *model*.
- **Définition :** moteur de l’application : un programme entraîné sur des données, qui produit une réponse à partir d’une requête.
- **Exemple :** deux applications peuvent utiliser le même modèle et donner pourtant des résultats différents.
- **Règle :** 1.
- **Source :** GDT, fiche [« modèle d’intelligence artificielle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26574363/modele-dintelligence-artificielle), mise à jour en 2024, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.
- **Emploi :** « modèle » seul suffit en contexte.

### modèle à poids ouverts

- **Anglais :** *open-weight model*.
- **Définition :** modèle dont les paramètres sont publiés, si bien qu’on peut l’exécuter sur ses propres serveurs.
- **Exemple :** pour garder les données sur place, l’équipe évalue un modèle à poids ouverts installé sur un serveur interne.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** C-02 (sujet facultatif).

### multimodal

- **Anglais :** *multimodal*.
- **Définition :** qualifie un modèle qui traite plusieurs types de données à la fois, comme du texte et des images.
- **Exemple :** vous joignez la photo d’un tableau blanc, et le modèle multimodal en tire une liste de tâches.
- **Règle :** 1.
- **Source :** GDT, fiche [« intelligence artificielle multimodale »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26574703/intelligence-artificielle-multimodale), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-01.

### notes de mise à jour

- **Anglais :** *release notes*.
- **Définition :** document qui accompagne une nouvelle version d’un logiciel et décrit ses nouvelles fonctions, ses corrections et ses limites.
- **Exemple :** l’agent rédige les notes de mise à jour à partir des demandes de fusion acceptées, puis une personne les relit.
- **Règle :** 1.
- **Source :** GDT, fiche [« notes de mise à jour »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8871935/notes-de-mise-a-jour), mise à jour en 2001, consultée le 10 novembre 2026.
- **Introduit dans :** E-08.
- **Emploi :** toujours au pluriel. Le GDT donne aussi « notes complémentaires » et « notes techniques », mais les juge trop génériques.

### obligation de rendre compte

- **Anglais :** *accountability*.
- **Définition :** devoir de répondre d’un résultat et des moyens choisis pour l’obtenir, même quand l’IA a fait une partie du travail.
- **Exemple :** la personne qui envoie le rapport en a l’obligation de rendre compte, peu importe la façon dont il a été rédigé.
- **Règle :** 1.
- **Source :** GDT, fiche [« obligation de rendre compte »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26573352/obligation-de-rendre-compte) (FranceTerme, 2023), consultée le 10 novembre 2026.
- **Introduit dans :** C-06.
- **Emploi :** selon la fiche [« responsabilisation »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8360360/responsabilisation) (mise à jour en 2008), « responsabilité » désigne l’obligation d’agir, une autre notion. L’adjectif « responsable » reste d’usage courant.

### occasion d’affaires

- **Anglais :** *business opportunity*; l’étape *opportunity* de la carte d’un mandat.
- **Définition :** circonstance qui se présente à un moment donné, pour un temps limité, et qui permet de conclure une affaire.
- **Exemple :** la demande d’offres de services de Location Pavois est une occasion d’affaires pour votre équipe.
- **Règle :** 1.
- **Source :** GDT, fiche [« occasion d’affaires »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8369702/occasion-daffaires), mise à jour en 2010, consultée le 10 novembre 2026.
- **Introduit dans :** X-03.
- **Emploi :** première étape de la carte d’un mandat. « Opportunité » ne s’emploie pas en ce sens.

### offre de services

- **Anglais :** *proposal*.
- **Définition :** document qui décrit, pour un client potentiel, les services qu’une entreprise propose, avec les délais et les coûts.
- **Exemple :** l’offre de services de votre équipe couvre la phase 1 et reporte le paiement en ligne à une phase 2.
- **Règle :** 1.
- **Source :** GDT, fiche [« offre de service »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8377628/offre-de-service), mise à jour en 2006, consultée le 10 novembre 2026.
- **Introduit dans :** B-04 et X-03.
- **Emploi :** le GDT privilégie aussi « offre de service », au singulier. Le glossaire retient « offre de services ».

### outil

- **Anglais :** *tool*, ce que l’application laisse le modèle utiliser, comme la recherche Web.
- **Définition :** fonction que l’application laisse le modèle utiliser, comme la recherche Web, la lecture de fichiers ou l’exécution de code.
- **Exemple :** grâce à l’outil de recherche Web, l’assistant cite des pages publiées après sa date limite des connaissances.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026). La fiche [« outil d’intelligence artificielle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26574413/outil-dintelligence-artificielle) désigne une application (voir ce terme).
- **Introduit dans :** C-01.

### passation

- **Anglais :** *handoff*.
- **Définition :** transmission écrite du travail en cours à la personne ou à la session suivante : ce qui est fait et la prochaine étape.
- **Exemple :** en fin de journée, l’agent rédige une note de passation que la session du lendemain lit en premier.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** E-03.6.

### point d’approbation

- **Anglais :** *gate*, *approval gate*.
- **Définition :** étape où une personne doit approuver explicitement un résultat avant une action externe, irréversible ou lourde de conséquences.
- **Exemple :** l’agent prépare le courriel au client, mais le point d’approbation exige votre accord avant l’envoi.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour la notion (recherche du 10 novembre 2026).
- **Introduit dans :** C-06.
- **Emploi :** « point de contrôle » est réservé à la question posée au groupe avant le récapitulatif de chaque leçon.

### push

- **Forme retenue :** *push*, en italique à la première mention.
- **Définition :** envoi des commits locaux vers un dépôt distant, où l’équipe peut les voir.
- **Exemple :** vous envoyez les commits avec `git push` seulement après avoir lu le *diff*.
- **Règle :** 4, nom d’une commande de Git (`git push`).
- **Source :** aucune fiche du GDT pour le sens de la gestion de versions (recherche du 10 novembre 2026).
- **Introduit dans :** E-02.
- **Emploi :** comme verbe, écrivez « envoyer les commits », avec la commande `git push` à la première mention.

### récit utilisateur

- **Anglais :** *user story*.
- **Définition :** phrase courte qui décrit un besoin du point de vue de la personne qui utilise le produit.
- **Exemple :** « En tant que gestionnaire de comptes, je veux exporter mes factures afin de les classer par client. »
- **Règle :** 1.
- **Source :** GDT, fiche [« récit utilisateur »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26528979/recit-utilisateur), mise à jour en 2021, consultée le 10 novembre 2026.
- **Introduit dans :** P-02.
- **Emploi :** au pluriel, « des récits utilisateur ». Le GDT privilégie aussi « histoire utilisateur ». Le glossaire retient « récit utilisateur ».

### rédaction de requêtes

- **Anglais :** *prompting*.
- **Définition :** action de concevoir et d’envoyer des requêtes à un assistant ou à un agent pour qu’il accomplisse une tâche.
- **Exemple :** en atelier, vous pratiquez la rédaction de requêtes en comparant deux versions de la même demande.
- **Règle :** 1.
- **Source :** GDT, fiche [« rédaction de requêtes »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/10441153/redaction-de-requetes), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** C-04.
- **Emploi :** le GDT déconseille « rédaction de prompts » et « création de prompts ».

### rédactique

- **Anglais :** *prompt engineering*.
- **Définition :** ensemble des techniques qui servent à formuler des requêtes précises pour obtenir de meilleurs résultats.
- **Exemple :** l’équipe a réuni ses techniques de rédactique dans une page de conseils partagée.
- **Règle :** 1.
- **Source :** GDT, fiche [« rédactique »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26571214/redactique), mise à jour en 2023, consultée le 10 novembre 2026.
- **Introduit dans :** C-04.
- **Emploi :** désigne la discipline. Pour l’activité, on dit « rédaction de requêtes ».

### renseignements personnels

- **Anglais :** *personal information*.
- **Définition :** renseignements qui permettent d’identifier une personne physique, directement ou indirectement.
- **Exemple :** vous retirez les noms et les numéros de téléphone du courriel avant de le coller, car ce sont des renseignements personnels.
- **Règle :** 1.
- **Source :** GDT, fiche [« renseignement personnel »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26532706/renseignement-personnel), mise à jour en 2022, consultée le 10 novembre 2026.
- **Introduit dans :** C-07.
- **Emploi :** terme de la législation canadienne, selon le GDT. Il s’emploie surtout au pluriel.

### requête

- **Anglais :** *prompt*.
- **Définition :** texte, ou autre donnée, que vous envoyez à un assistant ou à un agent pour lui demander d’accomplir une tâche.
- **Exemple :** votre requête demande un plan en trois parties, avec une phrase par partie.
- **Règle :** 1.
- **Source :** GDT, fiche [« requête »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26571209/requete), mise à jour en 2023, consultée le 10 novembre 2026.
- **Introduit dans :** C-04.
- **Emploi :** le GDT privilégie aussi « invite ». Le glossaire retient « requête », qui forme aussi « rédaction de requêtes » et « infiltration de requête ».

### réunion de démarrage

- **Anglais :** *kickoff meeting*; l’étape *kickoff and setup* se dit « démarrage et mise en place ».
- **Définition :** réunion de travail des parties concernées qui marque le début effectif d’un projet.
- **Exemple :** à la réunion de démarrage, la directrice générale du client fixe la date du projet pilote.
- **Règle :** 1.
- **Source :** GDT, fiche [« réunion de démarrage »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26539018/reunion-de-demarrage) (FranceTerme, 2009), consultée le 10 novembre 2026. La fiche de l’OQLF [« réunion de démarrage »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17034470/reunion-de-demarrage), mise à jour en 1988, privilégie aussi ce terme en publicité.
- **Introduit dans :** X-03.

### révision humaine

- **Anglais :** *human review*.
- **Définition :** examen, par une personne compétente, d’un résultat produit par l’IA avant qu’il serve ou soit transmis.
- **Exemple :** pendant la révision humaine du contrat, vous vérifiez chaque chiffre et chaque clause, pas seulement le style.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour la révision d’un résultat produit par l’IA (recherche du 10 novembre 2026).
- **Introduit dans :** C-06.
- **Emploi :** pour le code, voir « revue de code ».

### revue de code

- **Anglais :** *code review*.
- **Définition :** examen du code écrit par une autre personne ou par un agent, pour en repérer les erreurs avant sa fusion.
- **Exemple :** la revue de code porte sur la logique et les tests, même quand le code vient d’un agent.
- **Règle :** 1.
- **Source :** GDT, fiche [« revue de code »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529106/revue-de-code), mise à jour en 2014, consultée le 10 novembre 2026.
- **Introduit dans :** E-05.
- **Emploi :** le GDT privilégie aussi « révision de code » et « vérification de code ». Le glossaire retient « revue de code ».

### secret

- **Anglais :** *secret*, comme une clé d’API ou un mot de passe.
- **Définition :** information confidentielle qui donne accès à un système, comme une clé d’API ou un mot de passe.
- **Exemple :** le fichier d’instructions interdit à l’agent de lire le dossier où sont rangés les secrets.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** E-03.4.

### skill

- **Forme retenue :** *skill*, en italique à la première mention.
- **Définition :** ensemble d’instructions et de fichiers qu’un agent charge seulement quand une tâche en a besoin.
- **Exemple :** le *skill* de vérification du français contient les règles typographiques que l’agent applique avant de remettre un texte.
- **Règle :** 4, nom d’une fonction de produit.
- **Source :** sans objet (règle 4).
- **Introduit dans :** E-03.5.

### sous-agent

- **Anglais :** *sub-agent*.
- **Définition :** agent lancé par un autre agent pour accomplir une sous-tâche dans son propre contexte, puis lui rendre le résultat.
- **Exemple :** l’agent principal confie la recherche de sources à un sous-agent et ne garde que son résumé.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour ce sens (recherche du 10 novembre 2026).
- **Introduit dans :** E-09.

### spécification

- **Anglais :** *specification*, *spec*.
- **Définition :** document qui décrit précisément ce qu’un produit ou un logiciel doit faire et les exigences qu’il doit respecter.
- **Exemple :** l’agent travaille à partir de la spécification, et chaque critère d’acceptation devient un test.
- **Règle :** 1.
- **Source :** GDT, fiche [« spécification logicielle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/3291766/specification-logicielle), mise à jour en 2021, consultée le 10 novembre 2026.
- **Introduit dans :** E-04.
- **Emploi :** pas d’abréviation.

### structuration contextuelle

- **Anglais :** *context engineering*.
- **Définition :** technique qui consiste à choisir, organiser et hiérarchiser l’information placée dans la fenêtre de contexte du modèle.
- **Exemple :** par structuration contextuelle, vous ne joignez que les trois fichiers utiles au lieu du dépôt entier.
- **Règle :** 1.
- **Source :** GDT, fiche [« structuration contextuelle »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26584295/structuration-contextuelle), mise à jour en 2025, consultée le 10 novembre 2026.
- **Introduit dans :** E-04.

### synthèse de découverte

- **Anglais :** *discovery brief*.
- **Définition :** document qui résume ce que l’équipe a appris à l’étape de la découverte : les besoins, les contraintes, les contradictions et les questions ouvertes.
- **Exemple :** chaque récit utilisateur de l’atelier renvoie à un besoin de la synthèse de découverte.
- **Règle :** 2.
- **Source :** aucune fiche du GDT pour cette notion ni pour l’étape *discovery* (recherche du 10 novembre 2026).
- **Introduit dans :** P-02.
- **Emploi :** l’étape *discovery* se dit « découverte ». À distinguer de l’« énoncé de projet », qui présente le projet lui-même.

## Termes écartés

| Terme écarté | Employer | Raison |
|---|---|---|
| *prompt*, hors première mention | requête | Terme privilégié du GDT. |
| invite | requête | Un seul terme. Le GDT privilégie les deux. |
| rédaction de prompts, création de prompts | rédaction de requêtes | Déconseillés par le GDT. |
| injection de requête | infiltration de requête | Terme privilégié du GDT. |
| *user story*, hors première mention | récit utilisateur | Déconseillé par le GDT. |
| histoire utilisateur | récit utilisateur | Un seul terme. Le GDT privilégie les deux. |
| *brief*, hors première mention | consigne | Règle 2. |
| mandat, pour *brief* | consigne | « Mandat » rend *engagement* (voir ce terme). |
| point de contrôle, pour *gate* | point d’approbation | Réservé à la question posée au groupe avant le récapitulatif. |
| point d’ancrage, pour *hook* | *hook* | Au GDT, « point d’ancrage Web » désigne un *webhook* (fiche [« lien de rappel HTTP »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26558230/lien-de-rappel-http)). |
| ajustement fin | *fine-tuning* | Aucune fiche du GDT. |
| *token*, hors première mention | jeton | Terme privilégié du GDT. |
| LLM, GML, MLGT, après la première mention | grand modèle de langage, ou « modèle » | Un seul terme, sans sigle. |
| IAG | IA générative | Un seul terme. |
| IA agentique | IA agentive | Un seul terme. Le GDT privilégie les deux. |
| GAR | RAG | Un seul sigle. Le GDT admet « RAG » dans ce domaine. |
| longueur de contexte | fenêtre de contexte | Un seul terme. Le GDT privilégie les deux. |
| outil d’intelligence artificielle, outil d’IA | application | « Outil » désigne ce que l’application laisse le modèle utiliser (C-01). |
| flux de travail | flux de travaux | Forme du GDT. |
| demande de tirage | demande de fusion | Terme privilégié du GDT. |
| *pull request*, hors première mention | demande de fusion | Terme privilégié du GDT. |
| référentiel, pour *repository* | dépôt | Le GDT nomme cette notion « dépôt de code source ». |
| classification des données | classification de sécurité | Terme privilégié du GDT. |
| donnée personnelle, DCP | renseignements personnels | Terme de la législation canadienne, selon le GDT. |
| espace de test | bac à sable | Un seul terme. Le GDT privilégie les deux. |
| révision de code, vérification de code | revue de code | Un seul terme. Le GDT privilégie aussi ces formes. |
| permission, en prose française | autorisation | Les noms de paramètres restent en anglais. |
| compétence, pour *skill* | *skill* | Nom d’une fonction de produit (règle 4). |
| spec | spécification | Pas d’abréviation. |
| commiter | *commit*, comme verbe : « créer un commit » | Emprunt que le GDT déconseille. |
| responsabilité, pour *accountability* | obligation de rendre compte | Au GDT, « responsabilité » désigne l’obligation d’agir. |
| imputabilité | obligation de rendre compte | Le GDT déconseille ce sens. |
| redevabilité | obligation de rendre compte | Le GDT déconseille ce sens. |
| responsabilisation | obligation de rendre compte | Un seul terme. |
| fiche, pour *handout* | document d’accompagnement | Terme privilégié du GDT. « Fiche » désigne une fiche de module ou une fiche du GDT. |
| document d’appui | document d’accompagnement | Un seul terme. Le GDT privilégie les deux. |
| mission, pour *engagement* | mandat | Un seul terme. |
| appel d’offres, pour *request for proposals* | demande d’offres de services | Au GDT, « appel d’offres » rend *call for tenders*. |
| appel de propositions | demande d’offres de services | Au GDT, ce terme rend *call for proposals*. |
| demande de propositions | demande d’offres de services | Un seul terme. |
| proposition, pour *proposal* | offre de services | Terme privilégié du GDT. |
| opportunité, pour *opportunity* | occasion d’affaires | Emploi déconseillé par l’OQLF en ce sens. |
| *kickoff*, réunion de lancement | réunion de démarrage | Terme recommandé par FranceTerme et privilégié par l’OQLF. |
| notes de version, *release notes* hors première mention | notes de mise à jour | Terme privilégié du GDT. |
| note de passation, pour *handover document* | document de passation | La note de passation transmet le travail d’une session à la suivante. |

## Index anglais-français

| Anglais | Français |
|---|---|
| acceptance criteria | critères d’acceptation |
| accountability | obligation de rendre compte |
| agent | agent |
| agentic AI | IA agentive |
| allow | autoriser |
| application | application |
| approval gate | point d’approbation |
| artificial intelligence (AI) | intelligence artificielle |
| ask | demander |
| assistant | assistant |
| branch | branche |
| brief | consigne |
| business opportunity | occasion d’affaires |
| code review | revue de code |
| commit | *commit* (terme anglais conservé) |
| connector | connecteur |
| context engineering | structuration contextuelle |
| context window | fenêtre de contexte |
| data classification | classification de sécurité |
| deny | refuser |
| diff | *diff* (terme anglais conservé) |
| discovery brief | synthèse de découverte |
| engagement | mandat |
| fine-tuning | *fine-tuning* (terme anglais conservé) |
| gate | point d’approbation |
| generative AI | IA générative |
| hallucination | hallucination |
| handoff | passation |
| handout | document d’accompagnement |
| handover document | document de passation |
| hook | *hook* (terme anglais conservé) |
| human review | révision humaine |
| instruction file | fichier d’instructions |
| iteration | itération |
| kickoff meeting | réunion de démarrage |
| knowledge cutoff | date limite des connaissances |
| large language model (LLM) | grand modèle de langage |
| model | modèle |
| multimodal | multimodal |
| open-weight model | modèle à poids ouverts |
| opportunity | occasion d’affaires |
| permission | autorisation |
| personal information | renseignements personnels |
| project brief | énoncé de projet |
| prompt | requête |
| prompt engineering | rédactique |
| prompt injection | infiltration de requête |
| prompting | rédaction de requêtes |
| proposal | offre de services |
| pull request (PR) | demande de fusion |
| push | *push* (terme anglais conservé) |
| RAG | génération augmentée par récupération |
| release notes | notes de mise à jour |
| repo | dépôt |
| repository | dépôt |
| request for proposals (RFP) | demande d’offres de services |
| retrieval-augmented generation | génération augmentée par récupération |
| sandbox | bac à sable |
| secret | secret |
| skill | *skill* (terme anglais conservé) |
| spec | spécification |
| specification | spécification |
| sub-agent | sous-agent |
| token | jeton |
| tool | outil |
| training | entraînement |
| user story | récit utilisateur |
| workflow | flux de travaux |
