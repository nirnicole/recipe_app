/*
  Author: Nir Nicole
*/

const model = recipeModel()
const renderer = recipeRender()

const generateData = function (attempts, user_input, gluten, dairy) {
	model
		.getData(user_input, gluten, dairy)
		.then((res) => renderer.renderResults(res))
		.catch((error) => errorHandeling(error, attempts, generateData))
}

$("#submit").on("click", function () {
	let user_input = $("#user-input").val()
	let gluten = $("#gluten-active").is(":checked")
	let dairy = $("#dairy-active").is(":checked")
	if (user_input != "") {
		model.initData()
		generateData(5, user_input, gluten, dairy)
	} else console.warn("no input")
})

$("body").bind("keypress", function (event) {
	if (event.keyCode === 13) {
		$("#submit").trigger("click")
	}
})

let errorHandeling = function (error, attempts, callback) {
	console.warn(error)
	if (attempts-- > 0) {
		console.warn(`coudlnt load user.\n
			Attampts left: ${attempts}\n
			trying again...`)
		callback(attempts)
	} else {
		console.log(`attampet limit reached, please check whats wrong`)
	}
}
