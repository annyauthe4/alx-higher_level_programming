#!/usr/bin/node
// Writes to a file

const fs = require('fs');
const fp = process.argv[2];
const text = process.argv[3];

fs.writeFile(fp, text, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
