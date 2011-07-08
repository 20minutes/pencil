# -*- coding: utf-8 -*-
from urllib import urlencode


class Pencil(object):
    def __init__(self, begin=None, end=None):
        self._from = begin
        self._until = end
        self._title = None
        self._vtitle = None
        self._target = []
        self._colorList = []
        self._bgcolor = "FFFFFF"
        self._fgcolor = "000000"
        self._fontName = "Helvetica"
        self._areaMode = "none"
        self._lineMode = "slope"

    def set_title(self, title):
        self._title = title
        return self

    def set_vtitle(self, title):
        self._vtitle = title
        return self

    def set_fgcolor(self, color):
        self._fgcolor = color
        return self

    def set_font(self, font):
        self._fontName = font
        return self

    def area_mode(self, mode):
        self._areaMode = mode
        return self

    def line_mode(self, mode):
        self._lineMode = mode
        return self

    def set_bgcolor(self, color):
        self._bgcolor = color
        return self

    def add_metric(self, metric, color=None):
        self._target.append(metric)
        if color:
            self._colorList.append(color)
        return self

    def add_deploy(self, deploy):
        self._target.append("drawAsInfinite(%s)" % deploy)
        return self

    def _build_params(self):
        return dict([(key[1:], value)
            for key, value in self.__dict__.iteritems() if value])

    def url(self, base, width, height):
        params = self._build_params()
        params['width'] = width
        params['height'] = height
        return "%s?%s" % (base, urlencode(params, True))
