function rc4(data, key) {

	var box = Array(256)
	for (var i = 0; i < 256; i++) {
		box[i] = i
	}

	var x = 0
	for (var i = 0; i < 256; i++) {
		x = (x + box[i] + key.charCodeAt(i % key.length)) % 256
		var temp = box[i]
		box[i] = box[x]
		box[x] = temp
	}


	var x = 0
	var y = 0
	var out = []
	for (var i = 0; i < data.length; i++)
	{
		var code = data.charCodeAt(i)

		var x = (x + 1) % 256
		var y = (y + box[x]) % 256
		var temp = box[x]
		box[x] = box[y]
		box[y] = temp

		var k = (box[x] + box[y]) % 256

		out.push(String.fromCharCode(code ^ box[k]))
	}
	return out.join('')
}

// key = 'mysecret'
//
// a = rc4('hello world!', key)
// console.log(a)
//
// b = rc4(a, key)
// console.log(b)

// include >> https://raw.githubusercontent.com/dankogai/js-base64/master/base64.js
// Base64.encode(a)
