<script lang="ts">
  import { AppShell } from "$lib/components";
  import type { Snippet } from "svelte";

  type Props = {
    children?: Snippet;
  };

  let { children }: Props = $props();
</script>

<AppShell>
  {@render children?.()}
</AppShell>
