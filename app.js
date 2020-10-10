//get environment variables from .env
require('dotenv').config()

const Discord = require('discord.js');

//create a new discord client
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    if (msg.content === 'ping') {
        msg.reply('pong');
    }
});

//login with token from .env
client.login(process.env.TOKEN);