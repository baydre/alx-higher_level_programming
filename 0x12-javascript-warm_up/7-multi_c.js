#!/usr/bin/node
// script that prints x times "C is fun".
const x = Number(process.argv[2]);
if (!process.argv[2] || isNaN(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
