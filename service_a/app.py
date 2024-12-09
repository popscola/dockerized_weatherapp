from flask import Flask, render_template, request
from weather import main as get_weather


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form.get('cityName')
        state = request.form.get('stateName', 'ON') 
        country = request.form.get('countryName', 'Canada')  
        data = get_weather(city, state, country)

    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)
