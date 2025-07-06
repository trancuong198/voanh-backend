from flask import Flask, request
import os
import requests

app = Flask(__name__)

"Authorization": f"Bearer {NOTION_TOKEN}",
...
"parent": { "database_id": DATABASE_ID },


@app.route('/')
def home():
    return "✅ Vô Ảnh Backend đã hoạt động!"

@app.route('/log')
def log_to_notion():
    text = request.args.get("text", "No text provided")

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Name": {
                "title": [{
                    "text": { "content": text }
                }]
            }
        }
    }

    response = requests.post(url, json=data, headers=headers)
    return f"✅ Sent to Notion: {response.status_code}"
