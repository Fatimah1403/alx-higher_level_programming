#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
let characters = [];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movieData = JSON.parse(body);
  characters = movieData.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request.get(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
