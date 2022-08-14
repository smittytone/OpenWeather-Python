# OpenWeather-Python

Α Python integration for the OpenWeather API.

The class it contains allows you to make one of two possible calls to [OpenWeather’s API](https://openweathermap.org/api/one-call-api).

Access to the API is controlled by key. [Register for developer access](https://openweathermap.org/appid) to obtain your key.

**Note** Rhis class does not parse the incoming data, which is highly complex. It is up to your application to extract the data you require.

## Python Requests

The library uses the Python `Requests` module or equivalent to issue HTTP requests to the API and process the responses. Your code will need to import `Requests` and pass an instance into the library’s constructor.

The library does not import `requests` itself in order to support different species of Python, such as [MicroPython](https://micropyhon.org) and [CircuitPython](https://circuitpython.org) which have slightly different implementations of `Requests`.

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

## Copyright and licence

OpenWeather-Python is © 2022 by Tony Smith and is licensed under the terms of the [MIT licence](./LICENSE.md).