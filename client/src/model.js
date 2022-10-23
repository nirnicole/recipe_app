/*
  Author: Nir Nicole
*/
const recipeModel = function () {
	let metaInstance
	let cacheData

	function getCache() {
		return cacheData
	}

	function initData() {
		metaInstance = new MetaDataApi()
	}

	async function getData(userInput, gluten, dairy) {
		let promise = metaInstance.getData(userInput, gluten, dairy)
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			return results[0]
		})
	}

	//restful extention, not fully implemented
	async function addData(userInput) {
		let addedPlayerPromise = metaInstance.postData(userInput)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return results[0]
		})
	}

	//restful extention, not fully implemented
	async function deleteData(userInput) {
		let addedPlayerPromise = metaInstance.deleteData(userInput)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return results[0]
		})
	}

	return {
		getCache,
		getData,
		initData,
		addData,
		deleteData,
	}
}
