from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to receive data
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    print("Received data:", data)

    # Process or store data as needed (e.g., save to database)
    
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run Flask on all network interfaces
