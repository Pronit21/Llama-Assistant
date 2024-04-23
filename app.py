from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Route to serve static files (CSS, JavaScript, images, etc.)
@app.route('/static/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('static', path)
    except FileNotFoundError:
        return jsonify({"error": "Static file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
