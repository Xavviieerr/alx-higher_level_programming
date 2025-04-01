#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < parseInt(argv[2]); x++) {
    console.log('C is fun');
  }
}
