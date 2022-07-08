<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('article/', id, fetch, 'article');
	}
</script>

<script lang="ts">
	import type { Article } from '$lib/typing';
	export let article: Article;
</script>

<div>{article.title}</div>