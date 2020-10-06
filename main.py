import os
import sys
import discord
from time import sleep
from typing import List
from dotenv import load_dotenv, set_key

from Drivers.Job import Job
from Drivers.DriverInterface import DriverInterface
from Drivers.ItJobs import ItJobs
from Drivers.LandingJobs import LandingJobs

TOKEN = None
CHANNELID = None
FETCHINTERVAL = None
DRYRUN = False


class DiscordClient(discord.Client):
    token = ""
    dryrun = False
    channel_id = 0
    fetch_interval = 0
    drivers: List[DriverInterface] = []

    def __init__(self, token: str, channel_id: int, fetch_interval: int, dryrun: bool = False):
        super().__init__()
        self.token = token
        self.channel_id = channel_id
        self.fetch_interval = fetch_interval
        self.dryrun = dryrun

    async def on_ready(self):
        print('Hello i\'am Bot for Landing Jobs', self.user)
        while True:
            for driver in self.drivers:
                jobs: List[Job] = driver.get()
                for job in jobs:
                    try:
                        print('Sending message for job id:' +
                              str(job.identifier))
                        if not self.dryrun:
                            await self.sendMessage(job)
                        driver.persistPublished(job)
                    except:
                        print("An error ocorred, closing bot...")
                        print(sys.exc_info()[0])
                        await self.close()
                        return

            print("Sleeping for " + str(self.fetch_interval) + ' seconds...')
            sleep(self.fetch_interval)

    async def sendMessage(self, job: Job):
        channel = self.get_channel(self.channel_id)
        await channel.send(job.url)

    def registerDriver(self, driver: DriverInterface):
        self.drivers.append(driver)


def main():
    try:
        client = DiscordClient(TOKEN, CHANNELID, FETCHINTERVAL, DRYRUN)
        print("Starting bot ...")
        client.registerDriver(ItJobs())
        client.registerDriver(LandingJobs())
        client.run(TOKEN)
    except:
        print("An error ocorred ...")
        print(sys.exc_info()[0])


def fetchConfig() -> bool:
    global TOKEN
    global CHANNELID
    global FETCHINTERVAL
    global DRYRUN
    try:
        load_dotenv()
        TOKEN = os.getenv('TOKEN')
        CHANNELID = int(os.getenv('CHANNELID'))
        FETCHINTERVAL = int(os.getenv('FETCHINTERVAL'))
        DRYRUN = '--dry' in sys.argv
        if TOKEN == None or CHANNELID == None or FETCHINTERVAL == None:
            return False
        return True
    except:
        print("An error ocorred fetching config...")
        print(sys.exc_info()[0])


while True:

    if fetchConfig():
        main()
    print("Restarting " + str(FETCHINTERVAL) + ' seconds...')
    sleep(FETCHINTERVAL)
    python = sys.executable
    os.execl(python, python, *sys.argv)
