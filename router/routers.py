from configuration.get_config import get_config


class ReqresRouterMaker:
    route = ''
    config = get_config()
    Reqres_API_HOST = config['request']['baseUrl']


    def reqres_route(self):
        self.route = f"{self.Reqres_API_HOST}/users"
        return self.route

    def reqres_route_id(self, user_id):
        self.route = f"{self.Reqres_API_HOST}/users/{user_id}"
        return self.route

