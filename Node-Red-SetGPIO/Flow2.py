[
    {
        "id": "9f0d9938.6bc568",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "bbab9b46.8c6388",
        "type": "function",
        "z": "9f0d9938.6bc568",
        "name": "HIGH",
        "func": "msg.payload=\"GPIO set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 100,
        "wires": [
            [
                "d68a441a.8f88c8",
                "f5baa158.789d7"
            ]
        ]
    },
    {
        "id": "54df2084.75798",
        "type": "function",
        "z": "9f0d9938.6bc568",
        "name": "to 0",
        "func": "msg.payload=0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 250,
        "y": 300,
        "wires": [
            [
                "ec50a2b6.7f43c"
            ]
        ]
    },
    {
        "id": "8f6600ea.c21af",
        "type": "function",
        "z": "9f0d9938.6bc568",
        "name": "LOW",
        "func": "msg.payload=\"GPIO set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 440,
        "wires": [
            [
                "d68a441a.8f88c8",
                "f5baa158.789d7"
            ]
        ]
    },
    {
        "id": "d68a441a.8f88c8",
        "type": "debug",
        "z": "9f0d9938.6bc568",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 630,
        "y": 300,
        "wires": []
    },
    {
        "id": "f5baa158.789d7",
        "type": "http response",
        "z": "9f0d9938.6bc568",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 590,
        "y": 160,
        "wires": []
    },
    {
        "id": "a33d29b3.5d6318",
        "type": "http in",
        "z": "9f0d9938.6bc568",
        "name": "",
        "url": "/1",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 70,
        "y": 200,
        "wires": [
            [
                "64791f2d.3a30d",
                "bbab9b46.8c6388"
            ]
        ]
    },
    {
        "id": "14581a86.ab19e5",
        "type": "http in",
        "z": "9f0d9938.6bc568",
        "name": "",
        "url": "/0",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 70,
        "y": 280,
        "wires": [
            [
                "54df2084.75798",
                "8f6600ea.c21af"
            ]
        ]
    },
    {
        "id": "ec50a2b6.7f43c",
        "type": "rpi-gpio out",
        "z": "9f0d9938.6bc568",
        "name": "",
        "pin": "11",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 400,
        "y": 260,
        "wires": []
    },
    {
        "id": "64791f2d.3a30d",
        "type": "function",
        "z": "9f0d9938.6bc568",
        "name": "to 1",
        "func": "msg.payload=1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 290,
        "y": 160,
        "wires": [
            [
                "ec50a2b6.7f43c"
            ]
        ]
    }
]