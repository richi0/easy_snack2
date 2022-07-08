<script lang="ts">
	import { color } from '$lib/constants';
	export let active: boolean;
	export let url: string;
	export let linkColor: string = color.primary;
    

    const style = (): string => {
        let col = `color: ${linkColor};`
        return col
    }
</script>

<a href={url} style={style()} class={(active && 'active') || null}>
	<slot />
</a>

<style>
    a {
        transition: all 0.5s;
    }

    a:hover {
        filter: brightness(110%) saturate(140%)
    }

	.active {
		color: red !important;
        text-decoration: underline;
	}
</style>
