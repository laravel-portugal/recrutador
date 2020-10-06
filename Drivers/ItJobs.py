import os
import requests
from dotenv import load_dotenv, set_key
from typing import List
from math import ceil


from Drivers.Job import Job
from Drivers.DriverInterface import DriverInterface


class ItJobs(DriverInterface):
    search = ""
    api_key = ""
    url = ""
    last_published_id = 0

    def __init__(self):
        load_dotenv()

        self.search = os.getenv('ITJOBS_SEARCH')
        self.url = 'http://api.itjobs.pt/job/search.json'
        self.api_key = os.getenv('ITJOBS_API')
        self.last_published_id = int(os.getenv('ITJOBS_LASTPUBLISHEDID'))

    def get(self) -> List[Job]:
        limit = 100
        payload = {'api_key': self.api_key, 'q': self.search, 'limit': 1}
        r = requests.get(self.url, payload)
        total = r.json()['total']
        if (total == 0):
            return []
        pages = ceil(total/limit,)
        currentJobs = []
        for page in range(1, pages + 1):
            payload = {'api_key': self.api_key,
                       'q': self.search, 'limit': limit, 'page': page}
            currentJobs = currentJobs + \
                requests.get(self.url, payload).json()['results']
        currentJobs = list(sorted(currentJobs, key=lambda j: j['id']))
        currentJobs = list(
            filter(lambda j: self.__filterUnpublished(j['id']), currentJobs))

        unpublishedJobs: List[Job] = []
        for j in currentJobs:
            unpublishedJobs.append(Job(j['id'], self.__getJobUrl(j)))
        return unpublishedJobs

    def __filterUnpublished(self, id: int) -> bool:
        return id > self.last_published_id

    def __getJobUrl(self, job) -> str:
        return 'https://www.itjobs.pt/oferta/' + str(job['id']) + '/' + job['slug']

    def persistPublished(self, job: Job):
        if job.identifier > self.last_published_id:
            self.last_published_id = job.identifier
            print('Persisting ITJOBS_LASTPUBLISHEDID==' + str(job.identifier))
            set_key(os.path.join(os.path.dirname(os.path.realpath(
                __file__)), '.env'), 'ITJOBS_LASTPUBLISHEDID', str(job.identifier))
