from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_index():
    if request.method == 'POST':
        city = request['city']
        return render_template('city.html', city=city)
    else:
        return render_template('index.html')
