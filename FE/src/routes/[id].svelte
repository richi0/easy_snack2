<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('article/?p=', id, fetch, ['results', 'previous', 'next']);
	}
</script>

<script lang="ts">
	import type { Article } from '$lib/typing';

	export let results: Article[];
	export let previous: string;
	export let next: string;

	const getPage = (url: string): string | null => {
		if (url) {
			const urlParams = new URLSearchParams(url.split('?')[1]);
			return urlParams.get('p') || '1';
		}
		return null;
	};

	$: nextUrl = getPage(next);
	$: previousUrl = getPage(previous);
</script>

{#each results as article}
	<div>
		{article.title}
		<a sveltekit:prefetch href="/article/{article.id}">Details</a>
	</div>
{/each}
<div>
	{#if previousUrl}
		<a href="/{previousUrl}">Previous</a>
	{/if}
	{#if nextUrl}
		<a href="/{nextUrl}">Next</a>
	{/if}
</div>
