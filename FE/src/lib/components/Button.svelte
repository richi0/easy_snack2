<script lang="ts">
	export let type = 'primary';
	export let click: () => any;
</script>

<button on:click={click} class={type}>
	<slot />
</button>

<style>
	button {
		border: 0;
		padding: 10px;
		border-radius: 5px;
	}

	button:hover {
		animation-name: wiggle;
		animation-duration: 0.5s ;
        animation-iteration-count: infinite;
        animation-direction: alternate;
	}

	.primary {
		color: #fff;
		font-weight: bold;
		background: #03a5fc;
	}

	@keyframes wiggle {
		from {
			transform: rotateZ(0deg);
		}
		to {
			transform: rotateZ(10deg);
		}
	}
</style>
