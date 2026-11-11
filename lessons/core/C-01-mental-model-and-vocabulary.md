---
id: C-01
title: "Une image juste et les bons mots"
card: .ai/project/spec/curriculum/core/C-01-mental-model-and-vocabulary.md
track: core
minutes: 15
status: review
last_verified: "2026-11-11"
native_review: pending
glossary:
  - intelligence artificielle
  - IA générative
  - grand modèle de langage
  - modèle
  - entraînement
  - hallucination
  - application
  - assistant
  - outil
  - agent
  - date limite des connaissances
  - fenêtre de contexte
  - jeton
  - multimodal
  - mandat
  - demande d’offres de services
  - offre de services
  - réunion de démarrage
---

# Une image juste et les bons mots

On se sert mal d’un assistant virtuel qu’on se représente mal. La plupart des gens qui débutent le traitent comme un moteur de recherche, une base de données ou un collègue qui connaît déjà le projet. Une seule image juste évite la plupart des erreurs du début.

<!-- slide: section -->
### Une image juste et les bons mots

<details><summary>Notes de présentation</summary>

[1 min] Bienvenue dans le premier module. Avant d’apprendre à travailler avec un assistant, il faut savoir ce que c’est. La plupart des erreurs du début viennent d’une image fausse. Certaines personnes le prennent pour un moteur de recherche. D’autres, pour une base de données. D’autres encore, pour un collègue qui connaît déjà le projet. Aucune de ces images n’est juste. Dans les prochaines minutes, vous allez les remplacer par une seule image, plus juste. Vous allez aussi apprendre quatre mots que tout le monde confond. Nos exemples viennent d’un mandat fictif. Votre équipe construit un portail de réservation pour Location Pavois, une entreprise qui loue du matériel pour les événements.

</details>
<!-- /slide -->

## Objectifs

À la fin de ce module, vous serez en mesure :

- de dire en une phrase ce que fait un modèle de langage;
- de distinguer un modèle, une application, un outil et un agent;
- d’expliquer pourquoi une réponse bien écrite peut être fausse.

## Déroulement

| Étape | Minutes | Diapositives |
|---|---|---|
| Ouverture | 1 | 1 |
| Une suite plausible | 3 | 2 et 3 |
| Quatre mots | 2 | 4 et 5 |
| Ce que l’assistant sait | 3 | 6 et 7 |
| Point de contrôle | 3 | 8 |
| Pratique | 2 | 9 |
| Récapitulatif | 1 | 10 |
| **Total** | 15 | |

Si vous êtes en retard, ou dans la version de 90 minutes de la séance : la pratique ne porte que sur trois cartes, et le point de contrôle se limite à deux réponses.

## Une suite plausible

Une personne pose une question à un assistant, sans lui donner aucun document : quand le portail de réservation de Location Pavois ouvrira-t-il? L’assistant répond avec une date précise et une raison qui sonne juste. Posée une seconde fois, la même question reçoit une autre date. Aucune des deux n’a jamais été fixée.

<!-- slide: example -->
### Deux essais, deux dates inventées

> **Vous :** Quand le portail de réservation de Location Pavois ouvrira-t-il?
>
> **Premier essai :** Le portail ouvrira le 1er avril, juste avant la haute saison.
>
> **Second essai :** Le lancement est prévu pour la mi-juin, dans les trois succursales.

Aucun document fourni. Aucune de ces dates n’existe.

<details><summary>Notes de présentation</summary>

[1,5 min] Voici une question posée à un assistant, sans aucun document. [Montrez la question.] Quelqu’un demande quand le portail de Location Pavois ouvrira. Regardez le premier essai. Il donne une date précise, le 1er avril, et une raison qui sonne juste. [Pause] Regardez maintenant le second essai. C’est la même question, posée quelques secondes plus tard. Cette fois, on parle de la mi-juin, dans les trois succursales. Les deux réponses sont bien écrites. Les deux ont l’air sûres d’elles. Pourtant, personne n’a jamais fixé ces dates. Je vous pose une question, sans attendre de réponse : laquelle auriez-vous crue? [Pause] Sans doute celle que vous avez lue en premier. C’est exactement le piège. L’assistant n’a pas menti. Il a fait ce qu’il fait toujours. Voyons ce que c’est.

</details>
<!-- /slide -->

