#!/usr/bin/node
// Read from file passed as command line arg.

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
