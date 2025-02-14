#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
