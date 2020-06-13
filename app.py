import random
from flask import Flask, render_template
# Импортируем данные для передачи их в шаблон
import data

app = Flask(__name__)

@app.route('/')
def render_index():
    # Отбираем рандомные 6 туров из нашего обшего перечня
    d = data.tours.keys()
    random.seed()
    keys = random.sample(list(d), 6)
    tour_dict = {k: data.tours[k] for k in keys}
    return render_template('index.html', tours=tour_dict, dep=data.departures)


@app.route('/departure/<departure>')
def render_departure(departure):
    dep_dict = {k: data.tours[k] for k, v in data.tours.items() if v['departure'] == departure}
    return render_template('departure.html', tours=dep_dict, dep=data.departures, cur_dep = departure)


@app.route('/tour/<int:id>/')
def render_tour(id):
    cur_tour = data.tours[id]
    return render_template('tour.html', tour=cur_tour, dep=data.departures)

if __name__ == '__main__':
    app.run('0.0.0.0',8000)