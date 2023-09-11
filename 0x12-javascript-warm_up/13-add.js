#!/usr/bin/node

// Retrieve the first argument from process.argv
const arg1 = process.argv[2];

// Use parseInt to attempt conversion to an integer
const numOccurrences = parseInt(arg1);

// Check if numOccurrences is a valid integer (not NaN)
if (!isNaN(numOccurrences)) {
    // Use a loop to print "C is fun" the specified number of times
    for (let i = 0; i < numOccurrences; i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
