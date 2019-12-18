[
    {
        "id": "4f0e46a1.565ae8",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "af628d60.113aa",
        "type": "inject",
        "z": "4f0e46a1.565ae8",
        "name": "",
        "topic": "",
        "payload": ",,25.3",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 150,
        "y": 180,
        "wires": [
            [
                "da05d5db.3baf18"
            ]
        ]
    },
    {
        "id": "ac0d1b3.947ace8",
        "type": "inject",
        "z": "4f0e46a1.565ae8",
        "name": "",
        "topic": "",
        "payload": ",,31.7",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 150,
        "y": 300,
        "wires": [
            [
                "da05d5db.3baf18"
            ]
        ]
    },
    {
        "id": "da05d5db.3baf18",
        "type": "mqtt out",
        "z": "4f0e46a1.565ae8",
        "name": "",
        "topic": "mcs/DbRoKLhc/0m1IixzX0GrW0lnz/Temperature",
        "qos": "",
        "retain": "",
        "broker": "61e5064.df6d3f8",
        "x": 470,
        "y": 260,
        "wires": []
    },
    {
        "id": "61e5064.df6d3f8",
        "type": "mqtt-broker",
        "z": "",
        "name": "MCS Cloud",
        "broker": "mqtt.mcs.mediatek.com",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "willTopic": "",
        "willQos": "0",
        "willPayload": ""
    }
]