class UpdateUser:
    response = {
    "name": "morpheus",
    "job": "zion resident"
}

    def set_body(self,
                 user_name='morpheus',
                 user_job='zion resident'
                 ):

      self.response['name'] = user_name
      self.response['job'] = user_job



      return self.response