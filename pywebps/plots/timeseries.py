import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd


def plot(config):

    data_url = config['data']
    plot_cfg = config['config']

    x = plot_cfg['x']
    y = plot_cfg['y']

    # gather date and time
    # date required, time optional
    date_cols = [x['date']]
    if 'time' in x:
        date_cols.append(x['time'])

    # get data lines
    y_cols = []
    y_lbls = []
    for c in y:
        y_cols.append(c['col'])
        y_lbls.append(c['label'])

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure() and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots(figsize=plot_cfg['size'])

    #read data from csv
    data = pd.read_csv(data_url, usecols=date_cols + y_cols, parse_dates={'datetime' : date_cols})

    #set date as index
    data.set_index(data['datetime'], inplace=True)
    del data['datetime']

    #plot data
    data.plot(ax=ax, subplots=True)

    #ax.set_xlabel(x['label'])
    ax.legend(y_lbls)

    plt.tight_layout()

    return fig
