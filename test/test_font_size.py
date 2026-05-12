import sys
import os
import unittest
from unittest.mock import MagicMock, patch
from types import ModuleType

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def _setup_mock_module(name, attrs=None):
    if name not in sys.modules:
        mod = MagicMock()
        if attrs:
            for k, v in attrs.items():
                setattr(mod, k, v)
        sys.modules[name] = mod
    return sys.modules[name]


_shapely = _setup_mock_module("shapely")
_setup_mock_module("shapely.geometry", {"Point": MagicMock})
_setup_mock_module("networkx", {"MultiDiGraph": MagicMock})
_geopy = _setup_mock_module("geopy")
_setup_mock_module("geopy.geocoders", {"Nominatim": MagicMock})
_setup_mock_module("geopandas", {"GeoDataFrame": MagicMock})
_np = _setup_mock_module("numpy")
_setup_mock_module("tqdm")
_mpl = _setup_mock_module("matplotlib")
_mpl.use = MagicMock()
_setup_mock_module("matplotlib.colors")
_setup_mock_module("matplotlib.pyplot")
_setup_mock_module("matplotlib.font_manager")
_setup_mock_module("osmnx")
_setup_mock_module("osmnx.projection")
_setup_mock_module("lat_lon_parser", {"parse": MagicMock()})
_setup_mock_module("PIL")
_setup_mock_module("font_management", {"load_fonts": MagicMock(return_value=None)})
_setup_mock_module("scipy")
_setup_mock_module("scipy.sparse")


MINIMAL_THEME = {
    "bg": "#FFFFFF",
    "water": "#0000FF",
    "parks": "#00FF00",
    "gradient_color": "#FFFFFF",
    "text": "#000000",
    "road_colors": {"primary": "#000000", "secondary": "#333333", "tertiary": "#666666"},
    "road_widths": {"primary": 1.0, "secondary": 0.5, "tertiary": 0.3},
}


class _FontPropTracker:

    def __init__(self):
        self.created = []

    def make(self, **kwargs):
        fp = MagicMock()
        size = kwargs.get("size", 0)
        fp.get_size.return_value = size
        fp._size = size
        fp._kwargs = kwargs
        self.created.append(fp)
        return fp


class TestFontSizeOverride(unittest.TestCase):

    def _run_create_poster(self, font_size=None):
        import importlib
        import create_map_poster
        importlib.reload(create_map_poster)

        tracker = _FontPropTracker()
        text_calls = []

        def capture_text(*args, **kwargs):
            text_calls.append({"args": args, "kwargs": kwargs})

        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_ax.text = capture_text
        mock_ax.plot = MagicMock()
        mock_ax.transAxes = MagicMock()

        empty_gdf = MagicMock()
        empty_gdf.empty = True

        g = MagicMock()
        g_proj = MagicMock()
        g_proj.graph = {"crs": "EPSG:3857"}

        with patch.object(create_map_poster, "fetch_graph", return_value=g), \
             patch.object(create_map_poster, "fetch_features", return_value=empty_gdf), \
             patch.object(create_map_poster, "ox") as mock_ox, \
             patch.object(create_map_poster, "get_edge_colors_by_type", return_value=[]), \
             patch.object(create_map_poster, "get_edge_widths_by_type", return_value=[]), \
             patch.object(create_map_poster, "get_crop_limits", return_value=((0, 1), (0, 1))), \
             patch.object(create_map_poster, "create_gradient_fade"), \
             patch.object(create_map_poster, "FONTS", None), \
             patch.object(create_map_poster, "FontProperties", side_effect=tracker.make), \
             patch.object(create_map_poster, "plt") as mock_plt, \
             patch("builtins.print"):

            mock_plt.subplots.return_value = (mock_fig, mock_ax)

            mock_ox.project_graph.return_value = g_proj
            mock_ox.plot_graph = MagicMock()

            buf = MagicMock()
            buf.write = MagicMock()

            create_map_poster.create_poster(
                city="Paris",
                country="France",
                point=(48.8566, 2.3522),
                dist=10000,
                output_file=buf,
                output_format="png",
                width=3600,
                height=4800,
                theme=MINIMAL_THEME,
                font_size=font_size,
            )

        return text_calls, tracker

    def _find_font_size(self, text_calls, text_contains):
        for tc in text_calls:
            args = tc["args"]
            if len(args) >= 3 and text_contains in str(args[2]):
                fp = tc["kwargs"].get("fontproperties")
                if fp is not None:
                    return fp._size
        return None

    def test_no_override_produces_text(self):
        text_calls, _ = self._run_create_poster(font_size=None)
        self.assertTrue(len(text_calls) > 0, "Should produce text calls")

    def test_2x_doubles_city_font(self):
        calls_def, _ = self._run_create_poster(font_size=None)
        calls_2x, _ = self._run_create_poster(font_size=2.0)

        size_def = self._find_font_size(calls_def, "P  A  R  I  S")
        size_2x = self._find_font_size(calls_2x, "P  A  R  I  S")

        self.assertIsNotNone(size_def, "City text should exist in default")
        self.assertIsNotNone(size_2x, "City text should exist in 2x")
        self.assertAlmostEqual(size_2x, size_def * 2.0, places=1)

    def test_half_reduces_country_font(self):
        calls_def, _ = self._run_create_poster(font_size=None)
        calls_half, _ = self._run_create_poster(font_size=0.5)

        size_def = self._find_font_size(calls_def, "FRANCE")
        size_half = self._find_font_size(calls_half, "FRANCE")

        self.assertIsNotNone(size_def)
        self.assertIsNotNone(size_half)
        self.assertAlmostEqual(size_half, size_def * 0.5, places=1)

    def test_1_5x_scales_coords(self):
        calls_def, _ = self._run_create_poster(font_size=None)
        calls_15, _ = self._run_create_poster(font_size=1.5)

        size_def = self._find_font_size(calls_def, "°")
        size_15 = self._find_font_size(calls_15, "°")

        self.assertIsNotNone(size_def)
        self.assertIsNotNone(size_15)
        self.assertAlmostEqual(size_15, size_def * 1.5, places=1)

    def test_1_0_matches_no_override(self):
        calls_none, _ = self._run_create_poster(font_size=None)
        calls_one, _ = self._run_create_poster(font_size=1.0)

        city_none = self._find_font_size(calls_none, "P  A  R  I  S")
        city_one = self._find_font_size(calls_one, "P  A  R  I  S")

        self.assertIsNotNone(city_none)
        self.assertIsNotNone(city_one)
        self.assertAlmostEqual(city_none, city_one, places=1)


if __name__ == "__main__":
    unittest.main()
