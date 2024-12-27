from datetime import datetime


class Logger:
    def __init__(self):
        now = datetime.now()
        self.current_time = now.strftime("%d/%m/%Y - %H:%M:%S")

    def custom_log(self, message):
        print("--------------------------------------------------")
        print(f"[{self.current_time}] --- {message}")
        print("--------------------------------------------------")

    def request_log(self, url='not specified', method='not specified', body={}, httpcode=0):
        print("--------------------------------------------------")
        print(f"[{self.current_time}] --- {method} --- {url}")
        print(f"{httpcode} --- status code")
        print(body)
        print("--------------------------------------------------")

    def start_test_log(self):
        print("--------------------------------------------------")
        print(f"[{self.current_time}] --- TEST STARTED")
        print("--------------------------------------------------")

    def finish_test_log(self):
        print("--------------------------------------------------")
        print(f"[{self.current_time}] --- TEST FINISHED")
        print("--------------------------------------------------")

    def pay_attention(self, message):
        print("--------------------------------------------------")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"[{self.current_time}] --- {message}")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("--------------------------------------------------")
