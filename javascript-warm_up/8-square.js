#!/usr/bin/node

// Using const for constant values
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Checking if the conversion was successful and printing the result
if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
