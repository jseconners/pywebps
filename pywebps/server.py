import os
import utils
import json
from flask import Flask, abort, request

import pandas as pd

app = Flask(__name__)

from plots import timeseries

available_plots = {
    'timeseries': timeseries
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
            abort(404)

        data = pd.DataFrame(config_obj['data'])
        fig = available_plots[plot].plot(data)

        return utils.send_fig(fig)


    else:
        abort(404)
