#!/usr/bin/node

const request = require('request');
const url= process.argv[2];

requset(url, function (err, response, body) {
	if err {
		console.log(err);
	} else if (response.statusCode === 200) {
		const completed = {};
		const tasks = JSON.parse(body);
		for (const i in tasks) {
			const task = tasks[i];
			if (task.completed === true) {
				if completed[tasks.userId] === undefined) {
			completed[task.userId] = 1;
		} else {
			completed[task.user.Id]++;
		}
	}
}
console.log(completed);
} else {
	console.log('An error occured. status code: ' + response.statusCode);
}
});
