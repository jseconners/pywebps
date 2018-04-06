import os
from io import BytesIO
from flask import Flask, send_file
app = Flask(__name__)

from plots import testplot

def return_fig(fig):
    imgdata = BytesIO()

    fig.savefig(imgdata, format='png')
    imgdata.seek(0)

    return send_file(
        imgdata,
        mimetype='image/png'
    )


@app.route("/")
def home():
    fig = testplot.plot()
    return return_fig(fig)
