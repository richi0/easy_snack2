<script lang="ts">
	import type { Article } from '$lib/typing';
    import { goto } from '$app/navigation';
	import Snacks from './Snacks.svelte';
	export let article: Article;
</script>

<div class="card" on:click={() => goto(`/article/${article.id}/`)}>
	<p class="title">{article.title}</p>
	<div class="titleRow">
		<p class="date">{article.publish_on}</p>
		<Snacks number={article.snacks} height={20} />
	</div>
	<img class="image" src={article.image} alt={article.title} />
	<p class="preface">{article.preface}</p>
</div>

<style>
	.card {
		box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.2), 0 3px 5px 0 rgba(0, 0, 0, 0.19);
		margin: 10px;
		padding: 20px;
		display: flex;
		flex-direction: column;
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
		margin-bottom: 8px;
	}
</style>
