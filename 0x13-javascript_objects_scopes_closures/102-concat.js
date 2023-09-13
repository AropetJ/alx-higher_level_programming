#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

fs.readFile(sourceFilePath1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.readFile(sourceFilePath2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const concatenatedContent = data1 + data2;

    fs.writeFile(destinationFilePath, concatenatedContent, (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
    });
  });
});
