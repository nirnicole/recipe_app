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
		let resObject = {
			playersData: res.metaData,
		}
		renderComponent("#results-template", "#results", resObject)
		appandImgs(res.metaData)
	}
	const appandImgs = function (metaData) {
		for (player of metaData) {
			let elementToRender = `#${player.id}`
			renderComponent("#imgs-template", elementToRender, player)
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
