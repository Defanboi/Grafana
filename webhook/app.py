
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_API_URL = 'https://api.telegram.org/bot<7357155982:AAFSYlZyi2-_-pPuc3hDrUaIgn9TI9Yfi0Y'
CHAT_ID = '<6840362427>'

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    message = f"Alert: {data['alerts'][0]['annotations']['summary']}"
    requests.post(TELEGRAM_API_URL, json={'chat_id': CHAT_ID, 'text': message})
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
