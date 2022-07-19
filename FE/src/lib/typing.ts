export type Article = {
	content: (TextParagraph|ImageParagraph)[] | [];
	id: string;
	author?: string;
	title: string;
	image: string;
	caption?: string;
	restaurant_name?: string;
	cost: string;
	country: string;
	country_name: string;
	city: string;
	city_name: string;
	google_map?: string;
	snacks?: number;
	preface?: string;
	publish_on?: string;
};

export type LoadFunction = {
  fetch: (url: string) => Promise<Response>;
  params?: Params;
};

export type Params = {
    id?: number
}

export type TextParagraph = {
	article?: number;
	content: string;
	order?: number;
	title?: string;
	type_: "paragraph";
}

export type ImageParagraph = {
	article?: number;
	image: string;
	caption?: string;
	type_: "image";
}

export type City = {
	id: number;
	country: string;
	country_name: string;
	image: string;
	name: string;
	posts: number;
	description: number;
};