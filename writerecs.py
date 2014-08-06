#!/usr/bin/env python

import json

class Ingredient(object):

	def __init__(self):
		pass
		
def make_ingredient(*args):
	labels = ["name", "unit", "quantity"]

	return dict(zip(labels, args))

def make_step(*args):
	pass


def main():
	i1 = make_ingredient("aubergine", "whole", 1)
	i2 = make_ingredient("red pepper", "whole", 1)
	i3 = make_ingredient("capers", "g", 50)

	s1 = "Grill the aubergine"
	s2 = "Chop the pepper"
	s3 = "Eat the capers"

	recipe = {"ingredients" : [i1, i2, i3], "steps" : [s1, s2, s3]}

	print(json.dumps(recipe, indent=4, sort_keys=True))

	pass

if __name__ == '__main__':
	main()