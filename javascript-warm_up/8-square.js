#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg, 10);

if (!arg || isNaN(size) || size <= 0) {
  if (!arg || isNaN(size)) {
    console.log('Missing size');
  }
} else {
  let i = 0;
  const line = 'X'.repeat(size);
  while (i < size) {
    console.log(line);
    i++;
  }
}
