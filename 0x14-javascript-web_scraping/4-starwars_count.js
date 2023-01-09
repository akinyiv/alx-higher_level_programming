#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const char = results[i].characters;
      for (let j = 0; j < char.length; j++) {
        if (char[j].slice(char[j].length - 3, char[j].length - 1) === '18') { count += 1; }
      }
    }
    console.log(count);
  }
});
