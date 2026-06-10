<script lang="ts">
  import { page } from "$app/stores";
  import type { Snippet } from "svelte";

  type NavItem = {
    href: string;
    label: string;
  };

  type Props = {
    children?: Snippet;
  };

  let { children }: Props = $props();

  const navItems: NavItem[] = [
    { href: "/", label: "Inicio" },
    { href: "/schedules", label: "Horarios" },
    { href: "/teachers", label: "Maestros" },
    { href: "/settings", label: "Configuración" },
  ];
</script>

<div class="flex min-h-screen bg-background">
  <aside class="flex w-56 flex-col border-r border-border bg-muted/30">
    <div class="border-b border-border px-4 py-5">
      <p class="text-xs font-medium uppercase tracking-wider text-muted-foreground">Classtify</p>
      <h1 class="text-lg font-semibold">Gestión escolar</h1>
    </div>

    <nav class="flex flex-1 flex-col gap-1 p-3">
      {#each navItems as item}
        <a
          href={item.href}
          class="rounded-md px-3 py-2 text-sm font-medium transition-colors hover:bg-muted {$page.url
            .pathname === item.href
            ? 'bg-primary text-primary-foreground hover:bg-primary/90 hover:text-primary-foreground'
            : 'text-foreground'}"
        >
          {item.label}
        </a>
      {/each}
    </nav>
  </aside>

  <div class="flex flex-1 flex-col">
    <header class="flex h-14 items-center border-b border-border px-6">
      <p class="text-sm text-muted-foreground">Panel de administración</p>
    </header>
    <main class="flex-1 p-6">
      {@render children?.()}
    </main>
  </div>
</div>
