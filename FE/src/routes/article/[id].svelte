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
	import Snacks from '$lib/components/Snacks.svelte';
	import { ensureImageParagraph, ensureTextParagraph } from '$lib/ensure';
import Stats from '$lib/components/Stats.svelte';

	export let article: Article;
</script>

<div class="article">
	<div class="titleRow">
		<div>
			<p class="title">
				{article.title}
			</p>
			<p class="date">
				{article.publish_on} by {article.author}
			</p>
		</div>
		<span class="snack">
			<Snacks number={article.snacks} reverse height={30} />
		</span>
	</div>
	<Stats {article} />
	<div class="content">
		<TextParagraph paragraph={ensureTextParagraph(article.preface)} />
		<ImageParagraph paragraph={ensureImageParagraph(article.image, article.caption)} />

		{#each article.content as paragraph}
			{#if paragraph.type_ === 'paragraph'}
				<TextParagraph {paragraph} />
			{/if}
			{#if paragraph.type_ === 'image'}
				<ImageParagraph {paragraph} />
			{/if}
		{/each}
	</div>
</div>

<style>
	.article {
		display: flex;
		justify-content: center;
		flex-direction: column;
		padding: 10px 20px 10px;
	}

	.titleRow {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 100%;
	}

	.title {
		display: flex;
		flex-direction: column;
		font-size: 24px;
		font-weight: 600;
		margin-bottom: 8px;
	}

	.snack {
		margin-right: auto;
		margin-bottom: 20px;
	}

	.date {
		font-size: 14px;
		font-weight: 600;
		color: #03a5fc;
		margin-bottom: 8px;
	}

	.content {
		display: flex;
		justify-content: center;
		flex-direction: column;
		gap: 20px;
	}

	@media (min-width: 600px) {
		.titleRow {
			flex-direction: row;
		}

		.title {
			flex-direction: row;
			justify-content: space-between;
			font-size: 24px;
			font-weight: 600;
			margin-bottom: 8px;
		}

		.snack {
			margin-left: auto;
			margin-right: 0;
			margin-bottom: 20px;
		}
	}
</style>
