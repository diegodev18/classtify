# IA — OpenRouter

Classtify usa **[OpenRouter](https://openrouter.ai/)** como proveedor único de LLM.

## Principio de seguridad

La API key **nunca** va al cliente Tauri. Todas las llamadas pasan por `backend/app/ai/openrouter.py`.

## Variables de entorno

```env
OPENROUTER_API_KEY=sk-or-...
OPENROUTER_DEFAULT_MODEL=anthropic/claude-sonnet-4
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

## Cliente

```python
from app.ai.openrouter import OpenRouterClient

client = OpenRouterClient()
response = await client.chat([
    {"role": "user", "content": "Hola"},
])
```

Si falta `OPENROUTER_API_KEY`, el cliente lanza `OpenRouterError`.

## Roadmap RAG

1. Añadir **pgvector** a PostgreSQL
2. Pipeline de embeddings de documentos escolares
3. Endpoint `/api/v1/ai/chat` protegido con JWT
4. UI de asistente en el desktop

El scaffold actual solo incluye el cliente HTTP — sin endpoints de chat ni RAG.
