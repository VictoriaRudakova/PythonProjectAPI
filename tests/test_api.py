import pytest
import requests
from router.routers import ReqresRouterMaker
from faker import Faker


from json_builder.create_user import CreateUser
from make_requests.make_requests import HttpRequest

from logger.logger import Logger

fake = Faker()

@pytest.mark.smoke
### create user ###
def test_create_user():
    print(help(test_create_user))
    user_name = fake.first_name()
    user_job = fake.last_name()
    url = ReqresRouterMaker().reqres_route()
    body = CreateUser().set_body(user_name=user_name,user_job=user_job)
    create_user = HttpRequest().make_post(url=url, body=body)
    user_id  = create_user['id']
    print(user_id)

### update user ###

    user_name = fake.first_name()
    user_job = fake.last_name()
    url = ReqresRouterMaker().reqres_route_id(user_id=user_id)
    body = CreateUser().set_body(user_name=user_name,user_job=user_job)
    update_user = HttpRequest().make_put(url=url, body=body)

### delete user ###
    url = ReqresRouterMaker().reqres_route_id(user_id=user_id)
    delete_user = HttpRequest().make_delete(url=url)
    r = requests.get(url=url)