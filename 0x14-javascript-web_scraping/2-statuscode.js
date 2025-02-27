#!/usr/bin/node
// Displays GET request status code.

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
