class AjaxCall {
	async getApi(url, method = "GET", apidata = "empty", resourcses = "") {
		let ajaxData = {
			url: url + resourcses,
			data: apidata,
			success: (result) => result,
			error: (result) => "error",
			type: method,
		}
		if (method != "GET") {
			ajaxData["dataType"] = "json"
			ajaxData["contentType"] = "application/json"
			ajaxData["data"] = JSON.stringify(apidata)
		}
		return await $.ajax(ajaxData)
	}
}
