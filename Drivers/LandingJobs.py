import os
import requests
from dotenv import load_dotenv, set_key
from typing import List

from Drivers.Job import Job
from Drivers.DriverInterface import DriverInterface


class LandingJobs(DriverInterface):
    tags = []
    url = ""
    last_published_id = 0

    def __init__(self):
        load_dotenv()
        self.tags = os.getenv('LANDINGJOBS_TAGS').split(',')
        self.url = 'https://landing.jobs/api/v1/jobs'
        self.last_published_id = int(os.getenv('LANDINGJOBS_LASTPUBLISHEDID'))

    def get(self) -> List[Job]:
        limit = 50
        offset = 0
        currentJobs = []
        for offset in range(0, 1000, limit):
            payload = {'limit': limit, 'offset': offset}
            r = requests.get(self.url, payload)
            if len(r.json()) == 0:
                break
            currentJobs = currentJobs + r.json()

        currentJobs = list(sorted(currentJobs, key=lambda j: j['id']))
        currentJobs = list(
            filter(lambda j: self.__filterByTags(j['tags']), currentJobs))
        currentJobs = list(
            filter(lambda j: self.__filterUnpublished(j['id']), currentJobs))

        unpublishedJobs: List[Job] = []
        for j in currentJobs:
            unpublishedJobs.append(Job(j['id'], j['url']))
        return unpublishedJobs

    def __filterByTags(self, tags: list) -> bool:
        for tag in self.tags:
            if (tag in tags):
                return True
        return False

    def __filterUnpublished(self, id: int) -> bool:
        return id > self.last_published_id

    def persistPublished(self, job: Job):
        if job.identifier > self.last_published_id:
            self.last_published_id = job.identifier
            print('Persisting LANDINGJOBS_LASTPUBLISHEDID==' + str(job.identifier))
            set_key(os.path.join(os.path.dirname(os.path.realpath(
                __file__)), '.env'), 'LANDINGJOBS_LASTPUBLISHEDID', str(job.identifier))
