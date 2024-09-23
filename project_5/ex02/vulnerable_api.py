#!/usr/bin/venv python3

from flask import Flask, jsonify

app = Flask(__name__)

#Broken Object Property Level Authorization
#Sending profile owner sensible information
users_db = {
    1: {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'password': 'hashed_password',
        'credit_card': '1234-5678-9012-3456'
    },
    2: {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'password': 'hashed_password_2',
        'credit_card': '6543-2109-8765-4321'
    }
}

@app.route('/see_profile/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

#Security Misconfiguration
#convarsetion most set Cache-Control header as no-store
@app.route('/dm/conversation')
def get_user_updates():
    response = jsonify({
        'conversation_id': 1234567,
        'messages': [
            {'from': 'Alice', 'message': 'Olá, tudo bem?'},
            {'from': 'Bob', 'message': 'Tudo ótimo, e você?'}
        ]
    })

    return response

if __name__ == '__main__':
    app.run(debug=True)

