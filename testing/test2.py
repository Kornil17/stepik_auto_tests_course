import requests
from src.pydantic_schemas.computers import *
SERVICE_URL = 'https://my-json-server.typicode.com/typicode/demo/posts'
from src.enums.global_enums import GlobalErrorMessages
from jsonschema import validate
from src.schemas.posts import POST_SCHEMAS
# from src.pydantic_schemas.posts import Post
# def test_getting_posts():
#     response = requests.get(url=SERVICE_URL)
#     recived_posts = response.json()
#
#     assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
#     assert len(recived_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT
#     for post in recived_posts:
#         validate(post, POST_SCHEMAS)

def test_validate():
    comp = Computer.model_validate(computer)
    print(comp.detailed_info.physical.color.as_hex())
    print(comp.detailed_info.owners[0].card_number)
    assert type(comp.detailed_info.owners) == list and comp.detailed_info.owners[0].card_number == '5555555555554444'





