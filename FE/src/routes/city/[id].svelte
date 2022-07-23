<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { City, LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('city/', id, fetch, 'city');
	}
</script>

<script lang="ts">
	import ListCard from '$lib/components/ListCard.svelte';
	import Link from '$lib/components/Link.svelte';
	import Image from '$lib/components/Image.svelte';

	export let city: City;
</script>

<p class="title">{city.name}</p>
<div class="country">
	<span>
		Country:
		<Link url={`/country/${city.country}`}>{city.country_name}</Link>
	</span>
</div>
<Image src={city.image} alt={city.name} />
<p class="description">{city.description}</p>

<div class="list">
	{#each city.articles as article}
		<ListCard>
			<Link slot="title" url={`/article/${article.id}`}>{article.title}</Link>
		</ListCard>
	{/each}
</div>

<style lang="scss">
	.title {
		@include t1;
		text-align: center;
		margin-bottom: 16px;
	}

	.country {
		text-align: center;
		margin-bottom: 40px;
	}

	.description {
		margin-top: 40px;
	}

	.list {
		@include default-list;
		margin-top: 40px;
	}
</style>
