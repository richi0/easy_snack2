<script context="module">
	import { API_PATH } from '$lib/constants.ts';
	export async function load({ fetch }) {
		const res = await fetch(`${API_PATH}test/`);
		const text = await res.json();
		if (res.ok) {
			return {
				props: {
					text: text.test1
				}
			};
		}
		return {
			status: res.status,
			error: new Error('Could not fetch the guides')
		};
	}
</script>

<script>
	export let text;
</script>

<div>{text}</div>
