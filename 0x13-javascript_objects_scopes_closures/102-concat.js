#!/usr/bin/node

const fs = require('fs');
const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

if (!sourceFilePath1 || !sourceFilePath2 || !destinationFilePath) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const readStream1 = fs.createReadStream(sourceFilePath1);
const writeStream = fs.createWriteStream(destinationFilePath, { flags: 'a' });

readStream1.pipe(writeStream);

writeStream.on('finish', () => {
  const readStream2 = fs.createReadStream(sourceFilePath2);

  readStream2.pipe(writeStream);

  readStream2.on('end', () => {
    readStream1.close();
    readStream2.close();
    writeStream.close();
    console.log('Concatenation complete.');
  });
});

readStream1.on('error', (err) => {
  console.error(`Error reading source file 1: ${err.message}`);
  process.exit(1);
});

readStream2.on('error', (err) => {
  console.error(`Error reading source file 2: ${err.message}`);
  process.exit(1);
});

writeStream.on('error', (err) => {
  console.error(`Error writing to destination file: ${err.message}`);
  process.exit(1);
});
