<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { Country, LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('country/', id, fetch, 'country');
	}
</script>

<script lang="ts">
	export let country: Country;
</script>

<p>{country.name}</p>
