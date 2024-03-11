#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const f = Number(process.argv[2]);
  let fi = 0;
  while (fi < f) {
    console.log('X'.repeat(f));
    fi++;
  }
}
