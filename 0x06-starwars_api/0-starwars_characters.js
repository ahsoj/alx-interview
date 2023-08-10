#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

request(`${endpoint}/films/${filmId}/`, async function (error, res, body) {
  if (error) return console.log(error);

  let characters = JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, res, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
