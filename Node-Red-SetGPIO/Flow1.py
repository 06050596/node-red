[
    {
        "id": "b626a202.5b508",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "5fa6f795.0c5268",
        "type": "http in",
        "z": "b626a202.5b508",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 110,
        "y": 180,
        "wires": [
            [
                "cf722e46.6e089"
            ]
        ]
    },
    {
        "id": "5e84d206.e9e06c",
        "type": "http response",
        "z": "b626a202.5b508",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 460,
        "y": 100,
        "wires": []
    },
    {
        "id": "84c149d4.7670f8",
        "type": "debug",
        "z": "b626a202.5b508",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 490,
        "y": 200,
        "wires": []
    },
    {
        "id": "cf722e46.6e089",
        "type": "function",
        "z": "b626a202.5b508",
        "name": "Get GPIO",
        "func": "msg.payload=global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 140,
        "wires": [
            [
                "84c149d4.7670f8",
                "5e84d206.e9e06c"
            ]
        ]
    },
    {
        "id": "93e7d73b.1ae9b8",
        "type": "function",
        "z": "b626a202.5b508",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 260,
        "wires": [
            [
                "84c149d4.7670f8"
            ]
        ]
    },
    {
        "id": "79eb3a70.d9c274",
        "type": "rpi-gpio in",
        "z": "b626a202.5b508",
        "name": "",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 120,
        "y": 280,
        "wires": [
            [
                "93e7d73b.1ae9b8"
            ]
        ]
    }
]