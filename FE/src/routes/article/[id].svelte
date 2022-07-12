<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('article/', id, fetch, 'article');
	}
</script>

<script lang="ts">
	import TextParagraph from '$lib/components/TextParagraph.svelte';
	import ImageParagraph from '$lib/components/ImageParagraph.svelte';
	import type { Article } from '$lib/typing';

	export let article: Article;
</script>

<div class="article">
	{article.title}
	{#if article.content}
		{#each article.content as paragraph}
			{#if paragraph.type_ === 'paragraph'}
				<TextParagraph {paragraph} />
			{/if}
			{#if paragraph.type_ === 'image'}
				<ImageParagraph {paragraph} />
			{/if}
		{/each}
	{/if}
</div>

<style>
	.article {
		display: flex;
		justify-content: center;
		flex-direction: column;
		gap: 20px;
		padding-bottom: 40px;
	}
</style>