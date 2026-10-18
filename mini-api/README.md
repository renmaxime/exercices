# mini-api

API REST en FastAPI qui gère des items (CRUD complet) stockés en mémoire, avec validation Pydantic et tests automatisés.

## Endpoints

| Méthode | Route | Description | Codes |
|---|---|---|---|
| GET | `/health` | Vérifie que l'API répond | 200 |
| GET | `/items` | Liste tous les items | 200 |
| GET | `/items/{item_id}` | Renvoie un item | 200, 404 |
| POST | `/items` | Crée un item | 201, 422 |
| PUT | `/items/{item_id}` | Remplace le nom d'un item | 200, 404, 422 |
| DELETE | `/items/{item_id}` | Supprime un item | 204, 404 |

Les données sont gardées en mémoire : elles sont réinitialisées à chaque redémarrage du serveur.

## Installation

Python 3.12 recommandé.

```bash
cd mini-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer

```bash
uvicorn main:app --reload
```

L'API tourne sur http://127.0.0.1:8000. La documentation interactive (Swagger) est sur http://127.0.0.1:8000/docs.

## Tests

```bash
pytest -v
```

Les tests utilisent le `TestClient` de FastAPI et couvrent chaque route, y compris les cas 404.

## Exemples

Créer un item :

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Camille"}'
```

```json
{"id": 3, "name": "Camille"}
```

Lister les items :

```bash
curl http://127.0.0.1:8000/items
```

```json
[{"id": 1, "name": "Jean"}, {"id": 2, "name": "Benoit"}, {"id": 3, "name": "Camille"}]
```
