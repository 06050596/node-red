[
    {
        "id": "9cfbf53d.ff2b68",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "48be5873.5f3138",
        "type": "debug",
        "z": "9cfbf53d.ff2b68",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 840,
        "y": 600,
        "wires": []
    },
    {
        "id": "b3e154bf.8b3b78",
        "type": "rpi-gpio in",
        "z": "9cfbf53d.ff2b68",
        "name": "button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 490,
        "y": 660,
        "wires": [
            [
                "7a47f38f.a3e12c",
                "48be5873.5f3138"
            ]
        ]
    },
    {
        "id": "1f5ff1c8.e1a10e",
        "type": "rpi-gpio out",
        "z": "9cfbf53d.ff2b68",
        "name": "",
        "pin": "11",
        "set": false,
        "level": "1",
        "freq": "",
        "out": "out",
        "x": 1020,
        "y": 720,
        "wires": []
    },
    {
        "id": "7a47f38f.a3e12c",
        "type": "switch",
        "z": "9cfbf53d.ff2b68",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "else"
            },
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 650,
        "y": 720,
        "wires": [
            [
                "763c3f5e.63953"
            ],
            [
                "c2bb0d9d.bed3c"
            ]
        ]
    },
    {
        "id": "763c3f5e.63953",
        "type": "change",
        "z": "9cfbf53d.ff2b68",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 830,
        "y": 680,
        "wires": [
            [
                "1f5ff1c8.e1a10e"
            ]
        ]
    },
    {
        "id": "c2bb0d9d.bed3c",
        "type": "change",
        "z": "9cfbf53d.ff2b68",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 830,
        "y": 780,
        "wires": [
            [
                "1f5ff1c8.e1a10e"
            ]
        ]
    }
]