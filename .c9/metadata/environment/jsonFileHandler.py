{"changed":true,"filter":false,"title":"jsonFileHandler.py","tooltip":"/jsonFileHandler.py","value":"import json\n\n\ndef readJsonFile(fileName):\n    data = \"\"\n    try:\n        with open(fileName) as json_file:\n            data = json.load(json_file)\n    except IOError:\n        print(\"Could not read file\")\n    return data","undoManager":{"mark":-2,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":11},"action":"insert","lines":["import json"],"id":2}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":27},"action":"insert","lines":["def readJsonFile(fileName):"],"id":5}],[{"start":{"row":2,"column":27},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["def readJsonFile(fileName):","    "],"id":7},{"start":{"row":2,"column":0},"end":{"row":6,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"]}],[{"start":{"row":2,"column":0},"end":{"row":6,"column":15},"action":"remove","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"],"id":8},{"start":{"row":2,"column":0},"end":{"row":10,"column":15},"action":"insert","lines":["","def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":15},"end":{"row":10,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1701713438408}