<script lang="ts">
	import logo from '$lib/assets/snacks.svg';
	export let height: number = 10;
	export let number: number = 0;
	export let coverColor: string = '#FFF';
</script>

<div class="wrapper">
	<div>
		<img width={height} {height} src={logo} alt={logo} />
		<img width={height} {height} src={logo} alt={logo} />
		<img width={height} {height} src={logo} alt={logo} />
		<img width={height} {height} src={logo} alt={logo} />
		<img width={height} {height} src={logo} alt={logo} />
	</div>
	<div class="cover" style={`width: ${100 - (20 * number)}%; background: ${coverColor}`} />
</div>

<style>
	.wrapper {
		position: relative;
	}

	.cover {
		position: absolute;
		left: 0;
		top: 0;
		height: 100%;
	}
</style>
