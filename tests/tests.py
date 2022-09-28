import unittest
import requests

from openweather import OpenWeather

class FakeResponse:
    status_code = 0
    def close(self): pass
    def json(self): raise requests.exceptions.JSONDecodeError("", "", 0)


class TestOpenWeather(unittest.TestCase):

    def setUp(self):
        # Load test data
        self.ow = OpenWeather(requests, "TEST")
    
    # ************ EXCLUDE ************

    def test_exlude_1(self):
        self.ow.exclude(["daily"])
        assert self.ow.excludes == "daily"

    def test_exlude_2(self):
        self.ow.exclude(["hourly", "weekly"])
        assert self.ow.excludes == "hourly"

    def test_exlude_3(self):
        self.ow.exclude(["hourly", "current"])
        assert self.ow.excludes == "hourly,current"

    def test_exlude_4(self):
        self.ow.exclude(["current", "minutely", "hourly", "daily", "alerts"])
        assert self.ow.excludes == "current,minutely,hourly,daily,alerts"

    def test_exlude_none(self):
        self.ow.exclude(["current"])
        self.ow.exclude([])
        assert self.ow.excludes == "current"

    # ************ SET LANGUAGE ************

    def test_set_language_bad_default(self):
        self.ow.set_language("zzzzzz")
        assert self.ow.lang == "en"
    
    def test_set_language_bad_retain_preset(self):
        self.ow.set_language("pt_br")
        self.ow.set_language("zzzzzz")
        assert self.ow.lang == "pt_br"

    def test_set_language_good_1(self):
        self.ow.set_language("fr")
        assert self.ow.lang == "fr" 

    # ************ SET UNITS ************

    def test_set_units_bad_default(self):
        self.ow.set_units("zzzzzz")
        assert self.ow.units == "metric"

    def test_set_units_bad_retain_preset(self):
        self.ow.set_units("standard")
        self.ow.set_units("zzzzzz")
        assert self.ow.units == "standard" 

    def test_set_units_good(self):
        self.ow.set_units("imperial")
        assert self.ow.units == "imperial"

    # ************ CHECK COORDS ************
    
    def test_check_coords_none(self):
        result = self.ow._check_coords()
        assert result == False

    def test_check_coords_bad_lat(self):
        result = self.ow._check_coords(180, 0)
        assert result == False

    def test_check_coords_bad_lon(self):
        result = self.ow._check_coords(0, 360)
        assert result == False

    def test_check_coords_bad_both(self):
        result = self.ow._check_coords(360, 360)
        assert result == False

    def test_check_coords_bad_type_lon(self):
        result = self.ow._check_coords(39.8535, "ZZZZZZ")
        assert result == False

    def test_check_coords_bad_type_lat(self):
        result = self.ow._check_coords("ZZZZZZ", 25.3428)
        assert result == False

    # ************ ADD OPTIONS ************

    def test_add_options_default(self):
        self.ow = OpenWeather(requests, "TEST")
        result = self.ow._add_options()
        assert result == "&units=metric&lang=en"

    def test_add_options_add_excludes(self):
        self.ow = OpenWeather(requests, "TEST")
        self.ow.exclude(["daily"])
        result = self.ow._add_options()
        assert result == "&units=metric&lang=en&exclude=daily"

    # ************ REQUEST FORECAST ************

    def test_request_forecast_bad_coords(self):
        result = self.ow.request_forecast(39.8535, "ZZZZZZ")
        assert "error" in result and result["error"] == "Co-ordinate error"

    def test_request_forecast_no_coords(self):
        result = self.ow.request_forecast()
        assert "error" in result and result["error"] == "Co-ordinate error"

    def test_process_response_bad_code(self):
        response = FakeResponse()
        response.status_code = 400
        result = self.ow._process_response(response)
        assert "err" in result and result["err"] == "Unable to retrieve forecast data (code: 400)"

    def test_process_response_bad_json(self):
        response = FakeResponse()
        response.status_code = 200
        result = self.ow._process_response(response)
        assert "err" in result and result["err"].startswith("Unable to decode data received from Open Weather: ")

    # ************ CONSTRUCTOR ************

    def test_constructor_no_args(self):
        with self.assertRaises(AssertionError):
            result = OpenWeather()

    def test_constructor_bad_arg_apikey(self):
        with self.assertRaises(AssertionError):
            result = OpenWeather(requests, "")

    def test_constructor_bad_arg_reqs(self):
        with self.assertRaises(AssertionError):
            result = OpenWeather(None, "TEST")

    def test_constructor_bad_arg_debug(self):
        with self.assertRaises(AssertionError):
            result = OpenWeather(requests, "TEST", "TEST")        

if __name__ == "__main__":
    unittest.main()