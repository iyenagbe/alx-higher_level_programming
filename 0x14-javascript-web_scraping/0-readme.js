#!/usr/bin/node
const fs = require ('fs');
fs.readfile(process.argv[2], 'utf8', function (error, content) {
	console.log(error || content);
});
