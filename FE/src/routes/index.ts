export async function get() {
	return {
		headers: { Location: '/1' },
		status: 302
	};
}
