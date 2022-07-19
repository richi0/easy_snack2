<script lang="ts">
	import type { Article } from '$lib/typing';
	import coin from '$lib/assets/coin.svg';
	import country from '$lib/assets/country.svg';
	import city from '$lib/assets/city.svg';
	import Link from './Link.svelte';
	import TextIcon from './TextIcon.svelte';

	export let article: Article;
</script>

<div>
	<TextIcon src={coin}>{article.cost}</TextIcon>
	<TextIcon src={city}>
		<Link url={`/city/${article.city}`}>{article.city_name}</Link>
	</TextIcon>
	<TextIcon src={country}>
		<Link url={`/country/${article.country}`}>{article.country_name}</Link>
	</TextIcon>
</div>

<style>
    div {
        display: flex;
        gap: 10px;
        flex-direction: column;
        align-items: center;
        border: 1px solid #03a5fc;
        padding: 16px;
        margin: 20px 0;
        font-weight: 600;
    }
</style>