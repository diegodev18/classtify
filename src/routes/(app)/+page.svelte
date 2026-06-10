<script lang="ts">
  import { onMount } from "svelte";
  import { ApiError, getHealth, type HealthResponse } from "$lib/api/client";
  import Button from "$lib/components/ui/button.svelte";
  import Card from "$lib/components/ui/card.svelte";
  import CardHeader from "$lib/components/ui/card-header.svelte";
  import CardTitle from "$lib/components/ui/card-title.svelte";
  import CardContent from "$lib/components/ui/card-content.svelte";

  let health: HealthResponse | null = $state(null);
  let error: string | null = $state(null);
  let loading = $state(true);

  async function checkHealth() {
    loading = true;
    error = null;

    try {
      health = await getHealth();
    } catch (err) {
      health = null;
      error = err instanceof ApiError ? err.message : "No se pudo conectar con el backend";
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    void checkHealth();
  });
</script>

<div class="mx-auto flex max-w-3xl flex-col gap-6">
  <div>
    <h2 class="text-2xl font-semibold tracking-tight">Bienvenido a Classtify</h2>
    <p class="mt-1 text-sm text-muted-foreground">
      Plataforma local para gestión de horarios escolares.
    </p>
  </div>

  <Card>
    <CardHeader>
      <CardTitle>Estado del backend</CardTitle>
    </CardHeader>
    <CardContent class="space-y-4">
      {#if loading}
        <p class="text-sm text-muted-foreground">Comprobando conexión…</p>
      {:else if error}
        <div class="flex items-center gap-2">
          <span class="inline-flex h-2 w-2 rounded-full bg-destructive"></span>
          <p class="text-sm text-destructive">{error}</p>
        </div>
      {:else if health}
        <div class="flex items-center gap-2">
          <span class="inline-flex h-2 w-2 rounded-full bg-green-500"></span>
          <p class="text-sm">
            Backend conectado — <span class="font-medium">{health.status}</span>
            {#if health.version}
              <span class="text-muted-foreground"> (v{health.version})</span>
            {/if}
          </p>
        </div>
      {/if}

      <Button variant="outline" size="sm" onclick={() => checkHealth()} disabled={loading}>
        Reintentar
      </Button>
    </CardContent>
  </Card>
</div>
