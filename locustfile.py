from locust import HttpUser, task, between
class WebsiteUser(HttpUser) :
    wait_time = between(1, 5)
    @task
    def get_users(self) :
        self.client.get("/users")