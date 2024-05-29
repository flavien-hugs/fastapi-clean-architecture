# Clean Architecture: Gestion des enchères

Dans ce didacticiel, nous essayons d'implementer les fonctionnalité qu'un système de gestion des enchères pourrait avoir.
Nous explorerons comment TDD accompagnele développement d'une application Clean Architecture

## Les scénarios identifiés sur lesquels nous nous concentrons:
* Créer un article,
* Créer une enchère
* Soumettre une offre pour une enchère existante

## USE CASES:
- La soumissio d'une offre, cela implique la logique suivante:
  * vérifier si l'enchère à laquelle l'offre est soumise existe
  * vérifier si l'enchère est active
  * vérifier si le prix de l'offre est supérieur au prix de départ de l'enchère ou à l'enchère la plus élevée.
  * enregistrer l'enchère si toutes les conditions ci-dessus sont remplies.
