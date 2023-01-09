#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const char = JSON.parse(body).characters;
    for (let i = 0; i < char.length; i++) {
      request.get(char[i], function (err, response, body) {
        if (err) { console.log(err); } else { console.log(JSON.parse(body).name); }
      });
    }
  }
});
