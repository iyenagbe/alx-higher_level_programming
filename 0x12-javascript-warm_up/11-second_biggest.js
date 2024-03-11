#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const farr = process.argv.slice(2).map(Number);
  const fsecond = farr.sort(function (a, b) { return b - a; })[1];
  console.log(fsecond);
}
