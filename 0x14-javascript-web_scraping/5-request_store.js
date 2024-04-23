#!/usr/bin/node
const fs = require ('fs');
const  request = reqiure('request');
request(process.argv[2]).pipe(fs.crateWriteStream(procees.argv[3]));

