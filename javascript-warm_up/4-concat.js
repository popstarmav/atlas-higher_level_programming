#!/usr/bin/node

// Get the command-line arguments excluding the first two (node and script path)
const [, , arg1, arg2] = process.argv;

// Print the arguments in the format " is "
console.log(`${arg1} is ${arg2}`);
