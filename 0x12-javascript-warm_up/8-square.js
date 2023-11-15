#!/usr/bin/node
// script that prints a square.
const x = Number(process.argv[2]);
if (!process.argv[2] || isNaN(x)) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
