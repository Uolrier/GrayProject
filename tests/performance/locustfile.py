from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def chat(self):
        self.client.post(
            "/chat/stream",
            json={"message": "hello"},
            timeout=30,
        )
