---
title: "Mandat fictif : Location Pavois"
sources:
  - .ai/project/spec/curriculum/overlays/X-03-end-to-end-engagement-map.md
  - .ai/project/spec/curriculum/session/S-02-workshop.md
decision: .ai/project/decisions/0016-fictional-engagement.md
status: review
native_review: done 2026-11-11
---

<!-- Settled with the author on 2026-11-10 (OD-11, decision 0016). This brief fixes the facts; each pack or lesson writes the full document it uses. The programming language and the sample repository are left to OD-04 and OD-16. The E-03 labs use this project only if OD-16 chooses it. -->

# Mandat fictif : Location Pavois

Ce document décrit le mandat fictif d’où viennent les exemples et les exercices du programme. Il présente un client inventé, son projet, les neuf étapes du mandat et les documents qui passent d’un rôle à l’autre. Il s’adresse aux personnes qui animent les séances et à celles qui rédigent les leçons et les trousses d’atelier.

Les personnes participantes en voient seulement le paragraphe de contexte placé en tête de chaque trousse. Elles voient aussi la carte d’un mandat de bout en bout (X-03).

## Comment employer ce document

- Tout nom, date, chiffre ou document cité dans une leçon ou une trousse vient d’ici. Un fait nouveau s’ajoute d’abord à ce document.
- Les dates n’indiquent ni l’année ni le jour de la semaine, pour que le contenu ne vieillisse pas.
- Aucun lieu réel n’est nommé, et les personnes n’ont pas de nom de famille.
- Chaque personne garde son prénom et son rôle d’un exercice à l’autre.
- Chaque exercice reçoit un point de départ préparé, si bien qu’aucun parcours n’attend le travail d’un autre. Ce document en fixe les faits; le document complet est rédigé avec l’exercice qui l’emploie.
- Ici, « le client » désigne Location Pavois. Les personnes qui louent son matériel forment sa clientèle.
- Votre organisation, qui réalise le mandat, n’est jamais nommée.

## Le client

Location Pavois loue du matériel pour les événements : tentes, tables, chaises, sonorisation et éclairage. Sa clientèle réunit des particuliers qui organisent un mariage ou une fête, et des entreprises qui organisent une activité.

L’entreprise compte environ 60 personnes et trois succursales au Québec :

- Nord, la principale, où se trouve l’entrepôt;
- Sud;
- Est, la plus petite.

La haute saison va de mai à septembre.

Aujourd’hui, le personnel prend les réservations par téléphone ou par courriel. Chaque succursale les note dans sa propre feuille de calcul. L’acompte se paie par téléphone, par carte de crédit.

Deux personnes forment l’équipe des technologies de l’information (TI). Elles gèrent le site Web et les comptes de l’entreprise.

## Le projet

Votre organisation réalise pour Location Pavois un portail de réservation en ligne. La phase 1 comprend :

- un catalogue en ligne qui montre la disponibilité réelle du matériel;
- les demandes de réservation : dates, livraison ou retrait en succursale, adresse;
- les comptes clients;
- une application d’arrière-guichet pour le personnel : calendrier des réservations, confirmation des demandes, liste quotidienne des livraisons et des retraits.

La phase 1 exclut deux exigences de la demande d’offres de services :

- le paiement en ligne de l’acompte, qui reste téléphonique;
- le lien avec le logiciel comptable, remplacé par un fichier exporté chaque jour.

Une règle s’ajoute pendant la découverte : une demande de réservation doit laisser au moins trois jours avant la livraison ou le retrait. Le récit utilisateur partagé, plus bas, la précise.

## Les personnes

Chaque personne a un prénom et un rôle. Les prénoms commencent par des lettres différentes, pour que les notes de réunion restent faciles à suivre.

