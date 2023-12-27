from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Your ML model and functions will go here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