L’intelligence artificielle générative (IA générative, *generative AI*) produit du contenu nouveau à partir d’une requête. Au cœur d’un assistant se trouve un grand modèle de langage (LLM, *large language model*), qu’on appelle ensuite simplement le modèle. Pendant son entraînement (*training*), il a traité une très grande quantité de texte. Il produit la suite la plus plausible de ce qu’on lui donne. Une suite plausible est souvent vraie, mais pas toujours. Un contenu faux présenté comme un fait s’appelle une hallucination. Une réponse fausse a le même ton qu’une réponse juste : l’assurance du texte ne dit rien de sa vérité. Enfin, la même question peut recevoir deux réponses différentes, et c’est un comportement normal.

<!-- slide: concept -->
### Le modèle produit la suite la plus plausible

- Entraîné sur une très grande quantité de texte
- Plausible : souvent vrai, parfois faux
- Le ton assuré ne prouve rien
- Deux essais, parfois deux réponses

<details><summary>Notes de présentation</summary>

[1,5 min] Un grand modèle de langage a été entraîné sur une très grande quantité de texte. À partir de ce que vous lui donnez, il produit la suite la plus plausible. Une suite plausible est souvent vraie. Elle ne l’est pas toujours. Quand elle est fausse, on parle d’hallucination. [Pause] Retenez surtout ceci : une réponse fausse a exactement le même ton qu’une réponse juste. Autre point : deux essais peuvent donner deux réponses. C’est normal, ce n’est pas une panne. Une image peut vous aider. Pensez à une personne très cultivée, nouvelle dans l’équipe, qui ne se souvient de rien d’hier. Elle a énormément lu, mais elle ne connaît pas votre projet. Cette image a ses limites. Une personne nouvelle vous dirait qu’elle ne sait pas. Le modèle, lui, ne le dit pas toujours. Et certaines applications offrent une fonction de mémoire, qui change un peu les choses.

</details>
<!-- /slide -->

## Quatre mots

Isabelle, responsable du développement des affaires, reçoit la demande d’offres de services de Location Pavois. Elle ouvre l’application de clavardage approuvée par son organisation, joint le fichier et demande quelles exigences donneront le plus de travail. L’application lit d’abord le fichier joint, puis la réponse arrive.

<!-- slide: example -->
### Une seule question, quatre choses au travail

> **Isabelle :** Voici la demande d’offres de services de Location Pavois. Quelles exigences demanderont le plus de travail?
>
> *Lecture du fichier joint…*
>
> **Assistant :** La demande énumère six exigences. Le paiement en ligne et le lien avec le logiciel comptable demanderont le plus de travail.

<details><summary>Notes de présentation</summary>

[1 min] Voici Isabelle, responsable du développement des affaires. Elle a reçu la demande d’offres de services de Location Pavois. Elle ouvre l’application de clavardage de son organisation et joint le fichier. Elle demande quelles exigences donneront le plus de travail. [Montrez la ligne en italique.] Regardez cette ligne : l’application lit le fichier joint. Ensuite seulement, la réponse arrive. Dans cette scène, plusieurs choses différentes travaillent ensemble. Pourtant, au quotidien, on les appelle toutes « l’IA ». Démêlons-les.

</details>
<!-- /slide -->

Quatre mots désignent quatre choses distinctes. Le modèle (*model*) est le moteur qui produit la réponse. L’application est le produit construit autour de lui, comme une application de clavardage ou une extension de l’éditeur de code. Un outil (*tool*) est une fonction que l’application laisse le modèle utiliser : la recherche sur le Web, la lecture de fichiers ou l’exécution de code. Un agent est un modèle qui travaille en boucle avec des outils pour atteindre un objectif : il planifie, agit, vérifie et recommence. Un assistant, enfin, est une application d’IA avec laquelle vous conversez en langage courant.

<!-- slide: concept -->
### Quatre mots pour quatre choses distinctes

- Modèle : le moteur
- Application : le produit autour du modèle
- Outil : ce que l’application lui laisse utiliser
- Agent : un modèle qui travaille en boucle avec des outils

<details><summary>Notes de présentation</summary>

[1 min] Le modèle, c’est le moteur. C’est lui qui produit le texte. L’application, c’est le produit construit autour : la fenêtre de clavardage d’Isabelle, ou une extension dans un éditeur de code. Un outil, c’est une fonction que l’application prête au modèle : lire un fichier, chercher sur le Web, exécuter du code. Un agent, enfin, c’est un modèle qui travaille en boucle avec des outils pour atteindre un objectif. Il planifie, agit, vérifie et recommence. Chez Isabelle, il n’y avait pas d’agent : une seule question, une seule réponse. Un agent, ce serait plutôt l’assistant de Julien, le développeur de l’équipe, qui lit le code, le modifie, lance les tests et recommence jusqu’à ce qu’ils passent. Un même modèle peut se trouver dans plusieurs applications. Quand quelqu’un dit « l’IA s’est trompée », demandez-vous lequel des quatre est en cause.

