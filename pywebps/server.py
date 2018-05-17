import os
import utils
import json
from flask import Flask, abort, request

import pandas as pd

app = Flask(__name__)

# import plots
from plots import timeseries, scatter

# map available plot names to modules
available_plots = {
    'timeseries': timeseries,
    'scatter': scatter
}


@app.route('/')
def welcome():
    return "Welcome"


@app.route('/<plot>', methods=['POST'])
def plot(plot):
    if (plot in available_plots):
        try:
            config_obj = json.loads(request.data)
        except:
            abort(400)

        # get plot figure
        fig = available_plots[plot].plot(config_obj)

        return utils.send_fig(fig)


    else:
        abort(404)
