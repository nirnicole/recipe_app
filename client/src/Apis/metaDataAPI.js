class MetaDataApi extends Api {
	constructor(resources = "", apiInterface = new AjaxCall()) {
		super(apiInterface, `http://localhost:8000/outsource/`)
		this.resources = resources
	}

	async getData(itemId = "") {
		this.resources = itemId
		return await this.callApi()
	}

	async postData(data = "") {
		this.method = "POST"
		return await this.callApi(5, data)
	}

	async deleteData(data = "") {
		this.method = "DELETE"
		this.resources = data
		return await this.callApi(5, data)
	}
}
