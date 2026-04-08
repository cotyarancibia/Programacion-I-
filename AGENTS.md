# AGENTS.md

## Repo Shape
- Django 6.0.4 backend for a pet-adoption API.
- `manage.py` uses `config.settings`; the Django project package is `config/`.
- App code is split across `base/` and `core/`.
- `config/urls.py` currently only mounts `admin/`; there are no app URL includes yet.
- `sqlite3` is the only configured database (`db.sqlite3`).

## Setup And Commands
- Create the virtualenv with `python -m venv venv` and activate it in PowerShell with `venv\Scripts\Activate.ps1`.
- Install dependencies with `pip install -r requirements.txt`.
- Apply migrations with `python manage.py migrate`.
- Run the dev server with `python manage.py runserver`.
- Run tests with `python manage.py test`.
- When changing models, run `python manage.py makemigrations` before `migrate`.

## Working Rules
- Keep `venv/`, `__pycache__/`, `*.pyc`, `db.sqlite3`, and `.env` out of commits; they are ignored in `.gitignore`.
- The project already enables `rest_framework`, `corsheaders`, and `drf_spectacular` in `config/settings.py`; preserve them unless you are deliberately removing that stack.
- `CORS_ALLOWED_ORIGINS` currently allows `http://localhost:3000`.

## Read Before Changing
- `README.md` is the only repo doc and matches the basic setup above.
- The app modules (`base/models.py`, `base/views.py`, `core/models.py`, `core/views.py`) are still placeholders, so most feature work will need real models/views/urls wired in.
