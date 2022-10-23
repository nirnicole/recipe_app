/*
  Author: Nir Nicole
*/
const recipeRender = function () {
	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template(metaData)
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}
	const renderResults = function (res) {
		renderComponent("#results-template", "#results", res)
		appandImgs(res.results)
	}
	const appandImgs = function (results) {
		for (item of results) {
			let elementToRender = `#${item.id}`
			renderComponent("#imgs-template", elementToRender, item)
		}
	}

	return {
		renderResults,
		renderComponent,
		appandImgs,
	}
}
