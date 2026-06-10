# Classtify

Plataforma **local** de gestión de horarios escolares. Monorepo con app desktop (Tauri + SvelteKit) y backend (FastAPI + PostgreSQL).

## Stack

| Capa | Tecnología |
|------|------------|
| Desktop | Tauri 2 + SvelteKit + TypeScript |
| UI | Tailwind CSS 4 + componentes propios |
| Backend | FastAPI + FastAPI Users (JWT) |
| IA | OpenRouter (cliente en backend) |
| Base de datos | PostgreSQL 16 — Docker |
| ORM / Migraciones | SQLAlchemy + Alembic |
| Python | uv |
| Orquestación | Docker Compose |

### Roadmap

OR-Tools (motor de horarios), RAG/pgvector, Google Sheets API, CI/CD.

## Estructura

```
classtify/
├── src/              # Frontend SvelteKit
├── src-tauri/        # Shell Tauri (Rust)
├── backend/          # API FastAPI
├── docs/             # Documentación
├── docker-compose.yml
└── .env.example
```

## Requisitos

- Node.js 20+ y pnpm
- Rust (para Tauri)
- Docker
- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Inicio rápido

### 1. Variables de entorno

```bash
cp .env.example .env
cp backend/.env.example backend/.env
```

### 2. Base de datos

```bash
pnpm dev:db
# o: docker compose up postgres -d
```

### 3. Backend

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload --port 8000
```

### 4. Desktop

```bash
pnpm install
pnpm dev          # Tauri + hot reload
# pnpm dev:web    # solo frontend
```

### Demo completa en Docker

```bash
docker compose up -d
```

## Scripts

| Script | Descripción |
|--------|-------------|
| `pnpm dev` | App desktop (Tauri) |
| `pnpm dev:web` | Frontend sin Tauri |
| `pnpm dev:db` | Postgres en Docker |
| `pnpm dev:backend` | API con hot reload |
| `pnpm docker:up` | Postgres + backend |
| `pnpm check` | Type-check Svelte |

## Documentación

- [Arquitectura](docs/architecture.md)
- [Convenciones API](docs/api-conventions.md)
- [Autenticación](docs/auth.md)
- [IA / OpenRouter](docs/ai.md)
- [Componentes UI](docs/frontend/components.md)
- [Design tokens](docs/frontend/design-tokens.md)

## Licencia

MIT
