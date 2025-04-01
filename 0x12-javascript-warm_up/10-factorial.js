#!/usr/bin/node
const { argv } = require('node:process');

function factorial(n) {
  if (isNaN(n) || n === 0) return 1; // Base case: factorial of NaN or 0 is 1
  return n * factorial(n - 1); // Recursive case
}

const num = parseInt(argv[2]);
console.log(factorial(num));
