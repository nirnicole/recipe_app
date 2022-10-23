/*
this is the parent class of all api classes.
every structual change will be made here and be inherited to each api class (see the error handeling for example).
note that each api will also implement its uniqe data proccess according to its destination api.
by default, all api calls are now a "GET" call.
*/
class Api {
	url = ""
	method = "GET"
	proccesedData = ""
	callerInteface

	constructor(callerInteface, url, method = "GET", resources = "") {
		this.callerInteface = callerInteface //dependancy injection
		this.url = url
		this.method = method
		this.resources = resources
		this.payload = {}
	}

	async callApi(attempts = 5, data = "") {
		return await this.callerInteface
			.getApi(this.url, this.method, data, this.resources)
			.catch((error) => {
				console.log(error)
				this.errorHandeler(this.callApi, attempts, data)
			})
	}

	errorHandeler(method, attempts, data = { "data": data }) {
		if (attempts-- > 0) {
			console.warn(`error in : ${this.constructor.name} \n
                        Attampts left: ${attempts}\n
                        trying again...`)
			return method(attempts, data)
		} else {
			console.log(`attampet limit reached, please check whats wrong`)
		}
	}

	processData(rawData) {
		this.proccesedData = rawData
		return this
	}
}
