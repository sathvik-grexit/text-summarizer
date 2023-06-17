import requests

class ClickUp:
    def __init__(self) -> None:
        CLICKUP_TOKEN = "YOUR_API_TOKEN"
        self.base_url = "https://api.clickup.com/api/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": CLICKUP_TOKEN
        }
        self.query = {
            "custom_task_ids": False,
            "team_id": "3698397"
        }

    def create_task(self, payload:dict) -> dict:
        
        list_id = 5521841
        url = f"{self.base_url}/list/{list_id}/task"
        try:
            response = requests.post(url, json=payload, headers=self.headers, params=self.query)
            data = response.json()
            return data
        except Exception as err:
            print("Exception while creating a new task", err)
            raise err
