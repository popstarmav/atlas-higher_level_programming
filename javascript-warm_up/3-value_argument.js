#!/usr/bin/node

// Using const for constant values
const arg = process.argv[2];

// Checking if any argument is passed and printing the result
console.log(arg !== undefined ? arg : 'No argument');
