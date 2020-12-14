import json


def add(name, craft):
	with open("craft/{}.json".format(name) , 'w') as f:
		f.write(json.dumps(craft, sort_keys=True, indent=4))
		f.close()
