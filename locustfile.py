from locust import HttpUser, task


class MyLocust(HttpUser):

    x_token = None

    def on_start(self):
        res = self.client.get("/login")
        res_body = res.json()
        print(res_body)
        self.x_token = res_body["x_token"]

    @task
    def get_users(self):
        self.client.get("/users", headers={"x-token": self.x_token})
