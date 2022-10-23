class MetaDataApi extends Api {
	constructor(resources = "", apiInterface = new AjaxCall()) {
		super(apiInterface, `http://localhost:8000/outsource/`)
		this.resources = resources
	}

	async getData(itemId = "cheese", gluten = false, dairy = true) {
		this.data = {
			"gluten": gluten,
			"dairy": dairy,
		}
		this.resources = itemId
		return await this.callApi()
	}

	//restful extention, not fully implemented
	async postData(data = "") {
		this.method = "POST"
		return await this.callApi(5, data)
	}

	//restful extention, not fully implemented
	async deleteData(data = "") {
		this.method = "DELETE"
		this.resources = data
		return await this.callApi(5, data)
	}
}
