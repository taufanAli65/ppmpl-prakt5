from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # Tes GET semua pengguna
    @task(1)
    def get_users(self):
        self.client.get("/users")
        
    # Tes GET pengguna berdasarkan ID
    @task(2)
    def get_user_by_id(self):
        user_id = 1  # ID yang ingin diambil
        self.client.get(f"/users/{user_id}")

    # Tes POST untuk menambahkan pengguna baru
    @task(3)
    def create_user(self):
        user_data = {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        self.client.post("/users", json=user_data)

    # Tes PUT untuk memperbarui data pengguna
    @task(4)
    def update_user(self):
        user_data = {
            "id": 1,
            "name": "John Doe Updated",
            "email": "john.doe.updated@example.com"
        }
        self.client.put("/users/1", json=user_data)

    # Tes DELETE untuk menghapus pengguna
    @task(5)
    def delete_user(self):
        self.client.delete("/users/1")