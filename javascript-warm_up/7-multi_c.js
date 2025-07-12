#!/usr/bin/node
const arg = process.argv[2];
const count = parseInt(arg, 10);

if (!count || count < 1) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}
