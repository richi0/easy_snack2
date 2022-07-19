<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('city/', id, fetch, 'city');
	}
</script>

<script lang="ts">
	export let city;
	console.log(city);
</script>
