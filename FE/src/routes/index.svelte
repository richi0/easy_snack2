<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		return idFetch('article/?p=', 1, fetch, ['results', 'previous', 'next']);
	}
</script>

<script lang="ts">
	import { page } from '$app/stores';
	import ArticleTeaser from '$lib/components/ArticleTeaser.svelte';
	import LatestSnack from '$lib/components/LatestSnack.svelte';
	import type { Article } from '$lib/typing';

	export let results: Article[];
	export let previous: string;
	export let next: string;

	const latest = (): Article | null | undefined => {
		if (!$page?.params?.id || $page?.params?.id === '1') {
			return results.shift();
		}
		return null
	};

	const getPage = (url: string): string | null => {
		if (url) {
			const urlParams = new URLSearchParams(url.split('?')[1]);
			return urlParams.get('p') || '1';
		}
		return null;
	};

	$: nextUrl = getPage(next);
	$: previousUrl = getPage(previous);
	$: latestSnack = latest()
</script>

{#if latestSnack}
	<div>
		<LatestSnack article={latestSnack} />
	</div>
{/if}

<div class="articles">
	{#each results as article}
		<ArticleTeaser {article} />
	{/each}
</div>

<div>
	{#if previousUrl}
		<a href="/{previousUrl}">Previous</a>
	{/if}
	{#if nextUrl}
		<a href="/{nextUrl}">Next</a>
	{/if}
</div>

<style>
	.articles {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		gap: 20px;
		padding-left: 10px;
		padding-right: 10px;
		max-width: 900px;
		justify-content: center;
		margin: 0 auto;
	}
</style>
