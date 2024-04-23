#!/usr/bin/node
const reqest = require('request');
request.get(process.argv[2]).on('response', function (response){
	console.log('code: ${response.status.code}');
});