</details>
<!-- /slide -->

## Ce que l’assistant sait

Marc-André, chargé de projet, pose la même question qu’au début : quand le portail ouvrira-t-il? Cette fois, il joint deux documents : l’offre de services et le compte rendu de la réunion de démarrage. La réponse est juste. Le modèle et la question n’ont pas changé, seulement ce que l’assistant avait sous les yeux.

<!-- slide: example -->
### Avec les bons documents, la réponse change

> **Marc-André :** *Deux pièces jointes : l’offre de services, le compte rendu de la réunion de démarrage.* Quand le portail ouvrira-t-il?
>
> **Assistant :** Le projet pilote ouvre à la succursale Est le 15 mai. Les succursales Nord et Sud suivent en octobre.

<details><summary>Notes de présentation</summary>

[1,5 min] Revenons au portail. Cette fois, Marc-André, le chargé de projet, joint deux documents avant de poser sa question. Le premier est l’offre de services. Le second est le compte rendu de la réunion de démarrage. [Montrez les deux pièces jointes.] Il pose la même question qu’au début. La réponse est maintenant juste. Le projet pilote ouvre à la succursale Est le 15 mai, et les deux autres succursales suivent en octobre. Qu’est-ce qui a changé depuis tout à l’heure? [Pause] Le modèle et la question sont restés les mêmes. Seuls les documents sous les yeux de l’assistant ont changé. Ces documents auraient pu être une photo, un enregistrement ou une capture d’écran. L’assistant lit aussi des images et des fichiers, parfois du son. On dit qu’il est multimodal.

</details>
<!-- /slide -->

L’assistant sait trois choses. Il connaît d’abord ce que son modèle a appris pendant l’entraînement, jusqu’à une date limite des connaissances (*knowledge cutoff*). Il connaît ensuite le contenu de la conversation, et enfin ce que ses outils vont chercher. De votre projet, il ne sait rien, sauf ce que vous lui montrez. La conversation tient dans la fenêtre de contexte (*context window*), sa mémoire de travail : elle est limitée, et tout ce que le modèle prend en compte doit y tenir. Cette limite se compte en jetons (*tokens*), des morceaux de mots, qui servent aussi à calculer le coût. Ce que vous lui montrez n’est plus seulement du texte : un modèle multimodal lit aussi des images, des fichiers, du son ou un écran.

<!-- slide: concept -->
### L’assistant ne sait que trois choses

- Son entraînement, jusqu’à une date limite
- Le contenu de la conversation
- Ce que ses outils vont chercher

<details><summary>Notes de présentation</summary>

[1,5 min] L’assistant sait trois choses, pas plus. D’abord, ce que son modèle a appris pendant l’entraînement, jusqu’à une date limite. Après cette date, il ignore tout. Ensuite, ce qui se trouve dans la conversation. Enfin, ce que ses outils vont chercher pour lui. De votre projet, il ne sait rien, sauf ce que vous lui montrez. Le portail de Location Pavois, par exemple, n’apparaît dans aucune donnée d’entraînement. Ses décisions sont écrites dans les documents de l’équipe, et nulle part ailleurs. Une date limite plus récente n’y changerait rien. [Pause] La conversation tient dans ce qu’on appelle la fenêtre de contexte. C’est sa mémoire de travail. Elle est grande, mais pas infinie, et tout ce que le modèle prend en compte doit y tenir. Dans une très longue conversation, les premiers échanges peuvent finir par en sortir. On la mesure en jetons, des morceaux de mots. Les jetons servent aussi à calculer le coût. Vous vous demandez peut-être quelle est la date limite de notre modèle. Je ne sais pas, je vais vérifier. Je vous enverrai la réponse par écrit. [Notez la question dans la liste des questions en attente.]

</details>
<!-- /slide -->

## Point de contrôle

Nommez une chose que l’assistant ne peut pas savoir de votre projet actuel, sauf si vous la lui donnez.

<!-- slide: checkpoint -->
### Nommez une chose que l’assistant ne peut pas savoir de votre projet actuel, sauf si vous la lui donnez

<details><summary>Notes de présentation</summary>

[3 min] Transition : « Vous savez maintenant ce que l’assistant sait, et surtout ce qu’il ne sait pas. Pensez à votre propre travail. »

[Lisez la question.] [Pause : comptez lentement jusqu’à sept avant de parler.] [Attendez deux ou trois réponses.] [Si personne ne répond, reformulez une fois : « Que devrait vous demander une personne nouvelle dans l’équipe, le premier jour? » Puis proposez une réponse, par exemple une décision prise à la dernière réunion, et demandez si la salle est d’accord.]

