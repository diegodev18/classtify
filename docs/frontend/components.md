# Componentes UI

Classtify usa **componentes propios** organizados al estilo shadcn (sin usar shadcn-svelte).

## Filosofía

| Carpeta | Contenido |
|---------|-----------|
| `src/lib/components/ui/` | Primitivos reutilizables (Button, Card, Input…) |
| `src/lib/components/` | Componentes de dominio (AppShell, etc.) |

**No** mezclar lógica de negocio en `ui/`.

## Convenciones

### Naming

- Archivos: `kebab-case.svelte` (`button.svelte`)
- Import: PascalCase (`import Button from "$lib/components/ui/button.svelte"`)

### Props estándar

- `class?: string` — mergeada con `cn()`
- `variant`, `size` — via `tailwind-variants`
- Forward de eventos nativos del elemento HTML

### Helper `cn()`

```ts
import { cn } from "$lib/utils/cn";

cn("base-class", conditional && "extra", className);
```

## Plantilla para nuevo componente

```svelte
<script lang="ts">
  import { tv, type VariantProps } from "tailwind-variants";
  import { cn } from "$lib/utils/cn";
  import type { Snippet } from "svelte";

  const variants = tv({
    base: "...",
    variants: { /* ... */ },
    defaultVariants: { /* ... */ },
  });

  type Props = VariantProps<typeof variants> & {
    class?: string;
    children?: Snippet;
  };

  let { class: className, children, ...rest }: Props = $props();
</script>

<div class={cn(variants(), className)} {...rest}>
  {@render children?.()}
</div>
```

## Componentes actuales

- **Button** — variantes: `default`, `secondary`, `outline`, `ghost`, `destructive`; tamaños: `sm`, `md`, `lg`
- **Card** — `Card`, `CardHeader`, `CardTitle`, `CardContent`

## Qué no hacer

- No usar el CLI de shadcn
- No copiar componentes sin adaptarlos a tokens propios
- No poner fetch o stores dentro de `ui/`
