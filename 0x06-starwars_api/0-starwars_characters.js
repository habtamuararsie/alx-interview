#!/usr/bin/node
const request = require('request');
const filmId = process.argv.slice(1)[1];

(function () {
  if (!filmId || isNaN(parseInt(filmId))) {
    return;
  }

  const getName = (character) =>
    new Promise((resolve, reject) => {
      request(
        {
          method: 'GET',
          uri: character,
          json: true
        },
        function (error, response, body) {
          if (response.statusCode !== 200) {
            console.error(error);
          }
          const { name } = body;
          resolve(name);
        }
      );
    });

  request(
    {
      method: 'GET',
      uri: `https://swapi-api.hbtn.io/api/films/${filmId}/`,
      json: true
    },
    async function (error, response, body) {
      if (response.statusCode !== 200) {
        console.error(error);
      }
      const { characters } = body;
      for (let i = 0; i < characters.length; i++) {
        const name = await getName(characters[i]);
        console.log(name);
      }
    }
  );
})();