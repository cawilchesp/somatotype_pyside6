"""
Matplotlib canvas component for plotting signals


"""

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from components.style_color import colors

# -----------------
# MatPlotLib Canvas
# -----------------
class MPLCanvas(FigureCanvasQTAgg):
    def __init__(self, parent, attributes: dict) -> None:
        """ Canvas settings for plotting signals """

        self.attributes = attributes
        self.parent = parent

        self.fig = Figure(constrained_layout=True)
        self.axes = self.fig.add_subplot(111)

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 96)
        self.setGeometry(x, y, w, h)
        
        self.setThemeStyle(attributes['theme'])


    def setThemeStyle(self, theme):
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        
        self.fig.set_facecolor(f'{background_color}')
        self.axes.set_facecolor(f'{background_color}')
        self.axes.xaxis.label.set_color(f'{color}')
        self.axes.yaxis.label.set_color(f'{color}')
        self.axes.tick_params(axis='both', colors=f'{color}', labelsize=8)
