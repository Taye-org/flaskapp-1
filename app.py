from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def progress():
    name = os.getenv('USER_NAME', 'Taye')
    current_step = 1
    total_steps = 3
    message = f"Hey {name}, welcome to your first app deployment!"
    next_up = "flask-app-2 is waiting for you 💪"

    return jsonify({
        "step": current_step,
        "total": total_steps,
        "user": name,
        "message": message,
        "next": next_up
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


 
