<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { City, LoadFunction } from '$lib/typing';
	export async function load({ fetch }: LoadFunction) {
		return idFetch('city/', -1, fetch, 'cities');
	}
</script>

<script lang="ts">
	import ListCard from '$lib/components/ListCard.svelte';
	import Link from '$lib/components/Link.svelte';

	export let cities: City[];
</script>

<div class="list">
	{#each cities as city}
		<ListCard>
			<Link slot="title" url={`/city/${city.id}`}>{city.name}</Link>
			<svelte:fragment slot="subtitle">
				Country: <Link url={`/country/${city.country}`}>{city.country_name}</Link>
			</svelte:fragment>
			<svelte:fragment slot="text">
				Number of Posts: {city.posts}
			</svelte:fragment>
		</ListCard>
	{/each}
</div>

<style lang="scss">
	.list {
		@include default-list
	}
</style>
