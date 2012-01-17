# -*- coding: utf-8 -*-
from urllib import urlencode

BOOLEAN_MAP = {
    True: "true",
    False: "false"
}

class Pencil(object):
    def __init__(self, begin=None, until=None):
        """Creates a Pencil object, specifying *optionally* a date range ::

            pencil = Pencil(begin="-1hours")

        """
        self._from = begin
        self._until = until
        self._title = None
        self._vtitle = None
        self._target = []
        self._colorList = ""
        self._bgcolor = "FFFFFF"
        self._fgcolor = "000000"
        self._fontName = "Helvetica"
        self._areaMode = "none"
        self._lineMode = "slope"
        self._hideLegend = "false"
        self._hideAxes = "false"
        self._template = "alphas"
        self._yMin = None
        self._yMax = None
        self._lineWidth = None
        self._graphType = "line"
        self._format = None

    def begin(self, value):
        self._from = value
        return self

    def until(self, value):
        self._until = value
        return self

    def y_min(self, value):
        """yMin set the minimum y value for the generated image"""
        self._yMin = value
        return self

    def y_max(self, value):
        """yMax set the maximun y-value for the generated image"""
        self._yMax = value
        return self

    def line_width(self, value):
        """
        Sets the line thickness, by default this is set depending
        on the size of the image
        """
        self._lineWidth = value
        return self

    def set_title(self, title):
        """Set the image title"""
        self._title = title
        return self

    def set_vtitle(self, title):
        """Set the image vertical title"""
        self._vtitle = title
        return self

    def set_fgcolor(self, color):
        """
        Set font color

        **Default :** black
        """
        self._fgcolor = color
        return self

    def hide_legend(self, boolean):
        """Hides the graph legend"""
        self._hideLegend = BOOLEAN_MAP[boolean]
        return self

    def hide_axes(self, boolean):
        """Hides both the x and y axis labels as well as the background grid"""
        self._hideAxes = BOOLEAN_MAP[boolean]
        return self

    def set_template(self, template):
        """
        Used for alternate coloring schemes

        **Default :** "alphas"
        """
        self._template = template
        return self

    def set_font(self, font):
        """
        Set font for text

        **Default :** "Helvetica"
        """
        self._fontName = font
        return self

    def area_mode(self, mode):
        """
        May be "none", "first", "stacked" or "all".
        This causes the area under lines to be shaded in, when using "all" you
        may need to use an alpha masked color

        **Default :** "none"
        """
        self._areaMode = mode
        return self

    def line_mode(self, mode):
        """
        May be either \"slope\" or \"staircase\"

        **Default :** "slope"
        """
        self._lineMode = mode
        return self

    def set_bgcolor(self, color):
        """
        Set image background color

        **Default :** white
        """
        self._bgcolor = color
        return self

    def add_metric(self, metric, colors=""):
        """
        Add a metric to image, may be either a graphite path
        or a function (such as avg)
        """
        self._target.append(metric)
        if colors:
            self._colorList = ",".join([color 
                for color in (self._colorList.split(",") + colors.split(","))
                if color])
        return self

    def graph_type(self, value):
        """
        Setup graph type, "line" or "pie"

        **Default :** "line"
        """
        self._graphType = value
        return self

    def add_deploy(self, deploy, colors=""):
        """Add a deploy metric"""
        self.add_metric("drawAsInfinite(%s)" % deploy, colors)
        return self

    def format(self, value):
        """
        Set output format as "csv" or "json"

        **Default : None**
        """
        self._format = value
        return self

    def _build_params(self):
        return dict([(key[1:], value)
            for key, value in self.__dict__.iteritems() if not value is None])

    def url(self, base, width, height):
        """Return image url based on the given URL for Graphite"""
        params = self._build_params()
        params['width'] = width
        params['height'] = height
        return "%s?%s" % (base, urlencode(params, True))
