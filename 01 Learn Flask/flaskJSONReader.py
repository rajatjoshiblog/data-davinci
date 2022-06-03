from flask import Flask, request
app = Flask(__name__)
@app.route('/post_json', methods=['POST'])
def process_json():
    # HTTP(S) requests have a parameter call headers
    # If a POST request is sent to a URL
    # then the url may contain some data (like a JSON)
    # and content_type header param tells the API what 
    # kind of data to expect (like 'application/json' for JSON data)
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        payload = request.json # payload from the curl request
        return f"Hello {payload['firstName']} {payload['lastName']}"
    else:
        return 'Content-Type not supported!'