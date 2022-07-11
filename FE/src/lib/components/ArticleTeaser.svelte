<script lang="ts">
	import type { Article } from '$lib/typing';
	import { goto } from '$app/navigation';
	import Snacks from './Snacks.svelte';
	import Image from './Image.svelte';
	export let article: Article;
</script>

<div class="card" on:click={() => goto(`/article/${article.id}/`)}>
	<div class="image">
		<Image src={article.image} alt={article.title} />
	</div>
	<div class="authorRow">
		<p class="author">by {article.author}</p>
		<Snacks number={article.snacks} height={10} />
	</div>
	<p class="title">{article.title}</p>
</div>

<style>
	.card {
		display: flex;
		flex-direction: column;
		max-width: 350px;
	}

	.card:hover .title {
		color: #03a5fc;
	}

	.title {
		font-size: 20px;
		margin-bottom: 4px;
	}

	.authorRow {
		display: flex;
		justify-content: space-between;
	}
	.author {
		font-size: 14px;
		margin-bottom: 4px;
	}

	.image {
		width: 340px;
		height: 350px;
	}

	@media (min-width: 450px) {
	.card {
		display: flex;
		flex-direction: column;
		max-width: 200px;
	}
		.image {
			margin: 0px auto 8px;
			width: 200px;
			height: 200px;
		}
	}
</style>
