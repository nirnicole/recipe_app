/*
  Author: Nir Nicole
*/
const rupgRender = function () {
	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template(metaData)
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}
	const renderResults = function (res) {
		console.log(res)
		renderComponent("#results-template", "#results", res)
		appandImgs(res.results)
	}
	const appandImgs = function (results) {
		for (item of results) {
			let elementToRender = `#${item.id}`
			renderComponent("#imgs-template", elementToRender, item)
		}
	}
	const renderCard = function (pid, pdata) {
		let elementToRender = `#card${pid}`
		renderComponent("#card-template", elementToRender, pdata)
		renderComponent("#imgs-template", `#${pid}`, pdata)
	}

	return {
		renderResults,
		renderComponent,
		appandImgs,
		renderCard,
	}
}
