#!/usr/bin/node
// script that searches the second biggest integer in an arg-list.
const list = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i])) {
      list.push(Number(process.argv[i]));
    }
  }
  // removes duplicate
  const sorted = list.sort(function (a, b) { return a - b; }).reverse();
  const uniq = [...new Set(sorted)];
  console.log(uniq[1]);
}
