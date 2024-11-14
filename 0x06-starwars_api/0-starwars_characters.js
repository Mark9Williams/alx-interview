#!/usr/bin/node
// Fetches and prints the names of characters from a Star Wars movie

const request = require('request');

// Check if the movie ID is provided
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieID}/`;

// Fetch the movie data from the Star Wars API
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Fetch each character's name in order
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
