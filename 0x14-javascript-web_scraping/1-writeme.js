#!/usr/bin/node
const fs = require('fs');
fs.writefile(process.argv[2], process.argv[3], error => {
	if (error) console.log(error);
});
