from flask import Flask, render_template, request, jsonify

app = Flask(__name___)

# Your ML model and functions will go here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])


def get_data(response):
    # Assuming response is an HTTP response object
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)