<script context="module" lang="ts">
	import { idFetch } from '$lib/fetch';
	import type { City, LoadFunction } from '$lib/typing';
	export async function load({ fetch }: LoadFunction) {
		return idFetch('city/', -1, fetch, 'cities');
	}
</script>

<script lang="ts">
	import CityCard from '$lib/components/CityCard.svelte';

	export let cities: City[];
</script>

<div class="list">
	{#each cities as city}
		<CityCard {city} />
	{/each}
</div>

<style>
	.list {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
	}
</style>
