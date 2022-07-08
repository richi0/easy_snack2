<script lang="ts">
	import { page } from '$app/stores';
	import Icon from '$lib/components/Icon.svelte';
	import Link from '$lib/components/Link.svelte';
	import logo from '$lib/assets/snacks.svg';
</script>

<header>
	<div class="logo desktop">
		<Icon width={30} height={30} src={logo} />
		<Link active={false} url={'/'}>
			<span>Snackeroo</span>
		</Link>
	</div>
	<div class="logo mobile">
		<Icon width={20} height={20} src={logo} />
		<Link active={false} url={'/'}>
			<span>Snackeroo</span>
		</Link>
	</div>
	<nav>
		<Link active={$page.routeId === '[id]' || $page.routeId === ''} url={'/'}>Blog</Link>
		<Link active={$page.routeId === 'map'} url={'/map'}>Map</Link>
		<Link active={$page.routeId === 'country'} url={'/country'}>Country</Link>
		<Link active={$page.routeId === 'city'} url={'/city'}>City</Link>
		<Link active={$page.routeId === 'about'} url={'/about'}>About</Link>
	</nav>
</header>

<style>
	header {
		box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
		margin-bottom: 20px;
		display: flex;
		height: 50px;
		padding: 10px;
		align-items: center;
	}

	.logo {
		gap: 10px;
		font-size: 24px;
		margin-right: auto;
		align-items: center;
    font-weight: 600;
	}

	.mobile {
		display: flex;
	}

	.desktop {
		display: none;
	}

	nav {
		display: flex;
		gap: 10px;
	}

	@media (min-width: 600px) {
    .logo {
      font-size: 30px;
    }

		.mobile {
			display: none;
		}

		.desktop {
			display: flex;
		}

		nav {
			font-size: 20px;
		}

		.desktop {
			display: flex;
		}
	}
</style>
