<script lang="ts">
	import { SERVER_PATH } from '$lib/constants';
	import type { ImageParagraph } from '$lib/typing';
	import Image from './Image.svelte';

	export let paragraph: ImageParagraph;
</script>

<div class="paragraph">
	<div class="image">
		<Image
			src={`${SERVER_PATH}${paragraph.image}`}
			alt={(paragraph.caption && paragraph.caption) || ''}
		/>
	</div>
	{#if paragraph.caption}
		<div class="caption">
			{paragraph.caption}
		</div>
	{/if}
</div>

<style>
	.paragraph {
		margin: 0 auto;
	}

	.image {
		width: 100%;
		max-height: 500px;
		overflow: hidden;
	}

	.caption {
		font-size: 16px;
		background: #94cbe996;
		padding: 10px;
	}

	@media (min-width: 600px) {
		.image {
			width: 100%;
			max-width: 600px;
			max-height: 450px;
		}
	}
</style>
