import { API_PATH } from './constants';

export const idFetch = async (
	url: string,
	id: number,
	fetch: (url: string) => Promise<Response>,
	result: string[]
) => {
	const res = await fetch(`${API_PATH}${url}${id}`);
	const body = await res.json();
	const resDict = Object.fromEntries(result.map((key) => [key, body[key]]));
	if (res.ok) {
		return {
			props: { ...resDict }
		};
	}
	return {
		status: res.status,
		error: new Error('Could not fetch the articles')
	};
};
