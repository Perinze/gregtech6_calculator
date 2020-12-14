import json


def plus(dict_a, dict_b, cnt):
	for bk in dict_b.keys():
		sub_dict_b = dict_b[bk]

		if bk in dict_a.keys():
			sub_dict_a = dict_a[bk]

			for sk in sub_dict_b.keys():
				if sk in sub_dict_a.keys():
					new_val = sub_dict_a[sk] + sub_dict_b[sk] * cnt
				else:
					new_val = sub_dict_b[sk] * cnt
				dict_a[bk].update({sk: new_val})

		else:
			for sk in sub_dict_b.keys():
				new_val = sub_dict_b[sk] * cnt
				dict_a.update({bk: {sk: new_val}})


def calc(name, cnt, mat='', rank=0):
	log = open("calc.log", "w")

	log.write("{}calc('{}', {}, '{}')".format(rank * '\t', name, cnt, mat))
	with open("craft/{}.json".format(name), 'r') as f:
		craft = json.loads(f.read())
	f.close()

	if len(craft) == 0:
		return {name: {mat: cnt}}	# {plate: {"": 4}}
	
	res = {}
	for meta in craft.keys():	# for key in {curved_plate, ring, screw}
		for material in craft[meta].keys():
			cover_material = material
			if cover_material == '':
				cover_material = mat
			subres = calc(meta, craft[meta][material], cover_material, rank + 1)	# calc(curved_plate, {"": 4}), subres = {plate: {"": 4}}
			plus(res, subres, cnt)

		'''
		for meta in subres.keys():	# plate, ring, screw
			for material in subres[meta].keys():	# "", stainless_steel, invar
				if meta in res.keys():	# plate in res.keys = [plate, ring, screw]
					if material in res[meta].keys():	# stainless_steel in ["", "stainless_steel"]
						res[meta][material] += subres[meta][meterial] * cnt
					else:
						res[meta][material] = subres[meta][meterial] * cnt
				else:
				 	res[meta][material] = subres[meta][material] * cnt
		'''

	log.write("{}res = {}".format(rank * '\t', res))

	log.close()
	return res
