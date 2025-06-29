from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Это интеллектуальная система."

if __name__ == '__main__':
    app.run(debug=True)
