#!/usr/bin/python
# 0-safe_print_list.py
# by: Aropet_Joel

def safe_print_list(my_list=[], x=0):
	"""A function that prints x elements of a list."""

	ret = 0
	for i in range(x):
		try:
			print("{}".format(my_list[i]), end="")
			ret += 1
		except IndexError:
			break
	print("")
	return (ret)
