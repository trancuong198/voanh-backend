from flask import Flask, request
import os
import requests

app = Flask(__name__)

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

@app.route('/')
def home():
    return "⭕ Vô Ảnh Backend đã hoạt động!"

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
                "title": [
                    {
                        "text": {
                            "content": "Log Entry"
                        }
                    }
                ]
            },
            "log": {
                "rich_text": [
                    {
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(url, json=data, headers=headers)
    return f"✅ Đã gửi đến Notion: {response.status_code}"
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notion-webhook', methods=['POST'])
def notion_webhook():
    data = request.json
    
    # 👇 Nếu là yêu cầu xác minh (verify)
    if 'verification_token' in data:
        print("👉 Token xác minh nhận được:", data['verification_token'])
        return jsonify({'verification_token': data['verification_token']}), 200

# ✅ Nếu là sự kiện bình thường (cập nhật nội dung...)
import json
print("🌀 Dữ liệu sự kiện nhận được:\n", json.dumps(data, indent=2))
return '', 200
