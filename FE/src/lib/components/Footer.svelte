<script lang="ts">
	import { page } from '$app/stores';
	import Link from '$lib/components/Link.svelte';
	import { color } from '$lib/constants';
</script>

<footer>
	<Link linkColor={color.primary} active={$page.routeId === 'subscribe'} url={'/subscribe'}>Subscribe</Link>
	<Link linkColor={color.primary} active={$page.routeId === 'disclaimer'} url={'/disclaimer'}>Disclaimer</Link>
</footer>

<style>
	footer {
		margin-top: auto;
		height: 50px;
		display: flex;
		justify-content: center;
		padding: 10px;
		gap: 40px;
		align-items: center;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
	}
</style>
