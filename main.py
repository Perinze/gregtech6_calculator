def route():
	import ui
	from calc import calc
	from add import add

	req = ui.listen()
	act = req.pop(0)
	if act == 'calc':
		if len(req) == 2:
			req.append('')
		res = calc(req[0], req[1], req[2])
		ui.show(res)
	elif act == 'add':
		add(req)
	elif act == 'q':
		return False
	else:
		pass
	return True
		

if __name__ == '__main__':
	print("enter 'q' to quit")
	while route():
		pass
