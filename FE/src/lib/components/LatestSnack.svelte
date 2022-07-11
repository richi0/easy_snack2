<script lang="ts">
	import type { Article } from '$lib/typing';
	import { goto } from '$app/navigation';
	import Snacks from './Snacks.svelte';
	import Image from './Image.svelte';
	export let article: Article;
</script>

<div class="card" on:click={() => goto(`/article/${article.id}/`)}>
	<div>
		<p>Latest Snack</p>
		<p class="title">{article.title}</p>
		<div class="authorRow">
			<p class="author">by {article.author}</p>
			<Snacks number={article.snacks} coverColor="94cbe996" height={16} />
		</div>
		<p class="preface">
			{article.preface}
		</p>
	</div>
	<div class="image">
		<Image src={article.image} alt={article.title} />
	</div>
</div>

<style>
	.card {
		display: flex;
		flex-direction: column-reverse;
		min-height: 400px;
		background: #94cbe996;
		justify-content: space-between;
		padding: 20px;
		gap: 20px;
        max-width: 820px;
        margin: 0 auto 20px;
	}

	.card:hover .title {
		color: #fc034e;
	}

	.title {
		font-size: 24px;
		margin-bottom: 8px;
		font-weight: 600;
	}

	.preface {
		font-size: 20px;
	}

	.authorRow {
		display: flex;
		justify-content: space-between;
	}
	.author {
		font-size: 18px;
		margin-bottom: 20px;
	}

	.image {
		min-width: 50%;
		min-height: 100%;
	}

	@media (min-width: 600px) {
		.card {
            flex-direction: row;
		}

		.image {
			width: 100%;
		}
	}
</style>