Résumé : « Les décisions, les personnes et les contraintes de votre projet, l’assistant les ignore tant que vous ne les lui donnez pas. »

</details>
<!-- /slide -->

## Pratique

Classez six cartes dans l’une des quatre catégories : modèle, application, outil ou agent. Durée : 2 minutes en séance, à voix haute avec le groupe; seul ou seule avec le manuel.

Les six cartes :

1. une application de clavardage;
2. une extension de l’éditeur de code;
3. le nom d’un modèle;
4. la recherche sur le Web;
5. un agent de programmation;
6. le téléversement d’un fichier.

Résultat attendu : application, application, modèle, outil, agent, outil.

<!-- slide: exercise -->
### Classez chaque carte : modèle, application, outil ou agent

1. Écoutez la carte lue (0,5 min)
2. Dites sa catégorie à voix haute (1 min)
3. Comparez avec le corrigé (0,5 min)

<details><summary>Notes de présentation</summary>

[2 min] Passons à une courte pratique, en groupe. Je lis six cartes. Pour chacune, dites tout haut : modèle, application, outil ou agent. [Lisez les cartes une à une. Laissez la salle répondre avant de confirmer.] [Corrigé : application de clavardage, application; extension de l’éditeur de code, application; nom d’un modèle, modèle; recherche sur le Web, outil; agent de programmation, agent; téléversement d’un fichier, outil.] [Si vous êtes en retard : ne lisez que les cartes 1, 3 et 5.]

</details>
<!-- /slide -->

## Récapitulatif

Le modèle produit la suite la plus plausible de ce qu’on lui donne, et son ton ne prouve rien : les deux dates inventées du début en sont la preuve. Modèle, application, outil et agent désignent quatre choses distinctes. Enfin, l’assistant ne sait de votre projet que ce que vous lui montrez : les deux documents de Marc-André ont tout changé.

<!-- slide: recap -->
### Ce que vous retenez de ce module

- Une suite plausible n’est pas une vérité
- Modèle, application, outil, agent : quatre choses distinctes
- Il ne sait que ce que vous lui montrez

<details><summary>Notes de présentation</summary>

[1 min] Avant de passer à la suite, à vous. Qu’est-ce que vous retenez de ces quelques minutes? [Attendez deux ou trois réponses, puis montrez les énoncés.] D’abord, le modèle produit une suite plausible, et son ton ne prouve rien. Pensez aux deux dates inventées. Ensuite, quatre mots, quatre choses : le moteur, le produit autour, ce qu’il utilise et le travail en boucle. Enfin, l’assistant ne sait de votre projet que ce que vous lui montrez. Ce sont les deux documents de Marc-André qui ont tout changé. Dans le prochain module, nous verrons où l’assistant aide et où il échoue.

</details>
<!-- /slide -->

## Pour aller plus loin

Ces sujets ne sont pas présentés en séance. Ils servent de référence.

- L’effort de réflexion est un réglage : un modèle peut consacrer plus ou moins d’effort à une tâche. Plus d’effort n’est pas toujours mieux.
- Utiliser un modèle ne l’entraîne pas. L’emploi de vos données pour l’entraînement dépend du produit, de l’abonnement et des réglages (voir le module sur les données et l’usage responsable).
- Avec la recherche ou la génération augmentée par récupération (RAG), l’assistant va chercher des sources avant de répondre. Une réponse appuyée sur des sources se vérifie; une réponse tirée de sa mémoire, non.
- Un même modèle se comporte différemment selon le produit. Le comportement dépend de l’application, de l’abonnement et des réglages.

Sujets facultatifs :

- les plongements et la recherche vectorielle;
- le *fine-tuning*, la rédaction de requêtes et la récupération, comparés;
- les modèles à poids ouverts et les modèles installés localement;
- les tests de performance publiés, et pourquoi ils prédisent mal vos propres résultats;
- l’échantillonnage et la température.

Le sens de chaque terme est dans le [glossaire](../../resources/R-02-glossary.md). Les lectures complémentaires (R-01) en donnent les sources, section « Fondements ».

## À revérifier avant chaque prestation

- Le nom de l’application approuvée et de son modèle, montrés pendant la présentation : à vérifier dans l’application la semaine de la prestation. Dernière vérification : à faire.
- Ce que fait la fonction de mémoire de l’application approuvée, citée dans la limite de l’image : à vérifier dans ses réglages. Dernière vérification : à faire.
- La date limite des connaissances du modèle approuvé, si la salle la demande : à vérifier dans la documentation du fournisseur. Dernière vérification : à faire.
