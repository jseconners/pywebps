import os
from io import BytesIO
from flask import send_file



def send_fig(fig, img_format='png'):
    '''
    Returns saved figure image data
    '''
    imgdata = BytesIO()

    fig.savefig(imgdata, format=img_format)
    imgdata.seek(0)

    return send_file(
        imgdata,
        mimetype='image/{}'.format(img_format)
    )
