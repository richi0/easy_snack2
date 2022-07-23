import { writable } from 'svelte/store';

export const commentStore = writable({
	name: '',
	email: '',
	comment: ''
})