<script lang="ts">
	import type { City } from '$lib/typing';
	import Link from './Link.svelte';

	export let city: City;
</script>

<div class="wrapper">
	<div class="city">
		<Link url={`/city/${city.id}`}>{city.name}</Link>
	</div>
	<div class="country">
		Country: <Link url={`/country/${city.country}`}>{city.country_name}</Link>
	</div>
	<span>Number of Posts: {city.posts}</span>
</div>

<style>
	.wrapper {
		display: flex;
		flex-direction: column;
		gap: 10px;
		width: 200px;
		border: 1px solid #03a5fc;
		padding: 16px;
	}

    .city {
        font-size: 20px;
        font-weight: 600;
    }

    span {
        font-size: 15px;
    }

</style>
