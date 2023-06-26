#!/usr/bin/python
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
	"""A function that prints x elements of a list."""

	y = 0
	for j in range(x):
		try:
			k = "{}"
			print(k.format(my_list[i]), end="")
			ret += 1
		except IndexError:
			break
	print("")
	return (y)