| Côté | Prénom | Rôle | Étapes où la personne intervient |
|---|---|---|---|
| Client | Hélène | Directrice générale et propriétaire | Découverte, offre de services, démarrage, livraison, suivi |
| Client | Patrick | Directeur des opérations | Découverte, spécification, suivi |
| Client | Amina | Coordonnatrice des réservations, succursale Est | Découverte, réalisation, suivi |
| Client | Kevin | Responsable des TI | Démarrage, réalisation, livraison |
| Votre équipe | Isabelle | Responsable du développement des affaires | Occasion d’affaires, découverte, offre de services |
| Votre équipe | Marc-André | Chargé de projet | Démarrage, vérification, livraison, suivi |
| Votre équipe | Léa | Analyste d’affaires et responsable de produit | Découverte, démarrage, spécification, suivi |
| Votre équipe | Simon | Designer | Spécification |
| Votre équipe | Julien | Développeur | Démarrage, réalisation, livraison |
| Votre équipe | Fatou | Analyste en assurance qualité | Vérification |

La direction de votre organisation, sans prénom, approuve deux décisions : répondre à la demande d’offres de services, puis envoyer l’offre.

## Les règles du client sur l’IA

À la réunion de démarrage, Kevin présente trois règles. Elles priment sur celles de votre organisation :

1. Les documents et les données de Location Pavois ne vont que dans l’assistant approuvé par votre organisation, avec le compte de l’organisation.
2. Aucun renseignement personnel de la clientèle ne va dans un assistant. L’équipe travaille à partir d’une extraction de données anonymisées.
3. L’équipe travaille dans le dépôt et les comptes de Location Pavois.

## Le déroulement du mandat

Le mandat suit les neuf étapes de la carte d’un mandat de bout en bout (X-03). À chaque étape, un document passe d’un rôle à l’autre, et une personne l’approuve : c’est le point d’approbation de l’étape.

| Étape | Date | Document transmis | Préparé par | Approuvé par | Vérification |
|---|---|---|---|---|---|
| 1. Occasion d’affaires | 15 janvier | La décision de répondre à la demande d’offres de services | Isabelle | La direction de votre organisation | Le mandat correspond à la capacité de l’équipe |
| 2. Découverte | 4 au 6 février | La synthèse de découverte | Léa | Hélène | Chaque besoin renvoie à une note; les contradictions sont signalées |
| 3. Offre de services | 20 février au 7 mars | L’offre de services | Isabelle | La direction de votre organisation, puis Hélène | Chaque engagement est dans la portée; aucune date n’est promise |
| 4. Démarrage et mise en place | 16 mars | Le compte rendu de la réunion de démarrage; les accès au dépôt et aux comptes | Marc-André; Kevin pour les accès | Hélène pour le projet pilote, Kevin pour les accès | L’équipe connaît les règles du client sur l’IA |
| 5. Spécification | 27 mars | Les récits utilisateur et leurs critères d’acceptation | Léa, avec Simon | Patrick | Chaque critère d’acceptation peut être testé |
| 6. Réalisation | 30 mars au 1er mai | Les modifications révisées | Julien | Kevin, qui accepte les demandes de fusion | Les tests passent; le *diff* a été lu |
| 7. Vérification | 4 au 8 mai | La version prête pour le projet pilote | Fatou | Marc-André | Chaque critère d’acceptation est vérifié |
| 8. Livraison et passation | 15 mai | Les notes de mise à jour; le document de passation | Julien pour les notes, Marc-André pour le document | Hélène; Kevin reçoit le document | Kevin peut exploiter le portail sans l’équipe |
| 9. Suivi | 26 juin | Le rapport sur six semaines de réservations | Léa | Hélène | Chaque chiffre renvoie aux données |

### 1. Occasion d’affaires

Le 15 janvier, Location Pavois envoie une demande d’offres de services à quelques firmes, dont votre organisation. Les réponses sont attendues le 21 février. La demande énumère six exigences :

1. un catalogue en ligne qui montre la disponibilité réelle;
2. les demandes de réservation en ligne;
3. les comptes clients;
4. une application d’arrière-guichet pour le personnel;
5. le paiement en ligne de l’acompte;
6. un lien avec le logiciel comptable.

Isabelle analyse la demande et recommande d’y répondre. La direction de votre organisation approuve.

Exercice, avec son point de départ préparé :

- B-04 : la demande d’offres de services.

C-01 s’en sert aussi comme exemple : Isabelle lit la demande avec l’assistant.

### 2. Découverte

Le 4 février, Isabelle et Léa rencontrent Hélène, Patrick et Amina. Hélène et Patrick se contredisent sur l’échéance :

