---
id: C-04
title: "La boucle de travail"
card: .ai/project/spec/curriculum/core/C-04-working-loop-and-prompting.md
track: core
minutes: 13
status: review
last_verified: "2026-11-11"
native_review: done 2026-11-11
glossary:
  - assistant
  - requête
  - rédaction de requêtes
  - consigne
  - itération
  - offre de services
  - réunion de démarrage
  - critères d’acceptation
  - skill
---

# La boucle de travail

Une seule requête produit rarement un résultat fini. Ce qui y mène, c’est une boucle : donner une consigne, examiner le résultat, le corriger, le vérifier. C’est la même boucle pour un courriel, une spécification ou une modification de code, et tout le programme repose sur elle.

<!-- slide: section -->
### La boucle de travail

<details><summary>Notes de présentation</summary>

[0,5 min] Vous savez maintenant quoi confier à un assistant. Voyons comment le faire. Je vais vous montrer une seule tâche, du début à la fin, avec ses ratés. Regardez surtout ce qui change entre la première réponse et la dernière. Ce qui change tout, c’est ce que la personne donne à l’assistant, et ce qu’elle vérifie.

</details>
<!-- /slide -->

## Objectifs

À la fin de ce module, vous serez en mesure :

- de mener la boucle, d’une demande approximative jusqu’à un résultat vérifié;
- de rédiger une consigne qui précise le but, le contexte, les contraintes et le résultat attendu;
- de corriger un résultat en nommant le défaut, au lieu de demander « mieux ».

## Déroulement

| Étape | Minutes | Diapositives |
|---|---|---|
| Ouverture | 0,5 | 1 |
| Huit étapes | 1,5 | 2 |
| Une première requête | 1,5 | 3 |
| Point de contrôle | 3 | 4 |
| Une consigne complète | 3 | 5 et 6 |
| Vérifier et corriger | 3 | 7 et 8 |
| Récapitulatif | 0,5 | 9 |
| **Total** | 13 | |

La pratique de ce module est l’atelier de la séance, qui applique la même boucle à du matériel propre à chaque rôle.

Si vous êtes en retard : ne faites pas la démonstration en direct. Montrez seulement les diapositives 3, 5 et 7, qui contiennent la version préparée.

## Huit étapes

Le 16 mars, après la réunion de démarrage de Location Pavois, Marc-André, chargé de projet, doit préparer un résumé du projet d’une page pour le personnel des succursales. Il va s’y prendre en plusieurs tours avec l’assistant, et ce résumé nous suit pendant toute la séance.

<!-- slide: concept -->
### Huit étapes, de la demande au résultat vérifié

1. Cadrer, donner le contexte
2. Demander, examiner
3. Itérer, vérifier
4. Approuver, conserver

<details><summary>Notes de présentation</summary>

[1,5 min] Voici la tâche. Le 16 mars, Marc-André sort de la réunion de démarrage avec le client. Il doit écrire un résumé d’une page pour le personnel des trois succursales. Pour y arriver, il suit une boucle en huit étapes. [Montrez la première ligne.] D’abord, cadrer : ce qu’il veut obtenir, et pour qui. Puis donner le contexte : les documents utiles. [Montrez la deuxième ligne.] Ensuite, demander, puis examiner la réponse. [Montrez la troisième ligne.] Si elle ne convient pas, itérer : un tour de plus, avec une consigne plus précise. Puis vérifier chaque fait contre les documents. [Montrez la quatrième ligne.] Enfin, une personne approuve le résultat, et Marc-André conserve ce qui a marché. [Pause] Cette boucle vaut pour un courriel, une spécification ou du code. Le piège, c’est de s’arrêter à la quatrième étape : lire la réponse, puis l’envoyer. Les quatre dernières étapes font la différence entre un texte plausible et un texte juste. Regardez maintenant ce qui se passe quand on saute les deux premières étapes.

</details>
<!-- /slide -->

La boucle de travail compte huit étapes : cadrer, donner le contexte, demander, examiner, itérer, vérifier, approuver et conserver. Cadrer, c’est savoir ce qu’on veut et pour qui. Donner le contexte, c’est fournir les documents dont l’assistant a besoin. Examiner, c’est lire la réponse d’un œil critique. Une itération (*iteration*) est un tour de plus dans la boucle, avec une consigne plus précise. Vérifier, c’est comparer chaque fait aux documents. Approuver revient à une personne. Conserver, c’est garder la consigne qui a fonctionné pour la prochaine fois.

## Une première requête

Marc-André ouvre l’assistant et écrit une requête (*prompt*) d’une ligne : « Écris un résumé du projet pour le personnel. » Il ne joint aucun document. La réponse arrive vite, bien écrite et enthousiaste. Elle annonce que les clients pourront payer leur acompte en ligne. Or l’offre de services exclut le paiement en ligne de la phase 1.

