#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const fsArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + fsArg);
