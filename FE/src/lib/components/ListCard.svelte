<div class="wrapper">
	<div class="title">
		<slot name="title"></slot>
	</div>
	<div class="subtitle">
		<slot name="subtitle"></slot>
	</div>
	<span>
		<slot name="text"></slot>
	</span>
</div>

<style lang="scss">
	.wrapper {
		display: flex;
		flex-direction: column;
		gap: 10px;
		width: 200px;
		border: 1px solid $primary;
		padding: 16px;
	}

    .title {
        font-size: 20px;
        font-weight: 600;
    }

    text {
        font-size: 15px;
    }
</style>
