# Intro_test
Lien vibe : [https://vibe.adatechschool.fr/archives/level-up/tests-et-tdd](https://vibe.adatechschool.fr/archives/level-up/tests-et-tdd)

Js testing intoduction: 

article : [https://www.freecodecamp.org/news/how-to-start-unit-testing-javascript/](https://www.freecodecamp.org/news/how-to-start-unit-testing-javascript/)

video : [https://www.youtube.com/watch?v=r9HdJ8P6GQI&ab_channel=Academind](https://www.youtube.com/watch?v=r9HdJ8P6GQI&ab_channel=Academind)

Python tests

video: [https://www.youtube.com/watch?v=1Lfv5tUGsn8&ab_channel=Socratica](https://www.youtube.com/watch?v=1Lfv5tUGsn8&ab_channel=Socratica)

A partir d'un code on cherche les résultats escomptés pour ce faire on crée un test qui peut etre automatisé et simplifié qui sera soit réussi soit échoué. 

avantage des tests: 

- On teste pour voir quel est l'erreur suite à l'application d'une suite de test,
- on gagne du temp, ça nous pousse à réfléchir au possible bug et pb, on peut intégrer ces test dans le flow des qu'on commit par exemple le test sera lancé.
- améliorer l'architecture de son code. On écrit un code plus indépendant les uns des autres et par conséquent on améliore notre code grâce à l'ensemble de ces contraintes.
- lister les fonctionnalités et cas de figures avant de coder
- on est sure que notre code fonctionne.

Un bon test est : 

- automatisé (plateformes d'intégration),
- rapide et facile à lancer (pvr lancer en local, facilite les expérimentation),
- facile à interpréter quand il échoue (on écrit un test pour qu'il échoue et qu'on comprenne ou en précisant la nom de la méthode publique testée, ou la fonctionnalité)

(src: [https://damien.pobel.fr/post/bon-test-unitaire-integration-fonctionnel/](https://damien.pobel.fr/post/bon-test-unitaire-integration-fonctionnel/))

### Les differents types de tests (unitaires, d’intégration, de parcours/validation)

types de test: 

- Fully isolated (testing one function) ⇒ Unit Tests (write a thousands of this) : on teste une partie de l'implémentation sans dépendances ou intégration.
- With dependencies (testing a function that calls a function) ⇒ Integration Tests (write a good couples of this) : on teste un code en lien avec une partie externe: database, autre dossier...
- Full Flow (validating a the DOM after a click) ⇒ End-toEnd Tests (write a few of these) : permet de voir si l'application en entier fonctionne.

The more dependencies you have the more complex it is. 

du coup plus c'est complexe moins on en écrit. 

Pour faire des test on a besoin d'outils:

- test runner such as Mocha : execute your tests summarize resuls
- assertion library : define testing logic conditions such as Chai
- Library for both runing test and asserting : Jest
- Headless browser : simulate browser interaction : Puppeteer.

### Qu’est ce que le code coverage (couverture de code)?

En génie logiciel, la couverture de code est une mesure utilisée pour décrire le taux de code source exécuté d'un programme quand une suite de test est lancée.(Wiki)

### Qu’est ce que le TDD?

Test Driven Development. 

video intro explicative: [https://www.youtube.com/watch?v=k7_WBqd6C0Y&ab_channel=LaMinuteAgile](https://www.youtube.com/watch?v=k7_WBqd6C0Y&ab_channel=LaMinuteAgile)

est une approche d'ingénierie logicielle consistant à réliser des tests avant meme de code la fonction resultante, ça permet d'être driver par le resultat attendu. 

Pourquoi? Refactorisation, code plus sure. 

En quoi ça consiste 

- ecrire en test unitaire
- lancer le test et s'assurer qu'il est faux
- ecrire le contenu de la fonction pour répondre au resultat du test attendu
- relancer le test et s'assurer qu'il passe
- affiner la fonction: refactoring
- verifier que le test passe toujours

### A quoi doit répondre un test unitaire (F.I.R.S.T.)?

These principles help to write well-crafted unit tests and will make testing easier. The purpose of these principles is to create clean code, and by extension clean tests

Fast

Independant

Repeatable

Self-validating

Timely

(src:[https://romainbrunie.medium.com/f-i-r-s-t-principles-4eec4b9c1cde](https://romainbrunie.medium.com/f-i-r-s-t-principles-4eec4b9c1cde))

### Note mini atelier test with Alya

utilisation de librairie spécifique au test : chai, mocha ou jasmine

créer dossier src et test (npm init) cf getting started de mocha

creer un fichier js dans src index.js 

test unitaire = niveau le plus fin ou on regarde si le code fonctionne vs test utilisateur par ex 
le test unitaire ne doit pas dépendre de l'environnement, pour cela il faut faire des mocks pour substituer

il vaut mieux mettre un seul return dans un élément 

TDD : écrire un test avt le code. 

 
