import type { ImageParagraph, TextParagraph } from './typing';

export const ensureTextParagraph = (input: string | undefined): TextParagraph => {
	return {
		content: (input && input) || '',
		type_: 'paragraph'
	};
};

export const ensureImageParagraph = (
	input: string | undefined,
	caption: string | undefined
): ImageParagraph => {
	return {
		image: (input && input) || '',
		caption: (caption && caption) || '',
		type_: 'image'
	};
};
