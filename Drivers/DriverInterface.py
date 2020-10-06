from abc import ABCMeta, abstractmethod
from typing import List

from Drivers.Job import Job


class DriverInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> List[Job]:
        pass

    @abstractmethod
    def persistPublished(self, job: Job):
        pass
