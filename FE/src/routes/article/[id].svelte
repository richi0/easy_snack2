<script context="module">
	import { API_PATH } from '$lib/constants.ts';
	export async function load({ fetch, params }) {
		const res = await fetch(`${API_PATH}article/${params.id}/`);
		const body = await res.json();
		if (res.ok) {
			return {
				props: {
					article: body,
				}
			};
		}
		return {
			status: res.status,
			error: new Error('Could not fetch the article')
		};
	}
</script>

<script>
	export let article;
</script>

<div>{article.title}</div>