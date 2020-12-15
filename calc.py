import json


# multiply leaves of dict tree
def mul(d, cnt):
	for k in d.keys():
		if type(d[k]) == int:
			d[k] *= cnt
		else:
			mul(d[k], cnt)


def merge(da, db, cnt):
	for k in db.keys():
		if (type(db[k]) == int):
			if k in da.keys():
				da[k] += db[k] * cnt
			else:
				da[k] = db[k] * cnt
		else:
			if k in da.keys():
				merge(da[k], db[k], cnt, rank + 1)
			else:
				dbc = db
				mul(dbc, cnt)
				da[k] = db[k]
				
				
def calc(name, cnt, mat='', rank=0):
	with open("craft/{}.json".format(name), 'r') as f:
		craft = json.loads(f.read())
	f.close()

	if len(craft) == 0:
		return {name: {mat: cnt}}
	
	res = {}
	for meta in craft.keys():
		for material in craft[meta].keys():
			cover_material = material
			if cover_material == '':
				cover_material = mat
			subres = calc(meta, craft[meta][material], cover_material, rank + 1)
			merge(res, subres, cnt)

	return res
