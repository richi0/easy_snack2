<script lang="ts">
	import Icon from './Icon.svelte';
	export let src: string;
	export let height = 20;
	export let width = 20;
</script>

<span>
	<Icon {width} {height} src={src} />
	<slot />
</span>

<style>
	span {
		display: flex;
		gap: 20px;
		align-items: center;
		align-content: center;
		height: 100%;
	}
</style>