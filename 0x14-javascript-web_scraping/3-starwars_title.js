#!/usr/bin/node
const request = require('request');
const { argv } = process;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request.get(url, { json: true }, (err, response, body) => {
  if (err) console.log(err);
  else if (response && response.statusCode === 200) console.log(body.title);
});
