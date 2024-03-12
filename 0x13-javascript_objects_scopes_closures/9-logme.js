#!/usr/bin/node
let fnarg = 0;

exports.logMe = function (item) {
  console.log(fnarg + ': ' + item);
  fnarg++;
};
