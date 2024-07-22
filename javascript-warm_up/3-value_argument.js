#!/usr/bin/node

const [, , arg] = process.argv;

// Print the first argument or "No argument" if no argument is passed
console.log(arg ? 'Argument found' : 'No argument');
