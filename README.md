# Evvy Interview

Welcome! Before the session, please:
1. **Get the repo running locally** — follow the Quickstart below.
2. **Read [`CONTEXT.md`](./CONTEXT.md)** — this gives you the lay of the land so we can hit the ground running.

The sample data lives in [`backend/data/`](./backend/data/).

## Prerequisites

> **Docker is required.** The backend (Django + Postgres) runs entirely inside
> Docker containers. Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/)
> is installed and running before you do anything else.

- Docker Desktop (includes `docker compose`)
- Node 22 LTS — use [nvm](https://github.com/nvm-sh/nvm): `nvm install && nvm use` (reads `.nvmrc`)
- npm (comes with Node)

## Key Components
- python3 docker container
- postgres database
- django 4.2.1
- django rest framework
- gunicorn web server
- react 16.7
- react-router
- tailwind css precompilation

## Quickstart

### Backend
- `make build` and go make yourself a cup of coffee while you wait
  - If you are on an older version of Docker (v1) that doesn't have the `docker compose` plugin, you may need to install `docker-compose` separately and update the makefile accordingly
- `make up`, then visit http://localhost:8001/health/ to see healthcheck
- http://localhost:8001/api/v1/test-results/ returns data
- (optional) `make create_admin` to create a superuser if you want to browse data
  in the django admin at http://localhost:8001/admin/

### Frontend
- `npm install` from /frontend to install npm packages (or `make install_frontend` from root)
- `npm start` from /frontend (or `make start_frontend` from root) and go check out the app at `http://localhost:3000/`

### Sanity check
1. Make sure everything runs!
2. Go to http://localhost:3000, and view the list of test results on the `/tests/` page.
3. If that works, you're good to go.

## Migrations

Django migrations live in `backend/test_results/migrations/`. The container applies pending migrations automatically on startup, so you typically don't need to run them manually — but here's how to do it explicitly:

### Generating a new migration

After changing a model in `backend/test_results/models.py`, generate a migration file:

```bash
make makemigrations
```

You can also give it a descriptive name:

```bash
make makemigrations name=add_patient_email
```

The generated file appears in `backend/test_results/migrations/` and should be committed alongside your model changes.

### Applying migrations

```bash
make migrate
```

### Other useful commands

```bash
# See which migrations have/haven't been applied
make showmigrations

# Preview the SQL a migration will run (without executing it)
docker compose exec django python manage.py sqlmigrate test_results 0001

# Roll back to a specific migration (use "zero" to undo all)
docker compose exec django python manage.py migrate test_results 0001
```

### Writing a data migration

If you need to backfill or transform data (not just change schema), create an empty migration and use `RunPython`:

```bash
docker compose exec django python manage.py makemigrations --empty --name backfill_something test_results
```

Then edit the generated file:

```python
from django.db import migrations

def forwards(apps, schema_editor):
    MyModel = apps.get_model("test_results", "MyModel")
    MyModel.objects.filter(...).update(...)

def backwards(apps, schema_editor):
    pass  # or reverse the change

class Migration(migrations.Migration):
    dependencies = [("test_results", "0001_initial")]
    operations = [migrations.RunPython(forwards, backwards)]
```
