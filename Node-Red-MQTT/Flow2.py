[
    {
        "id": "a91a753d.13b358",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "257647af.aeeb28",
        "type": "mqtt in",
        "z": "a91a753d.13b358",
        "name": "",
        "topic": "mcs/DbRoKLhc/0m1IixzX0GrW0lnz/+",
        "qos": "2",
        "datatype": "auto",
        "broker": "61e5064.df6d3f8",
        "x": 250,
        "y": 180,
        "wires": [
            [
                "f50b55fa.d79ff8"
            ]
        ]
    },
    {
        "id": "f50b55fa.d79ff8",
        "type": "csv",
        "z": "a91a753d.13b358",
        "name": "",
        "sep": ",",
        "hdrin": "",
        "hdrout": "",
        "multi": "one",
        "ret": "\\n",
        "temp": ",,Data",
        "skip": "0",
        "strings": true,
        "x": 470,
        "y": 240,
        "wires": [
            [
                "41963df2.3e58a4"
            ]
        ]
    },
    {
        "id": "41963df2.3e58a4",
        "type": "change",
        "z": "a91a753d.13b358",
        "name": "Get Data",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.Data",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 440,
        "y": 380,
        "wires": [
            [
                "1b1cebc3.aeb5d4"
            ]
        ]
    },
    {
        "id": "1b1cebc3.aeb5d4",
        "type": "ui_gauge",
        "z": "a91a753d.13b358",
        "name": "",
        "group": "3d06a7f0.54b9a8",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "gauge",
        "label": "units",
        "format": "{{value}}",
        "min": 0,
        "max": "50",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 640,
        "y": 400,
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
    },
    {
        "id": "3d06a7f0.54b9a8",
        "type": "ui_group",
        "z": "",
        "name": "Status",
        "tab": "698706cb.416668",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "698706cb.416668",
        "type": "ui_tab",
        "name": "Tab 1",
        "icon": "dashboard",
        "order": 1
    }
]