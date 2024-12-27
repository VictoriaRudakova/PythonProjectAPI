from enum import Enum


class StatusCode(Enum):
    OK = 200
    CREATED = 201
    NOCONTENT = 204
    NOTFOUND = 404
