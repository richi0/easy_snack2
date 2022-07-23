<script lang="ts">
	export let value: string;
	export let placeholder: string;
	export let error: string;
	export let type: 'text' | 'email' | 'password' = 'text';

	let isMoved = false;
	let placeholderRef: HTMLSpanElement;
	let inputRef: HTMLSpanElement;

	const setType = (node: any) => {
		node.type = type;
	};

	const movePlaceHolder = () => {
		if (!isMoved) {
			isMoved = true;
			placeholderRef.style.top = '-20px';
            inputRef.focus()
		}
	};
</script>

<div>
	<input bind:this={inputRef} on:click={movePlaceHolder} use:setType bind:value />
	<span class="placeholder" bind:this={placeholderRef} on:click={movePlaceHolder}
		>{placeholder}&nbsp</span
	>
	<span class="error">{error}&nbsp</span>
</div>

<style lang="scss">
	div {
		display: flex;
		flex-direction: column;
		max-width: 500px;
		width: 100%;
		position: relative;
	}
	input {
		@include i1;
        color: $black;
		width: 100%;
		border: 0;
		border-bottom: 2px solid $primary;
		padding: 10px 0;

		&:focus {
			outline: none;
            border-bottom: 2px solid $secondary;
		}
	}
	.placeholder {
		@include i1;
		position: absolute;
		top: 10px;
		transition: top 1s;
	}
	.error {
		color: $secondary;
	}
</style>
