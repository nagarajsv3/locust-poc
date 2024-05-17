import time
from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1,1)

    @task
    def root_api(self):
        self.client.get(url="/")

    @task
    def hello_api(self):
        self.client.get(url="/hello")

    @task
    def slow_api(self):
        self.client.get(url="/slow")
