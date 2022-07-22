<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { Country, LoadFunction } from '$lib/typing';
	export async function load({ fetch, params }: LoadFunction) {
		const id = (params?.id && params.id) || 1;
		return idFetch('country/', id, fetch, 'country');
	}
</script>

<script lang="ts">
	import Image from '$lib/components/Image.svelte';
	import ListCard from '$lib/components/ListCard.svelte';
	import Link from '$lib/components/Link.svelte';

	export let country: Country;
</script>

<p class="title">{country.name}</p>
<Image src={country.image} alt={country.name} />
<p class="description">{country.description}</p>

<div class="list">
	{#each country.cities as city}
		<ListCard>
			<Link slot="title" url={`/city/${city.id}`}>{city.name}</Link>
			<svelte:fragment slot="text">
				Number of Posts: {city.posts}
			</svelte:fragment>
		</ListCard>
	{/each}
</div>

<style lang="scss">
	.title {
		@include t1;
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
