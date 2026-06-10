<script lang="ts">
  import Card from "$lib/components/ui/card.svelte";
  import CardHeader from "$lib/components/ui/card-header.svelte";
  import CardTitle from "$lib/components/ui/card-title.svelte";
  import CardContent from "$lib/components/ui/card-content.svelte";
</script>

<div class="flex min-h-screen items-center justify-center bg-background p-6">
  <Card class="w-full max-w-md">
    <CardHeader>
      <CardTitle>Iniciar sesión</CardTitle>
    </CardHeader>
    <CardContent>
      <p class="text-sm text-muted-foreground">
        Autenticación con FastAPI Users — disponible en la siguiente iteración.
      </p>
    </CardContent>
  </Card>
</div>
