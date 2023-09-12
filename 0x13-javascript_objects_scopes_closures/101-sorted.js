#!/usr/bin/node

const data = require('./101-data');
const dict = data.dict;

const occurrenceDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in occurrenceDict) {
    occurrenceDict[occurrences].push(userId);
  } else {
    occurrenceDict[occurrences] = [userId];
  }
}

console.log(occurrenceDict);
