class Job:
    identifier: str = ""
    url: str = ""

    def __init__(self, identifier: int, url: str):
        self.identifier = identifier
        self.url = url
