#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const char = JSON.parse(body).characters;
    const limit = char.length;
    Characters(0, char[0], char, limit);
  }
});

function Characters (i, url, charList, limit) {
  if (i === limit) { return; }
  request.get(url, function (err, respinse, body) {
    if (err) { console.log(err); } else {
      console.log(JSON.parse(body).name);
      i++;
      Characters(i, charList[i], charList, limit);
    }
  });
}
