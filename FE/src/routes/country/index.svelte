<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { Country, LoadFunction } from '$lib/typing';
	export async function load({ fetch }: LoadFunction) {
		return idFetch('country/', -1, fetch, 'countries');
	}
</script>

<script lang="ts">
import ListCard from '$lib/components/ListCard.svelte';
import Link from '$lib/components/Link.svelte';


	export let countries: Country[];
</script>

<div class="list">
	{#each countries as country}
		<ListCard>
			<Link slot="title" url={`/country/${country.id}`}>{country.name}</Link>
			<svelte:fragment slot="text">
				Number of Posts: {country.posts}
			</svelte:fragment>
		</ListCard>
	{/each}
</div>

<style>
	.list {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
		margin-bottom: 40px;
	}
</style>
