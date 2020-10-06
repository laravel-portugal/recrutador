from abc import ABCMeta, abstractmethod
from Job import Job
from typing import List


class JobsInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> List[Job]:
        pass

    @abstractmethod
    def persistPublished(self, job: Job):
        pass
