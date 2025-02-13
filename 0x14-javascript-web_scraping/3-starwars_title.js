#!/usr/bin/node
// Print movie title using movie ID

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
  console.error(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
