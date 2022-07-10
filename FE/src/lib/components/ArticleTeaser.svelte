<script lang="ts">
	import type { Article } from '$lib/typing';
	import { goto } from '$app/navigation';
	import Snacks from './Snacks.svelte';
	import Image from './Image.svelte';
	export let article: Article;
</script>

<div class="card" on:click={() => goto(`/article/${article.id}/`)}>
	<p class="title">{article.title}</p>
	<div class="titleRow">
		<p class="date">{article.publish_on}</p>
		<Snacks number={article.snacks} height={20} />
	</div>
	<div class="image">
		<Image src={article.image} alt={article.title} />
	</div>
	<p class="preface">{article.preface}</p>
</div>

<style>
	.card {
		box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.2), 0 3px 5px 0 rgba(0, 0, 0, 0.19);
		margin: 10px;
		padding: 20px;
		display: flex;
		flex-direction: column;
		max-width: 800px;
		margin-left: auto;
		margin-right: auto;
	}

	.card:hover {
		box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.2), 0 10px 20px 0 rgba(0, 0, 0, 0.19);
	}

	.titleRow {
		display: flex;
		justify-content: space-between;
	}

	.title {
		font-size: 24px;
		font-weight: 600;
		margin-bottom: 4px;
	}

	.date {
		margin-bottom: 16px;
	}

	.image {
		margin: 0px auto 8px;
		width: 300px;
		height: 200px;
	}
	@media (min-width: 600px) {
		.image {
			width: 500px;
			height: 400px;
		}
	}
</style>
