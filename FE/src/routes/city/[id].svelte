<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { City, LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('city/', id, fetch, 'city');
	}
</script>

<script lang="ts">
	export let city: City;
</script>

<p>{city.name}</p>
