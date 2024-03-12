#!/usr/bin/node
exports.esrever = function (list) {
  let flen = list.length - 1;
  let f = 0;
  while ((flen - f) > 0) {
    const aux = list[flen];
    list[flen] = list[f];
    list[f] = aux;
    f++;
    flen--;
  }
  return list;
};