<!-- slide: example -->
### Une ligne de requête, une réponse inventée

> **Marc-André :** Écris un résumé du projet pour le personnel.
>
> **Assistant :** Bonne nouvelle! Notre nouveau portail transformera votre façon de travailler. Les clients pourront réserver en ligne, payer leur acompte directement sur le site et suivre leur commande en temps réel…

Le paiement en ligne est exclu de la phase 1.

<details><summary>Notes de présentation</summary>

[1,5 min] [Lancez l’enregistrement de la démonstration jusqu’à la première réponse, ou tapez la requête en direct. Si la réponse en direct diffère, revenez à cette diapositive : c’est la version préparée.] Voici la requête de Marc-André. Une seule ligne, et aucun document. Regardez la réponse. Elle est rapide, bien écrite, pleine d’enthousiasme. [Montrez « payer leur acompte ».] Lisez ce passage. Les clients pourraient payer leur acompte en ligne. Or l’offre de services exclut le paiement en ligne. Et personne n’a promis de suivre une commande en temps réel. [Pause] L’assistant n’a rien fait de mal. Il a produit la suite la plus plausible d’une requête vague. Sans document, il a rempli les trous avec ce que font la plupart des portails. Remarquez aussi le ton : « Bonne nouvelle! », « transformera votre façon de travailler ». C’est le ton de n’importe quelle annonce. Rien dans ce texte ne parle de Location Pavois en particulier : ni la succursale Est, ni le projet pilote, ni les dates. Un texte qui pourrait décrire n’importe quel projet est un signal d’alarme. Si Marc-André envoie ce texte, le personnel annoncera aux clients une fonction qui n’existe pas.

</details>
<!-- /slide -->

Une requête vague laisse l’assistant deviner. Il comble alors les trous avec ce qui est le plus courant ailleurs, et le résultat sonne juste sans l’être. Le défaut vient de ce qu’on lui a donné.

## Point de contrôle

Cette requête est faible. Que lui manque-t-il?

> Écris un résumé du projet pour le personnel.

Réponses attendues, parmi d’autres : les documents sur lesquels s’appuyer, le public précis, le but du texte, la longueur, ce qui est exclu du projet et les dates.

<!-- slide: checkpoint -->
### Cette requête est faible. Que lui manque-t-il?

« Écris un résumé du projet pour le personnel. »

<details><summary>Notes de présentation</summary>

[3 min] Transition : « Avant que je vous montre la suite, à vous de jouer. »

[Lisez la question.] [Pause : comptez lentement jusqu’à sept avant de parler.] [Recueillez trois réponses avant de montrer la suite. Notez-les au tableau ou dans le clavardage.] [Si personne ne répond, reformulez une fois : « Que devrait savoir une personne nouvelle dans l’équipe avant d’écrire ce texte? » Puis proposez une réponse, par exemple les documents de la réunion, et demandez si la salle est d’accord.]

Résumé : « Il lui manque surtout ce que Marc-André sait déjà : les documents, le public et le but. Voyons s’il les lui donne. »

</details>
<!-- /slide -->

## Une consigne complète

Marc-André recommence avec une consigne (*brief*) complète. Il joint l’offre de services et le compte rendu de la réunion de démarrage. Il précise le public, le but, la longueur, et il demande à l’assistant de poser ses questions avant d’écrire :

> Je joins deux documents : l’offre de services acceptée par Location Pavois et le compte rendu de la réunion de démarrage du 16 mars. Rédige un résumé du projet pour le personnel des comptoirs des trois succursales. Ces personnes n’ont pas de connaissances techniques. Le but : leur dire ce qui change pour elles, et quand. Une page au plus, en phrases courtes. Appuie-toi seulement sur les deux documents. Si une information manque, ou si les documents se contredisent, pose-moi tes questions avant d’écrire.

<!-- slide: example -->
### La même tâche, avec une vraie consigne

> **Marc-André :** *Deux pièces jointes : l’offre de services, le compte rendu de la réunion de démarrage.*
>
> Rédige un résumé pour le personnel des comptoirs, sans connaissances techniques. Le but : ce qui change pour le personnel, et quand. Une page au plus. Appuie-toi seulement sur ces documents. S’il manque une information, pose-moi tes questions avant d’écrire.

<details><summary>Notes de présentation</summary>

