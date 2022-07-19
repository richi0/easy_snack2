<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { City, LoadFunction } from '$lib/typing';
	export async function load({ fetch }: LoadFunction) {
		return idFetch('city/', -1, fetch, 'city');
	}
</script>

<script lang="ts">
	export let city: City[];
</script>

{#each city as c}
	<p>
		{c.name}
	</p>
{/each}
