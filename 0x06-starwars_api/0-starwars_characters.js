#!/usr/bin/node
// using request module in Node.js to fetch data from starWars API.



const request = require('request');

function fetchCharacters(movieID){
    const movieURL = 'https://swapi-api.alx-tools.com/api/';

    request(movieURL, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const charactersUrls = movieData.characters;

            charactersUrls.forEach(characterUrl => {
                request(characterUrl, (error, response, body) => {
                    if (!error && response.statusCode === 200) {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                    } else {
                        console.log('Error fetching character details:', error);
                    }
                });
            });
        } else {
            console.log('Error fetching movie details:', error);
        }
    });
}
