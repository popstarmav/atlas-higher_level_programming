#!/usr/bin/node

function findSecondBiggest (args) {
    if (args.length <= 1) {
      return 0;
    }
  
    const numbers = args.map(Number);
    const uniqueNumbers = [...new Set(numbers)];
  
    if (uniqueNumbers.length === 1) {
      return 0;
    }
  
    uniqueNumbers.sort((a, b) => b - a);
    return uniqueNumbers[1];
  }
  
  const args = process.argv.slice(2);
  console.log(findSecondBiggest(args));
