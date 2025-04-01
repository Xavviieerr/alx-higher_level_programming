#!/usr/bin/node
const { argv } = require('node:process');

const args = argv.slice(2).map(Number); // Convert arguments to integers

if (args.length < 2) {
  console.log(0); // Not enough arguments
} else {
  args.sort((a, b) => b - a); // Sort in descending order
  console.log(args[1]); // Second biggest integer
}
