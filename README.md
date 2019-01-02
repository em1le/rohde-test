# rohde-test

# Introduction
Cette petite API permet la création, la suppression, la mise à jour et le listing de document
Elle a été réalisée avec l'aide de [Hug](http://www.hug.rest/)

# Pré-requis
Python >= 3.4
[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

# Installation
Pour installer le projet :
```shell
pip install -r requirements.txt
```

Les dépendances sont désormais installées.

Du côté de l'authentification j'ai privilégié les credentials (pour plus de simplicité)
Et puis j'avais un conflit de dépendance avec pyjwt (sinon j'aurais réalisé par token ou api key)

Enfin rendez-vous dans le fichier settings.py et vous aurez accés à des identifiants par défaut

```python
# settings.py
USERNAME = 'Emile'
PASSWORD = '1234'
```

# Mise en route
Pour mettre en route le serveur

```shell
hug -f core.py
```

Maintenant que l'api est en route passons au requêtes

# Exemple de requêtes

## POST /api/v1/create
```shell
curl -i -X POST -H 'Content-Type:application/json' -d "title=hello&content=my_content" http://username:password@localhost:8000/api/v1/create
```

## PATCH /api/v1/update
```shell
 curl -i -X PATCH -H 'Content-Type:application/json' -d "title=hello&content=content_update" http://username:password@localhost:8000/api/v1/update
```

## DELETE /api/v1/update
```shell
 curl -i -X DELETE -H 'Content-Type:application/json' -d "title=hello" http://Emile:1234@localhost:8000/api/v1/delete
```

## GET /api/v1/list/all
```shell
 curl -i -X GET -H 'Content-Type:application/json' http://username:password@localhost:8000/api/v1/list/all
```
