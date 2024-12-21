#!/usr/bin/node

/*
Concatenates 2 files.
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const fs = require('fs');
// Get file paths
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

// Read the contents of source files
const content1 = fs.readFileSync(sourceFile1, 'utf-8');
const content2 = fs.readFileSync(sourceFile2, 'utf-8');

// Write to destination file
fs.writeFileSync(destFile, content1 + content2, 'utf-8');
