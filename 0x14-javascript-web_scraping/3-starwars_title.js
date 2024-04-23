#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.oi/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
	if (err) {
		consloe.log(err);
	} else if (request.statusCode === 200) {
		const responeJSON = JSON.parse(body);
		console.log(responseJSON.title);
	} else {
	
		console.log('Error code: ' + response.statuCode);
	}
});
