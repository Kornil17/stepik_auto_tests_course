from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color

from src.enums.global_enums import Statuses
import testing

class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr
class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


computer = {
  "status": "ACTIVE",
  "activated_at": "2023-04-15",
  "expiration_at": "2027-10-13",
  "host_v4": "91.222.191.20",
  "host_v6": "2001:0db8:85a3:0000:0000:8a2b:8360:1232",
  "detailed_info": {
    "physical": {
      "color": "blue",
      "photo": "https://youtube.com",
      "uuid": "550e8400-e29b-41d4-a716-446655440000"
    },
    "owners": [
      {
        "name": "Falka User",
        "card_number": "5555555555554444",
        "email": "test@mail.com"
      }
    ]
  }
}

comp = Computer.model_validate(computer)
# print(comp)