import os
import utils
from flask import Flask, abort

app = Flask(__name__)

from plots import timeseries

available_plots = {
    'timeseries': timeseries
}


@app.route('/')
def welcome():
    return "Welcome"


@app.route('/<plot>', methods=['GET', 'POST'])
def plot(plot):
    if (plot in available_plots):
        fig = available_plots[plot].plot()
        return utils.send_fig(fig)
    else:
        abort(404)
