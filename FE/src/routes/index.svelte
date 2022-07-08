<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('article/?p=', id, fetch, ['results', 'previous', 'next']);
	}
</script>

<script lang="ts">
    import Index from './[id].svelte'
	import type { Article } from '$lib/typing';

	export let results: Article[];
	export let previous: string;
	export let next: string;
</script>

<Index {results} {previous} {next}/>