[1,5 min] [Montrez la suite de l’enregistrement, ou tapez la consigne en direct.] Voici la deuxième tentative de Marc-André. Regardez d’abord la première ligne : deux documents joints, l’offre de services et le compte rendu de la réunion. L’assistant n’a plus à deviner le projet : il peut le lire. Ensuite, Marc-André dit pour qui il écrit : le personnel des comptoirs, sans connaissances techniques. Il dit pourquoi : ce qui change pour le personnel, et quand. Il fixe la longueur. [Montrez la dernière phrase.] Et il ajoute une chose que beaucoup oublient : s’il manque une information, l’assistant doit poser ses questions au lieu de deviner. [Si l’assistant pose des questions en direct, répondez à partir du compte rendu.] [Pause] Remarquez qu’aucun mot magique n’a été ajouté. Marc-André n’a pas écrit « tu es spécialiste en communication ». Il n’a pas mis de majuscules. Il n’a pas supplié l’assistant de faire attention. La consigne est simplement plus complète.

</details>
<!-- /slide -->

Donnez la consigne comme à une personne compétente, mais nouvelle dans l’équipe. Elle a besoin du but et de la raison qui le justifie, du public visé, des documents de départ, des contraintes, du format et de ce à quoi ressemble un résultat terminé. Quand la réponse doit s’appuyer sur des faits, fournissez les documents au lieu de compter sur la mémoire de l’assistant. Enfin, demandez-lui de poser ses questions quand une information manque, au lieu de deviner.

<!-- slide: concept -->
### Une consigne comme pour une personne nouvelle dans l’équipe

- Le but, et pourquoi il compte
- Le public, les documents, les contraintes
- Le format, et le résultat attendu
- « Pose tes questions avant d’écrire »

<details><summary>Notes de présentation</summary>

[1,5 min] Pensez à une personne compétente qui arrive aujourd’hui dans l’équipe. Elle ne connaît ni le client, ni le projet. Que lui diriez-vous? D’abord, le but, et pourquoi il compte. Ensuite, pour qui elle écrit. Puis vous lui donneriez les documents, au lieu de lui demander de se souvenir de ce qu’elle n’a jamais lu. Vous lui diriez les contraintes, le format, et à quoi ressemble un travail terminé. Enfin, vous lui diriez de venir vous voir si quelque chose manque. C’est exactement ce que Marc-André a fait. Pourquoi fournir les documents, au lieu de demander à l’assistant de se souvenir? Rappelez-vous le premier module. L’assistant ne sait de votre projet que ce que vous lui montrez. Sans l’offre de services, il ne peut pas savoir que le paiement en ligne est exclu. Avec l’offre, il le lit. Quand la réponse doit s’appuyer sur des faits, donnez la source. [Pause] Une consigne, c’est l’information qu’une personne nouvelle vous demanderait, écrite d’avance.

</details>
<!-- /slide -->

## Vérifier et corriger

La deuxième ébauche s’appuie sur les documents. Le paiement en ligne a disparu. Pourtant, elle annonce que le portail ouvre « dans les trois succursales le 15 mai ». Marc-André compare chaque date et chaque lieu au compte rendu. Celui-ci dit autre chose : un projet pilote à la succursale Est le 15 mai, puis Nord et Sud en octobre. L’ébauche a fusionné deux étapes en une. Marc-André répond par une correction précise :

> Dans le premier paragraphe, tu écris que le portail ouvre dans les trois succursales le 15 mai. Le compte rendu dit autre chose : un projet pilote à la succursale Est le 15 mai, puis Nord et Sud en octobre. Corrige seulement cette phrase.

<!-- slide: example -->
### Une erreur plausible, une correction précise

> **Assistant :** À partir du 15 mai, le portail ouvre dans les trois succursales…
>
> **Marc-André :** Le compte rendu dit autre chose : la succursale Est le 15 mai, en projet pilote, puis Nord et Sud en octobre. Corrige seulement cette phrase.

<details><summary>Notes de présentation</summary>

[1,5 min] [Montrez la deuxième réponse.] La deuxième réponse est bien meilleure. Le paiement en ligne a disparu, parce que l’assistant a lu l’offre. Mais regardez la première phrase : le portail ouvre dans les trois succursales le 15 mai. [Pause] Est-ce vrai? Marc-André vérifie chaque date et chaque lieu dans le compte rendu. Le 15 mai, c’est le projet pilote, à la succursale Est seulement. Nord et Sud suivent en octobre. L’assistant a fusionné deux étapes. L’erreur est plausible, et c’est pour ça qu’elle est dangereuse. Une lecture rapide ne l’aurait pas trouvée : la phrase est claire, et la date existe vraiment. Seule la vérification, document en main, l’a repérée. [Montrez la réponse de Marc-André.] Regardez comment il corrige. Il ne dit pas « fais mieux ». Il dit ce qui ne va pas, où, et ce qu’il veut à la place. Il demande de ne toucher qu’à cette phrase, pour ne pas tout réécrire.

</details>
<!-- /slide -->

