from abc import ABCMeta, abstractmethod
from typing import List
from pathlib import Path
import os

from Drivers.Job import Job


class DriverInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> List[Job]:
        pass

    @abstractmethod
    def persistPublished(self, job: Job):
        pass

    def getEnvFilePath(self) -> str:
        p = Path(os.path.dirname(os.path.realpath(__file__)))
        return os.path.join(p.parent, '.env')
