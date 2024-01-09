#!/usr/bin/node
// script that searches the second biggest integer in an arg-list.
let list = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i])) {
      list.push(Number(process.argv[i]));
    }
  }
  // removes duplicate
  let sorted = list.sort(function (a, b) { return a - b; }).reverse();
  let uniq = [...new Set(sorted)];
  console.log(uniq[1]);
}
