#!/usr/bin/node

// Using const for constant values
const arg = process.argv[2];

// Convert the argument to an integer
const occurrences = parseInt(arg);

// Checking if the conversion was successful and printing the result
if (!isNaN(occurrences)) {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
