export type Article = {
	content?: string;
	id?: string;
	author?: string;
	title?: string;
	image?: string;
	caption?: string;
	restaurant_name?: string;
	cost?: string;
	country?: string;
	city?: string;
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

