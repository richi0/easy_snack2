<script context="module">
	import { API_PATH } from '$lib/constants.ts';
	export async function load({ fetch, params }) {
		const res = await fetch(`${API_PATH}article/?p=${params.id}`);
		const body = await res.json();
		if (res.ok) {
			return {
				props: {
					results: body.results,
					previous: body.previous,
					next: body.next
				}
			};
		}
		return {
			status: res.status,
			error: new Error('Could not fetch the articles')
		};
	}
</script>

<script>
	export let results;
	export let previous;
	export let next;

	const getPage = (url) => {
		if (url) {
			const urlParams = new URLSearchParams(url.split('?')[1]);
			return urlParams.get('p') || 1;
		}
		return null;
	};

    $: nextUrl = getPage(next)
    $: previousUrl = getPage(previous)
</script>

<div>
	{#each results as article}
		<div>
			{article.title}
            <a sveltekit:prefetch href="/article/{article.id}">Details</a>
		</div>
	{/each}
	<div>
		{#if previousUrl}
			<a href=/{previousUrl}>Previous</a>
		{/if}
		{#if nextUrl}
			<a href=/{nextUrl}>Next</a>
		{/if}
	</div>
</div>
