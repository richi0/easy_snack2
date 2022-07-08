import { API_PATH } from './constants';

export const idFetch = async (
	url: string,
	id: number,
	fetch: (url: string) => Promise<Response>,
	result: string[] | string
) => {
	const res = await fetch(`${API_PATH}${url}${id}`);
	const body = await res.json();
	if (res.ok) {
		if (typeof result === 'string') {
			return {
				props: Object.fromEntries([[result, body]])
			};
		} else {
			const resDict = Object.fromEntries(result.map((key) => [key, body[key]]));
			return {
				props: { ...resDict }
			};
		}
	}
	return {
		status: res.status,
		error: new Error('Could not fetch the articles')
	};
};
