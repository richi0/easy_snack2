<script lang="ts">
	import type { TextParagraph } from '$lib/typing';

	export let paragraph: TextParagraph;
</script>

<div>
	{#if paragraph.title}
		<p class="title">{paragraph.title}</p>
	{/if}
	<p class="content">{paragraph.content}</p>
</div>

<style>
	.title {
		font-size: 20px;
		font-weight: 600;
		margin-bottom: 8px;
	}

	.content {
		font-size: 20px;
	}
</style>
