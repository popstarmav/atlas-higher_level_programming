#!/usr/bin/node

// Get the command-line arguments excluding the first two (node and script path)
const [, , arg] = process.argv;

// Convert the argument to a number
const num = Number(arg);

// Check if the converted number is an integer
if (!isNaN(num) && Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
