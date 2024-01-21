#!/usr/bin/node
// script that computes and prints a factorial.
const factorial = function (num) {
  if (isNaN(Number(num))) {
    return (1);
  }
  return num ? num * factorial(num - 1) : 1;
};

const result = factorial(process.argv[2]);
console.log(result);
