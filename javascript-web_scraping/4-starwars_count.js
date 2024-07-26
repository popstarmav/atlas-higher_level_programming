#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
