class CreateUser:
    response = {
    "name": "morpheus",
    "job": "leader"
}

    def set_body(self,
                 user_name='morpheus',
                 user_job='leader'
                 ):

      self.response['name'] = user_name
      self.response['job'] = user_job



      return self.response