<script lang="ts">
	export let src: string;
	export let alt: string;
</script>

<div>
    <img {src} {alt} />
</div>

<style>
    div {
        width: 100%;
        height: 100%;
        background-color: gray;
        line-height: 0;
    }

    img {
        object-fit: cover;
        width: 100%;
        height: 100%;
    }
</style>
