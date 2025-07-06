from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Vô Ảnh Backend đã hoạt động!"

if __name__ == '__main__':
    app.run()
