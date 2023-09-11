#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * computeFactorial(n - 1);
}

const arg1 = process.argv[2];

const num = parseInt(arg1);

const result = computeFactorial(num);

console.log(result);
