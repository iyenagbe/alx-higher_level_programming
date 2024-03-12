#!/usr/bin/node
const flist = require('./100-data.js').list;
console.log(flist);
console.log(flist.map((item, index) => item * index));
