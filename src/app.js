//get environment variables from .env
require('dotenv').config()
const Discord = require('discord.js');
const sleep = require('./sleep');
const LandingJobs = require('./drivers/LandingJobs');


//create a new discord client
const client = new Discord.Client();

/**
 * called when client is ready
 */
client.on('ready', async () => {
    console.log(`Ready to process jobs!`);
    do {
        await processJobs()
    } while (true);
});

//called when a error occurs in discord client
client.on('shardError', error => {
    console.error('A websocket connection encountered an error:', error);
    console.log('Restarting script');
    client.destroy()
    client.login(process.env.TOKEN);
});

/**
 * iterates drivers array and posts jobs on the specified channel
 * @returns {void}
 */
async function processJobs() {
    try {
        for (let index = 0; index < drivers.length; index++) {

            //awaits jobs from api
            let jobs = await drivers[index].getJobs();

            for (let jobIndex = 0; jobIndex < jobs.length; jobIndex++) {

                //get the channel
                const channel = client.channels.cache.get(process.env.CHANNELID);

                //logs the job url
                console.info("Sending job url: " + jobs[jobIndex].url)

                //awaits publishing job
                await channel.send(jobs[jobIndex].url)

                //stores the job in config file
                drivers[index].storePublishedJob(jobs[jobIndex])
            }
        }
        //pauses execution 
        console.info("Sleeping for " + parseInt(process.env.FETCHINTERVAL) * 1000)
        await sleep(parseInt(process.env.FETCHINTERVAL) * 1000)


    } catch (error) {
        console.error("processJobs -> error", error)
    }

}


//register each driver
//itJobs missing
const drivers = [new LandingJobs()]

//login with token from .env
client.login(process.env.TOKEN);