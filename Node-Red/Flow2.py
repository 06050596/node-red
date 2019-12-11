[
    {
        "id": "e41db834.6bee28",
        "type": "tab",
        "label": "Flow 5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "38b6047d.e1ebcc",
        "type": "inject",
        "z": "e41db834.6bee28",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 110,
        "y": 180,
        "wires": [
            [
                "d720dfa9.2e6e3"
            ]
        ]
    },
    {
        "id": "d720dfa9.2e6e3",
        "type": "function",
        "z": "e41db834.6bee28",
        "name": "",
        "func": "msg.headers={\n    deviceKey:\"paMOyV7WuTC0K0ta\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 250,
        "y": 120,
        "wires": [
            [
                "490c86ab.79ca58"
            ]
        ]
    },
    {
        "id": "cfb3f636.4cefe8",
        "type": "http response",
        "z": "e41db834.6bee28",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 630,
        "y": 140,
        "wires": []
    },
    {
        "id": "490c86ab.79ca58",
        "type": "http request",
        "z": "e41db834.6bee28",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/Dd8hF7V0/datachannels/LEDControl/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 430,
        "y": 120,
        "wires": [
            [
                "cfb3f636.4cefe8",
                "dd9e1223.68f89"
            ]
        ]
    },
    {
        "id": "dd9e1223.68f89",
        "type": "debug",
        "z": "e41db834.6bee28",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 630,
        "y": 200,
        "wires": []
    }
]