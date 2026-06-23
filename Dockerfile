FROM python:3.14-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]