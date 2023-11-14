# Algo
## [x] Récupération des nom des départements
> URL : https://fr.wikipedia.org/wiki/D%C3%A9partement_fran%C3%A7ais

- [x] Scraping de la liste

OUTPUTS : 
```
[
    {
        "nom":"xxxx",
        "code":"00"
    },
    ...
]
```

## [0] Récupération des url des départements

- [0] Recherche avec google advence search


OUTPUTS : 
```
[
    {
        "nom":"xxxx",
        "code":"00",
        "url":"https://xxxx.gouv.fr/"
    },
    ...
]
```

## [0] Récupération des url des E.RNT

- [0] Complétion et vérification de la page
> https://www.xxxx.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques
> https://www.indre-et-loire.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques
- [0] Vérification de la page avec request

si mauvais :
- [0] Recherche avec google advence search

OUTPUTS : 
```
[
    {
        "nom":"xxxx",
        "code":"00",
        "urls": {
            "domaine":"https://xxxx.gouv.fr/",
            "E.RNT": "https://www.xxxx.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques"
        }
        
    },
    ...
]
```