- Hélène veut le portail pour le 1er mai, avant la saison des mariages;
- Patrick refuse de changer de système en haute saison, de mai à septembre.

La réunion se termine sans trancher. Patrick ajoute qu’il faut au moins trois jours pour préparer une commande.

Les 5 et 6 février, Léa mène des entrevues avec trois personnes des comptoirs, dont Amina. Elle rédige ensuite la synthèse de découverte, qui signale la contradiction sur l’échéance sans la trancher.

Exercices, avec leur point de départ préparé :

- trousse B de la séance commune : les notes brutes de la réunion du 4 février;
- P-01 : les notes des trois entrevues;
- C-06 : un résumé de la réunion rédigé par un assistant, avec deux erreurs, et les notes d’origine.

### 3. Offre de services

Avant de rédiger l’offre, Isabelle compare trois options : le développement sur mesure et deux logiciels de location inventés pour l’exercice.

Le 20 février, votre organisation envoie son offre de services. L’offre couvre les quatre premières exigences en phase 1 et reporte les deux autres à une phase 2. Elle ne promet aucune date de mise en service : cette date sera fixée à la réunion de démarrage.

Le 27 février, Hélène écrit à Isabelle pour savoir quand le portail sera prêt. Le 3 mars, elles en parlent au téléphone, et l’appel se termine sans date. Hélène accepte l’offre le 7 mars.

Exercices, avec leur point de départ préparé :

- trousse C de la séance commune : les notes d’Isabelle après l’appel du 3 mars, et le courriel du 27 février;
- B-01 : les mêmes documents, plus détaillés;
- B-02 : la description des trois options.

### 4. Démarrage et mise en place

Le 16 mars, la réunion de démarrage réunit Hélène, Patrick et Kevin, avec Marc-André, Léa et Julien. Hélène tranche la question de l’échéance :

- un projet pilote à la succursale Est à partir du 15 mai, avec les réservations par téléphone en parallèle;
- les succursales Nord et Sud en octobre, après la haute saison.

Kevin crée le dépôt du portail dans les comptes de Location Pavois et en donne l’accès à l’équipe. Il présente aussi les trois règles sur l’IA. Marc-André rédige le compte rendu de la réunion.

Le même jour, Marc-André prépare un résumé du projet pour le personnel des succursales. C’est l’exemple de la séance commune.

Emplois de cette étape :

- C-01 : la date d’ouverture, d’abord demandée sans document, puis avec l’offre de services et le compte rendu;
- C-04 et la séance commune : le résumé pour le personnel (voir « L’exemple de la séance commune »);
- X-01 : ses exemples de premier jour chez un client.

### 5. Spécification

Léa, avec Simon, tire de la synthèse de découverte les récits utilisateur et leurs critères d’acceptation. Patrick les approuve le 27 mars. Simon propose les écrans de réservation.

Exercices, avec leur point de départ préparé :

- P-02, l’atelier du parcours Produit et expérience : la synthèse de découverte;
- P-04 : l’écran de demande de réservation;
- E-04 : une tâche décrite en une ligne, tirée de la synthèse, autre que le récit partagé.

### 6. Réalisation

Du 30 mars au 1er mai, Julien réalise les récits dans le dépôt de Location Pavois. Chaque modification passe par une demande de fusion. Kevin en fait la revue de code et l’accepte.

En avril, pendant une démonstration, Amina signale un bogue : du matériel apparaît disponible le jour même de son retour.

Exercices, avec leur point de départ préparé :

- trousse A de la séance commune : la fonction qui calcule la disponibilité, le signalement d’Amina et une convention de code d’une ligne;
- E-02, l’atelier du parcours Génie logiciel : le récit partagé, à réaliser dans le dépôt d’exemple;
- E-01 : le module qui calcule la disponibilité;
- E-06 : une question de conception sur le calcul de la disponibilité;
- E-07 : un signalement qui contient une instruction cachée.

### 7. Vérification

Du 4 au 8 mai, Fatou vérifie chaque critère d’acceptation sur la version prête pour le projet pilote. Marc-André donne le feu vert le 8 mai.

