from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = 'https://jsonplaceholder.typicode.com'

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/users')
def get_all_users():
    response = requests.get(f'{BASE_URL}/users')
    users = response.json()
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    user = response.json()
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