Une bonne correction nomme le défaut : ce qui ne va pas, à quel endroit, et ce que vous voulez à la place. « Fais mieux » ne donne aucune information à l’assistant. Pour une grande tâche, découpez le travail en étapes et demandez d’abord un plan ou une structure, avant le texte complet. Et quand une conversation part de travers, ne vous acharnez pas : ouvrez-en une nouvelle, avec une meilleure consigne.

Le résumé corrigé, Marc-André le fait approuver par Hélène, la directrice générale de Location Pavois, avant l’envoi au personnel. Il conserve ensuite sa consigne : elle resservira pour le prochain résumé.

<!-- slide: concept -->
### Corrigez avec précision, et recommencez au besoin

- Le défaut, l’endroit, ce que vous voulez à la place
- Grande tâche : demandez d’abord un plan
- Conversation qui dérape : recommencez avec une meilleure consigne

<details><summary>Notes de présentation</summary>

[1,5 min] Trois habitudes rendent les itérations efficaces. La première, vous venez de la voir : nommer le défaut, l’endroit, et ce que vous voulez à la place. La deuxième vaut pour les grandes tâches. Avant un rapport de vingt pages, demandez d’abord un plan. Vous corrigez le plan en deux minutes, au lieu de corriger vingt pages. Pour le résumé de Marc-André, ce serait les titres des parties du résumé. Vous vérifiez qu’ils couvrent ce qui change et quand, puis vous demandez le texte. La troisième est la plus difficile à appliquer. Quand une conversation part de travers, on a envie d’argumenter avec l’assistant. Ça marche rarement. Ouvrez une nouvelle conversation, avec une meilleure consigne. Reprenez votre consigne, ajoutez ce que vous avez appris en chemin, et repartez de zéro. [Pause] Pour finir la boucle : Hélène, chez le client, approuve le résumé avant l’envoi. Et Marc-André garde sa consigne pour le prochain résumé.

</details>
<!-- /slide -->

## Pratique

L’atelier de la séance est la pratique de ce module : chaque personne y applique la même boucle à du matériel propre à son rôle.

## Récapitulatif

Le résumé de Marc-André est passé par toute la boucle : cadrer, donner le contexte, demander, examiner, itérer, vérifier, approuver et conserver. La première requête d’une ligne a produit une fonction inventée. La consigne complète, avec les documents, a réglé ce problème. La vérification a trouvé l’erreur qui restait : deux étapes du déploiement fusionnées en une. Ce qui a amélioré le résultat, c’est ce que Marc-André a fourni et vérifié.

<!-- slide: recap -->
### Ce que vous retenez de ce module

- Une boucle de huit étapes, pas une seule requête
- Les documents et la consigne font la différence
- Chaque date se vérifie avant l’approbation

<details><summary>Notes de présentation</summary>

[0,5 min] Qu’avez-vous remarqué entre la première et la dernière version? [Attendez deux réponses, puis montrez les énoncés.] Une boucle, pas une requête unique. Des documents et une consigne complète. Et une vérification, date par date. Le prochain module explique pourquoi les documents ont tout changé, et comment choisir ceux que vous donnez.

</details>
<!-- /slide -->

## Pour aller plus loin

Ces sujets ne sont pas présentés en séance. Ils servent de référence.

- Un gabarit de consigne réutilisable : le but, le contexte, les contraintes, le résultat attendu, les critères d’acceptation (*acceptance criteria*), et « pose-moi tes questions si quelque chose n’est pas clair ».
- Un ou deux exemples de ce qu’on attend valent mieux qu’un paragraphe d’adjectifs.
- Demandez des solutions de rechange, les avantages et les inconvénients de chacune, une critique de l’ébauche par l’assistant, ou la liste de ce dont il n’est pas sûr.
- Certaines habitudes ne servent plus : les formules magiques, les jeux de rôle incantatoires, « réfléchis étape par étape », les majuscules. Les modèles récents répondent à un contexte clair et au réglage de l’effort de réflexion.
- L’assistant peut améliorer votre consigne : « Que vous faudrait-il savoir pour bien faire ce travail? »
- Gardez ce qui fonctionne comme gabarit. Plus tard, un gabarit peut devenir un *skill* (voir le parcours Génie logiciel).

Sujets facultatifs :

- les exemples dans la requête, les résultats structurés (tableaux, JSON) et le plan suivi de l’exécution;
- les bibliothèques de requêtes d’une équipe, et leur entretien;
- la rédaction de requêtes pour d’autres modèles et pour des agents.

Le sens de chaque terme est dans le [glossaire](../../resources/R-02-glossary.md). Les lectures complémentaires (R-01) donnent les sources, section « Méthode de travail et rédaction de requêtes ».

## À revérifier avant chaque prestation

- L’enregistrement de la démonstration, chaque fois que l’interface de l’application approuvée change. Dernière vérification : à faire, l’enregistrement reste à produire.
