# Design tokens

> **TBD — pendiente Claude Design.** Los tokens actuales son genéricos para el scaffold.

## Tokens semánticos

Definidos en `src/app.css` via `@theme`:

| Token | Uso |
|-------|-----|
| `--color-background` | Fondo de la app |
| `--color-foreground` | Texto principal |
| `--color-primary` | Acciones principales |
| `--color-primary-foreground` | Texto sobre primary |
| `--color-secondary` | Acciones secundarias |
| `--color-muted` | Fondos sutiles |
| `--color-muted-foreground` | Texto secundario |
| `--color-border` | Bordes |
| `--color-destructive` | Errores / acciones peligrosas |
| `--radius-sm`, `--radius-md`, `--radius-lg` | Border radius |

## Uso en Tailwind

```html
<div class="bg-background text-foreground border-border rounded-md">
  ...
</div>
```

## Tema oscuro

Automático via `@media (prefers-color-scheme: dark)` en `app.css`.

## Próximo paso

Cuando Claude Design entregue la paleta final:

1. Actualizar variables en `src/app.css`
2. Documentar valores hex/oklch aquí
3. Ajustar componentes `ui/` si cambian contrastes
