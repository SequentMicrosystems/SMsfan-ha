FULL_NAME = "Smart Fan"
LINK = "https://sequentmicrosystems.com/products/smart-fan-for-raspberry-pi"

import sfan
API = sfan
DOMAIN = "SMsfan"
NAME_PREFIX = "smsf"
SM_MAP = {
    "number": {
        "power": {
                "chan_no": 1,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 1.0,
                "com": {
                    "get": "getPower",
                    "set": "setPower"
                },
                "icon": {
                    "on": "mdi:fan",
                    "off": "mdi:fan-off"
                }
        },
    },
}
