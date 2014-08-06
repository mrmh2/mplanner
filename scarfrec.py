#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

import json

class Ingredient(object):

	def __init__(self, name):
		self.name = name

class MethodStep(object):

	def __init__(self, description):
		self.description = description

class Recipe(object):

	def __init__(self, name):
		self.name = name
		self.ingredients = []
		self.method_steps = []

	def add_ingredient(self, ingredient):
		self.ingredients.append(ingredient)

	def add_method_step(self, method_step):
		self.method_steps.append(method_step)

	def pretty_print(self):
		print(self.name + '\n')

		for ingredient in self.ingredients:
			print ingredient.name

		print('\n')

		for method_step in self.method_steps:
			print method_step.description

	def json_rep(self):
		dict_rep = {}
		dict_rep['name'] = self.name
		dict_rep['ingredients'] = [i.__dict__ for i in self.ingredients]
		dict_rep['method_steps'] = [m.__dict__ for m in self.method_steps]

		print json.dumps(dict_rep, indent=4, sort_keys=True)

	def __repr__(self):
		return "<Recipe: %s>" % self.name

def find_ingredients(soup):
	idiv = soup.find(id="ingredients")

	ing_list = idiv.find_all(name='li')

	return [ing.p.get_text() for ing in ing_list]

def find_method_steps(soup):
	prep_div = soup.find(id="preparation")

	prep_list = prep_div.find_all(name='li')

	return [prep_step.p.get_text() for prep_step in prep_list]

def scarf_recipe(recipe_url):
	print recipe_url

	r = requests.get(recipe_url)

	raw_html = r.text

	soup = BeautifulSoup(raw_html)

	#print soup.prettify().encode('utf-8')

	recipe_name = soup.find('div', 'article-title').h1.get_text()

	recipe = Recipe(recipe_name)

	ingredients = find_ingredients(soup)

	for ingredient in ingredients:
		recipe.add_ingredient(Ingredient(ingredient))

	method_steps = find_method_steps(soup)

	for method_step in method_steps:
		recipe.add_method_step(MethodStep(method_step))

	#recipe.pretty_print()

	recipe.json_rep()

def main():
	recipe_url = "http://www.bbc.co.uk/food/recipes/stuffedportobellomus_91403"
	#recipe_url = "http://www.bbc.co.uk/food/recipes/stirfriedszechuangre_91724"
	recipe_url = "http://www.bbc.co.uk/food/recipes/fennel_and_feta_linguini_59137"

	scarf_recipe(recipe_url)

if __name__ == '__main__':
	main()