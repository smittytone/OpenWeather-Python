# OpenWeather-Python 2.1.0

The class this integration contains allows you to make calls to [OpenWeather’s One Call API 1.0](https://openweathermap.org/api/one-call-api).

Access to the API is controlled by key. You will need to [register for developer access](https://openweathermap.org/appid) to obtain your key.

**Note** This class does not parse the incoming data, which is highly complex. It is up to your application to extract the data you require.

## Python Requests

The library uses the Python `Requests` module or equivalent to issue HTTP requests to the API and process the responses. Your code will need to import `Requests` and pass an instance into the library’s constructor.

The library does not import `requests` itself in order to support different species of Python, such as [MicroPython](https://micropyhon.org) and [CircuitPython](https://circuitpython.org) which have different implementations of `Requests`. For instance:

```python
# MicroPython example
import urequests as requests

ow = OpenWeather(requests, secrets["apikey"], True
```

```python
# CircuitPython example
import adafruit_requests as requests

ow = OpenWeather(requests, secrets["apikey"], False)
```

The library uses `Requests`’ `get()` method, and works with `Response` instances created by requests.

## Documentation

You can [find full library documentation at smittytone.net](https://smittytone.net/docs/openweather.html).

## Copyright and licence

OpenWeather-Python is © 2022 by Tony Smith and is licensed under the terms of the [MIT licence](./LICENSE.md).

The OpenWeather One Call API is © 2012—2022, OpenWeather.