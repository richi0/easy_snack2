<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch }: LoadFunction) {
		return idFetch('article/?p=', 1, fetch, ['results', 'next']);
	}
</script>

<script lang="ts">
	import { page } from '$app/stores';
	import ArticleTeaser from '$lib/components/ArticleTeaser.svelte';
	import LatestSnack from '$lib/components/LatestSnack.svelte';
	import type { Article } from '$lib/typing';
import Button from '$lib/components/Button.svelte';

	export let results: Article[];
	export let next: string;

	const loadMore = async () => {
		const data = await idFetch('article/?p=', Number(next.split('=')[1]), fetch, [
			'results',
			'next'
		]);
		results = [...results, ...data?.props?.results];
		next = data?.props?.next;
	};

	const latest = (): Article | null | undefined => {
		if (!$page?.params?.id || $page?.params?.id === '1') {
			return results.shift();
		}
		return null;
	};

	$: latestSnack = latest();
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

<div class="button">
	{#if next}
		<Button click={loadMore}>Load more Snacks</Button>
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

	.button {
		margin: 20px auto;
	}
</style>
