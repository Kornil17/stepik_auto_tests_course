from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = "Number of items isn't equal to expected"

class Statuses(Enum):
    ACTIVE = 'ACTIVE'
    BANNED = 'BANNED'
    DELETED = 'DELETED'
    INACTIVE = 'INACTIVE'

# print(str(Statuses.ACTIVE))
# print(Statuses.ACTIVE.name)
# print(Statuses.ACTIVE.value)
# print(Statuses.ACTIVE)
# print(Statuses('ACTIVE'))