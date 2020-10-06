import os
import discord
from time import sleep
from typing import List
from dotenv import load_dotenv, set_key


from Job import Job
from JobsInterface import JobsInterface

from LandingJobs import LandingJobs
from ItJobs import ItJobs
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNELID = int(os.getenv('CHANNELID'))
FETCHINTERVAL = int(os.getenv('FETCHINTERVAL'))


class DiscordClient(discord.Client):
    token = ""
    channel_id = 0
    fetch_interval = 0
    drivers: List[JobsInterface] = []

    def __init__(self, token: str, channel_id: int, fetch_interval: int):
        super().__init__()
        self.token = token
        self.channel_id = channel_id
        self.fetch_interval = fetch_interval

    async def on_ready(self):
        print('Hello i\'am Bot for Landing Jobs', self.user)
        while True:
            for driver in self.drivers:
                jobs: List[Job] = driver.get()
                for job in jobs:
                    print('Sending message for job id:' + str(job.identifier))
                    await self.sendMessage(job)
                    driver.persistPublished(job)

            sleep(self.fetch_interval)

    async def sendMessage(self, job: Job):
        channel = self.get_channel(self.channel_id)
        await channel.send(job.url)

    def registerDriver(self, driver: JobsInterface):
        self.drivers.append(driver)


client = DiscordClient(TOKEN, CHANNELID, FETCHINTERVAL)
client.registerDriver(ItJobs())
client.registerDriver(LandingJobs())
client.run(TOKEN)
