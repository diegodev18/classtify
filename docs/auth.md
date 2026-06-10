# Autenticación

Classtify usa **[FastAPI Users](https://fastapi-users.github.io/fastapi-users/)** con estrategia **JWT bearer**, integrada en el backend FastAPI.

## Endpoints

Prefijo: `/api/v1/auth`

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/login` | Obtener JWT |
| POST | `/logout` | Cerrar sesión |
| POST | `/register` | Registro (configurable) |
| GET | `/users/me` | Usuario actual |

## Roles

Campo `role` en el modelo `User`:

- `admin`
- `coordinador`
- `maestro`

RBAC en backend via `require_role()` en `app/core/security.py`.

## Flujo Tauri (futuro)

1. Usuario inicia sesión en `/login` → `POST /api/v1/auth/login`
2. Respuesta incluye `access_token`
3. Guardar token en almacenamiento seguro (`tauri-plugin-store` — pendiente)
4. Cliente API adjunta `Authorization: Bearer <token>`

## Variables

```env
JWT_SECRET=change-me-in-production
JWT_LIFETIME_SECONDS=3600
```

## Scaffold actual

- Modelo `User` + migración Alembic
- Routers montados en FastAPI
- UI de login y guards de ruta — **próxima iteración**
