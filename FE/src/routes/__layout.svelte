<script>
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<Header />
<div class="content">
	<slot />
</div>
<Footer />

<style>
	.content {
		margin-bottom: 40px;
	}
</style>