#!/usr/bin/node
// script that prints the first argument passed to it.
if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv[2]) {
  console.log(process.arg[2]);
}
