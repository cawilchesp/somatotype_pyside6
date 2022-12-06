"""
Matplotlib canvas component for plotting signals


"""

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


light = {
    'background': '#3785F5',
    'on_background': '#000000',
    'surface': '#FFFFFF',
    'on_surface': '#000000',
    'primary': '#3785F5',
    'on_primary': '#000000',
    'secondary': '#7FB0F5',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'on_disable': '#000000',
    'error': '#B3261E',
    'on_error': '#FFB4AB'
}

dark = {
    'background': '#3B4253',
    'on_background': '#E5E9F0',
    'surface': '#2E3441',
    'on_surface': '#E5E9F0',
    'primary': '#7FB0F5',
    'on_primary': '#000000',
    'secondary': '#3785F5',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'on_disable': '#000000',
    'error': 'B3261E',
    'on_error': '#FFB4AB'
}


class MPLCanvas(FigureCanvasQTAgg):
    def __init__(self, parent, theme: bool) -> None:
        """ Canvas settings for plotting signals """
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        self.apply_styleSheet(theme)

    def apply_styleSheet(self, theme):
        self.fig.subplots_adjust(left=0.05, bottom=0.15, right=1, top=0.95, wspace=0, hspace=0)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        if theme:
            self.fig.set_facecolor(f'{light["surface"]}')
            self.axes.set_facecolor(f'{light["surface"]}')
            self.axes.xaxis.label.set_color(f'{light["on_surface"]}')
            self.axes.yaxis.label.set_color(f'{light["on_surface"]}')
            self.axes.tick_params(axis='both', colors=f'{light["on_surface"]}', labelsize=8)
        else:
            self.fig.set_facecolor(f'{dark["surface"]}')
            self.axes.set_facecolor(f'{dark["surface"]}')
            self.axes.xaxis.label.set_color(f'{dark["on_surface"]}')
            self.axes.yaxis.label.set_color(f'{dark["on_surface"]}')
            self.axes.tick_params(axis='both', colors=f'{dark["on_surface"]}', labelsize=8)

    def language_text(self, language: int) -> None:
        """ Change language of switch text """
        return 0


