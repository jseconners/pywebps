import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd


def plot(config):

    data_url = config['data']
    plot_cfg = config['config']

    x = plot_cfg['x']
    y = plot_cfg['y']

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure() and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots(figsize=plot_cfg['size'])

    #read data from csv
    data = pd.read_csv(data_url, usecols=[x['col'], y['col']])

    #plot data
    data.plot(ax=ax, x=x['col'], y=y['col'], kind='scatter', fontsize=9)

    if x.get('invert'):
        ax.invert_xaxis()

    if y.get('invert'):
        ax.invert_yaxis()

    ax.set_xlabel(x['label'])
    ax.set_ylabel(y['label'])

    plt.tight_layout()

    return fig
