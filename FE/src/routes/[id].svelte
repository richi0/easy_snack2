<script context="module">
	import { API_PATH } from '$lib/constants.ts';
	export async function load({ fetch, params }) {
		const res_raw = await fetch(`${API_PATH}article/?p=${params.id}`);
		const res = await res_raw.json();
		if (res_raw.ok) {
			return {
				props: {
					results: res.results,
					previous: res.previous,
					next: res.next
				}
			};
		}
		return {
			status: res_raw.status,
			error: new Error('Could not fetch the guides')
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
			console.log(urlParams.get('p'), next, url);
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
		</div>
	{/each}
	<div>
		{#if previousUrl}
			<a href={`/${previousUrl}`}>Previous</a>
		{/if}
		{#if nextUrl}
			<a href={`/${nextUrl}`}>Next</a>
		{/if}
	</div>
</div>
