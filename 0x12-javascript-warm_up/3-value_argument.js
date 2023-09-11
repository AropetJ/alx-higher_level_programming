#!/usr/bin/node

const firstArg = process.argv[2];

if (typeof firstArg !== 'undefined') {
  console.log(firstArg);
} else {
  console.log('No argument');
}
