from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    data = request.json  # Retrieve JSON data from the POST request
    print("Received JSON:", data)
    # Process the JSON data here as needed
    return 'JSON received successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run Flask app on port 5000