const Blooket = require('blooket')

const client = new Blooket();

client.floodGames('6816274', 100);

client.on('flood', data => {
    console.log('Joined game with name: ' + data.player);
});