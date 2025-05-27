import PySimpleGUI as sg
import datetime as dt
import math
from os import path
import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import FuncFormatter

matplotlib.use('TkAgg')


def draw_figure(canvas, figure):
    """Draw a figure in canvas for PySimpleGUI"""
    fca = FigureCanvasTkAgg(figure, canvas)
    fca.draw()
    fca.get_tk_widget().pack(side='top', fill='both', expand=1)
    return fca


def format_x(n, pos):
    """Format representation of xticks with hours:minutes:seconds"""
    t = dt.datetime.fromtimestamp(n)
    return t.strftime("%H:%M:%S")


def format_y(n, pos):
    """Format representation of yticks with K,M metric prefixes"""
    if n >= 1e6:
        return '%1.0fM' % (n * 1e-6)
    if n >= 1e3:
        return '%1.0fK' % (n * 1e-3)
    return '%1.0f' % n


def gui(data):
    """Plot data and embed the figure in PySimpleGUI"""

    cols = 3
    rowspan = 2
    hsmooth = 3.0

    rows = math.ceil(len(data) / cols) + rowspan

    width = 13.0
    height = hsmooth * rows

    plt.figure(1)

    i = 1
    for k in sorted(data):
        plt.subplot(rows, cols, i)
        y = data[k]['load']
        x = data[k]['time']
        plt.plot(x, y)
        plt.title(k)
        plt.ylabel('bits/s')
        ax = plt.gca()
        ax.xaxis.set_major_formatter(FuncFormatter(format_x))
        ax.yaxis.set_major_formatter(FuncFormatter(format_y))
        plt.setp(ax.get_xticklabels(), rotation=30,horizontalalignment='right')
        i += 1

    fig = plt.gcf()
    fig.set_size_inches(width, height)
    fig.tight_layout()

    # pdp = path.join(path.dirname(__file__), 'plot.pdf')
    # pdp = path.abspath(pdp)
    # pp = PdfPages(pdp)
    # pp.savefig()
    # pp.close()

    layout = [
        [
            sg.Column([[sg.Canvas(key='-C1-')]],key='-COL1-',
                      scrollable=True,vertical_scroll_only=True)
        ],
    ]
    window = sg.Window('Mininet Attack Test',layout,finalize=True, resizable=True,
                       element_justification='center',font='Helvetica 18', keep_on_top=True, size=(800, 600))
    draw_figure(window['-C1-'].TKCanvas, fig)
    window['-COL1-'].expand(True, True)
    window.read()
    window.close()
