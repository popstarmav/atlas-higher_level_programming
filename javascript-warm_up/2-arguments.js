#!/usr/bin/env node

// Command-line excluding the first two
const args = process.argv.slice(2);

//Print a message depending on the number of arguments passed
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
}