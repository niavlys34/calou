FROM python:3.12-slim

# uv installé via l'image officielle (méthode recommandée)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copier uniquement les fichiers de dépendances d'abord (cache Docker)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Puis le reste du code
COPY . .

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "calou:create_app()"]