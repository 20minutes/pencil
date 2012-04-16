from unittest import TestCase

from pencil import Pencil


class PencilTest(TestCase):
    def setUp(self):
        self.pencil = Pencil()

    def test_begin(self):
        self.pencil.begin("-2hours")
        self.assertEqual(self.pencil._from, "-2hours")

    def test_y_min(self):
        self.pencil.y_min(32)
        self.assertEqual(self.pencil._yMin, 32)

    def test_y_max(self):
        self.pencil.y_max(42)
        self.assertEqual(self.pencil._yMax, 42)

    def test_line_width(self):
        self.pencil.line_width(2)
        self.assertEqual(self.pencil._lineWidth, 2)

    def test_set_title(self):
        self.pencil.set_title("Pencil")
        self.assertEqual(self.pencil._title, "Pencil")

    def test_set_vtitle(self):
        self.pencil.set_vtitle("Awesomeness")
        self.assertEqual(self.pencil._vtitle, "Awesomeness")

    def test_fgcolor(self):
        self.pencil.set_fgcolor("blue")
        self.assertEqual(self.pencil._fgcolor, "blue")

    def test_hide_legend(self):
        self.pencil.hide_legend(True)
        self.assertEqual(self.pencil._hideLegend, "true")
        self.pencil.hide_legend(False)
        self.assertEqual(self.pencil._hideLegend, "false")

    def test_hide_axes(self):
        self.pencil.hide_axes(True)
        self.assertEqual(self.pencil._hideAxes, "true")
        self.pencil.hide_axes(False)
        self.assertEqual(self.pencil._hideAxes, "false")

    def test_set_template(self):
        self.pencil.set_template("plain")
        self.assertEqual(self.pencil._template, "plain")

    def test_set_font(self):
        self.pencil.set_font("Verdana")
        self.assertEqual(self.pencil._fontName, "Verdana")

    def test_area_mode(self):
        self.pencil.area_mode("stacked")
        self.assertEqual(self.pencil._areaMode, "stacked")

    def test_line_mode(self):
        self.pencil.line_mode("staircase")
        self.assertEqual(self.pencil._lineMode, "staircase")

    def test_set_bgcolor(self):
        self.pencil.set_bgcolor("red")
        self.assertEqual(self.pencil._bgcolor, "red")

    def test_add_metric(self):
        self.pencil.add_metric("pencil.urls.count")
        self.assertEqual(self.pencil._target, ['pencil.urls.count'])

    def test_add_metric_with_color(self):
        self.pencil.add_metric("pencil.urls.count", "000000")
        self.assertEqual(self.pencil._target, ['pencil.urls.count'])
        self.assertEqual(self.pencil._colorList, "000000")

    def test_add_metric_with_alias(self):
        self.pencil.add_metric("pencil.urls.count", alias="urls")
        self.assertEqual(self.pencil._target,
            ['alias(pencil.urls.count, "urls")'])

    def test_graph_type(self):
        self.pencil.graph_type("pie")
        self.assertEqual(self.pencil._graphType, "pie")

    def test_add_deploy(self):
        self.pencil.add_deploy("pencil")
        self.assertEqual(self.pencil._target, ['drawAsInfinite(pencil)'])

    def test_add_deploy_with_alias(self):
        self.pencil.add_deploy("pencil", alias="deploy")
        self.assertEqual(self.pencil._target,
            ['alias(drawAsInfinite(pencil), "deploy")'])
