from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/start_assistant', methods=['POST'])
def start_assistant():
    return jsonify({'message': 'Assistant started'})

@app.route('/stop_assistant', methods=['POST'])
def stop_assistant():
    return jsonify({'message': 'Assistant stopped'})


@app.route('/static/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except FileNotFoundError:
        return jsonify({"error": "Static file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