Exercice, avec son point de départ préparé :

- E-05 : une demande de fusion dans laquelle un test a été affaibli discrètement.

### 8. Livraison et passation

Le 15 mai, le portail ouvre à la succursale Est, avec l’approbation d’Hélène. Julien rédige les notes de mise à jour. Marc-André remet le document de passation à Kevin.

Exercices, avec leur point de départ préparé :

- E-08 : les demandes de fusion acceptées, dont l’agent tire les notes de mise à jour;
- P-05 : un paragraphe de la page d’aide du portail, rédigé par un assistant.

### 9. Suivi

Le 26 juin, après six semaines de projet pilote, Marc-André et Léa rencontrent Hélène, Patrick et Amina. Léa présente un rapport tiré de l’extraction de données anonymisées des réservations. Location Pavois ouvre aussi un poste de coordonnateur ou de coordonnatrice des réservations en ligne.

Exercices, avec leur point de départ préparé :

- P-06 : l’extraction des six semaines, qui contient des lignes en double;
- P-03 : les notes de la réunion de suivi;
- B-03 : la description du poste.

## Le récit utilisateur partagé

Ce récit relie le parcours Produit et expérience au parcours Génie logiciel. L’atelier P-02 le produit parmi d’autres récits, et l’atelier E-02 le réalise. Chacun des deux parcours peut avoir lieu en premier. Les deux ateliers reçoivent donc ce texte tout prêt : P-02 comme corrigé, E-02 comme point de départ.

Il vient de Patrick, à la réunion de découverte : « Il nous faut au moins trois jours pour préparer une commande. » Patrick l’approuve le 27 mars.

> En tant que personne qui réserve en ligne, je veux savoir tout de suite si ma date est trop proche, afin d’en choisir une que la succursale pourra respecter.

Critères d’acceptation :

1. Si la date de livraison ou de retrait tombe moins de trois jours après la demande, le portail refuse la demande. Il propose alors la première date possible.
2. Si cette date tombe exactement trois jours après la demande, le portail accepte la demande.
3. Le délai se compte en jours de calendrier, fins de semaine comprises.

Par exemple, une demande faite le 2 mai pour le 5 mai est acceptée. Pour le 4 mai, elle est refusée, et le portail propose le 5 mai.

## L’exemple de la séance commune

La séance commune suit un seul exemple, de la démonstration de C-04 jusqu’au récapitulatif. Il se situe au démarrage du mandat.

1. Marc-André écrit une demande faible : « Écris un résumé du projet pour le personnel. » Au point de contrôle 3, la personne qui anime montre cette demande au groupe.
2. Sans contexte, l’assistant produit un texte générique. Il invente des fonctions, dont le paiement en ligne, que la phase 1 exclut.
3. Marc-André joint l’offre de services et le compte rendu de la réunion de démarrage. Il précise le public, soit le personnel des comptoirs, sans connaissances techniques. Il fixe la longueur à une page et le but : ce qui change pour le personnel, et quand. Il demande aussi à l’assistant de poser ses questions avant d’écrire.
4. La deuxième ébauche s’appuie sur les documents. Elle annonce pourtant l’ouverture « dans les trois succursales le 15 mai » : elle confond le projet pilote et le déploiement d’octobre.
5. Marc-André compare chaque date et chaque lieu au compte rendu. Il corrige l’erreur : la succursale Est le 15 mai, Nord et Sud en octobre.
6. Hélène approuve le résumé avant son envoi au personnel.

Les extraits du point de contrôle 4 (C-07) peuvent venir du même mandat. Par exemple, les notes d’un appel contiennent le numéro de carte d’une personne qui réserve.

## Le paragraphe de contexte des trousses

Chaque trousse d’atelier commence par ce paragraphe, suivi d’une phrase qui nomme son étape.

> Location Pavois loue du matériel pour les événements : tentes, tables, chaises, sonorisation et éclairage. L’entreprise compte trois succursales au Québec. Elle prend aujourd’hui ses réservations par téléphone et les note dans des feuilles de calcul. Votre équipe réalise pour elle un portail de réservation en ligne. Les noms, les dates et les documents de cette trousse sont fictifs.
