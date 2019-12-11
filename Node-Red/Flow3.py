[
    {
        "id": "1329a4e0.222abb",
        "type": "tab",
        "label": "Flow 4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "b545ac24.2bfc5",
        "type": "inject",
        "z": "1329a4e0.222abb",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 150,
        "y": 160,
        "wires": [
            [
                "bfc46fd2.e2f69"
            ]
        ]
    },
    {
        "id": "bfc46fd2.e2f69",
        "type": "function",
        "z": "1329a4e0.222abb",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"qBEaMma0yff9pQP0\"\n};\nmsg.payload=\"Temperature,,25.2\"\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 140,
        "y": 340,
        "wires": [
            [
                "e69a5fad.8330d"
            ]
        ]
    },
    {
        "id": "e69a5fad.8330d",
        "type": "http request",
        "z": "1329a4e0.222abb",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/DO6dkC5K/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 310,
        "y": 280,
        "wires": [
            [
                "2e5c0c66.01ce44",
                "94ea5f21.4f771"
            ]
        ]
    },
    {
        "id": "2e5c0c66.01ce44",
        "type": "http response",
        "z": "1329a4e0.222abb",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 470,
        "y": 200,
        "wires": []
    },
    {
        "id": "94ea5f21.4f771",
        "type": "debug",
        "z": "1329a4e0.222abb",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 490,
        "y": 320,
        "wires": []
    }
]