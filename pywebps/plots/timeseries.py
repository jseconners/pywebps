import matplotlib.pyplot as plt
import numpy as np



def plot(df):
    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure() and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()

    ax.scatter(df['temp'], df['salinity'])
    return fig
