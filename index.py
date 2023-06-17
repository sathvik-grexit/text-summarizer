import requests
from click_up import ClickUp

clickup = ClickUp()

API_TOKEN = "<YOUR_API_KEY>"
API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	res = response.json()
	summary = ""
	for i in res:
		summary += i["summary_text"]
	return summary
		

if __name__ == "__main__":
    output = query({
        "inputs": ["Visitor says - I am having trouble with automations not working as intended.",
            "Agent says - Hi, I am Saleena from Hiver Support. I will be assisting you today.", "Visitor says - Hi Saleena",
            "Agent says - I will certainly help you with this. Could you please share the message-id along with the automation name that was supposed to work ?",
            "Agent says - Steps to provide message-id: 1. Open the message in your Gmail inbox. Click the three dots in the top-right corner of the message. 2. Click the 'Show original' link toward the bottom of the options box. The message will open in a separate window with the full message headers at the top. 3. Copy the message-id(green) from the top of the page and send it across to me.",
            "Visitor says - sure",
            "Agent says - Thank you very much :)",
            "Visitor says - <CANeK0r1Whj0RE6-xsWVPjJhb=kBt5ZAFA3yFF_cQRQRVrc8tSg@mail.gmail.com>",
            "Visitor says - Automation = URGENT VOICE/URGENT",
            "Agent says - Thank you, please allow me 3-4 minutes to check this",
            "Visitor says - OK",
            "Agent says - Josh the automation should have triggered over here. Let me escalate it to my engineering team for more clarification. Will keep you posted via email",
            "Visitor says - Sounds good. Thank you!",
            "Agent says - You are most welcome Josh ! Have a lovely weekend"
        ]
    })

    task_res = clickup.create_task({
        "name": "Automation Issue",
        "description": f"Agent: Basit Rehman \n\
            Affected User: Byron Sanders (info@seselectricalcontractors.co.uk) \n\
            UGID: 289793 \n\
            SMID: 75698 \n\
            Summary: {output}\
	    ",
        "status": "With L2",
        "priority": 3,
        "tags": [
            "CART"
        ]
    })

    print(f"https://app.clickup.com/t/{task_res['id']}")