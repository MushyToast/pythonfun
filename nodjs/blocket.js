const axios = require('axios');
const Blooket = require('blooket')

const client = new Blooket();

client.joinGame("6816274", "JuandalePringle")

client.on('flood', data => {
    console.log('Joined game with name: ' + data.player);
});