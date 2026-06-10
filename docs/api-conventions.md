# Convenciones API

Base URL: `http://localhost:8000`

## Prefijo

Todos los endpoints de negocio y auth usan **`/api/v1`**.

## Health

```
GET /api/v1/health
→ { "status": "ok", "version": "0.1.0" }
```

## Respuestas exitosas

- Recurso único: objeto directo
- Listas (futuro): `{ "data": [...], "meta": { "page", "page_size", "total" } }`

## Errores

Formato estándar:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": []
  }
}
```

| HTTP | Código típico |
|------|---------------|
| 400 | `BAD_REQUEST` |
| 401 | `UNAUTHORIZED` |
| 403 | `FORBIDDEN` |
| 404 | `NOT_FOUND` |
| 422 | `VALIDATION_ERROR` |

## Paginación (futuro)

Query params: `page`, `page_size`

## IDs

UUID v4 en PostgreSQL.

## OpenAPI

FastAPI genera la spec en:

```
GET /openapi.json
```

Usar `openapi-typescript` para generar tipos TS cuando haya más endpoints.

> **Nota:** OpenAPI es la especificación REST de esta API. **OpenRouter** es el proveedor de LLM — son cosas distintas.
