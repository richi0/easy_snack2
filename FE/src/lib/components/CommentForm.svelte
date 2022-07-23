<script lang="ts">
	import { post } from '$lib/fetch';
	import { commentStore } from '$lib/stores';
	import Button from './Button.svelte';
	import Input from './Input.svelte';

	export let id: string;
	export let redirectUrl: string;

	let nameError = '';

	const submit = () => {
		console.log($commentStore);
		nameError = 'Error';
		/*
		post('http://localhost:7000/api/comment/', {
            name: name,
            email: email,
            comment: comment,
            article: id,
        })
        */
	};
</script>

<form>
	<Input type="text" placeholder="name" bind:value={$commentStore.name} error={nameError} />
	<Input type="email" placeholder="email" bind:value={$commentStore.email} error={nameError} />
	<Input type="text" placeholder="comment" bind:value={$commentStore.comment} error={nameError} />
	<div class="button">
		<Button type="primary" click={submit}>Submit</Button>
	</div>
</form>

<style>
	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 20px;
	}

	.button {
		max-width: 100px;
	}
</style>
