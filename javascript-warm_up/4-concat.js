#!/usr/bin/node

// Get the command-line arguments excluding the first two (node and script path)
const args = process.argv.slice(2);

// Print the arguments in the format " is " if there are at least two arguments
if (args.length >= 2) {
  const [arg1, arg2] = args;
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log('Not enough arguments');
}
