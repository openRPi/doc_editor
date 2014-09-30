# -*- coding:utf-8 -*-

import sys
import os
import csv
import itertools
import io
import collections

class tree(object):
	"""docstring for tree"""
	container = collections.defaultdict(str)

	def __init__(self):
		super(tree, self).__init__()

	def append2lev(self,lev,data):
		tree.container[lev] += data

	def get_dict(self):
		return tree.container

	def __str__(self):
		string = ''
		for key in tree.container:
			string += key + '\n'
			string += tree.container[key]
			string += '\n'
		return string

def check_cmd(line):
	if line.startswith('@'):
		return True 
	return False

def check_lev_end(line):
	if line.startswith('@end'):
		return True 
	return False

def parse_lev(line):
	if line.startswith('@') and not check_lev_end(line):
		lev_list = list(map(lambda x: x.strip(' ').strip('\n').strip('\r'), line[1:].split(',')))
		return lev_list
	else:
		return None

def parse2tree(lines, tree_module):
	lev_stack = []
	for line in lines:
		if check_cmd(line):
			lev_list = parse_lev(line)
			# 入栈
			if lev_list:
				lev_stack.append(lev_list)
			# 出栈
			if check_lev_end(line):
				lev_stack.pop(-1)
		else:
			for lev in lev_stack[-1]:
				tree_module.append2lev(lev,line)

def main():
	file_name = sys.argv[1]
	tree_module = tree()
	parse2tree(open(file_name,'r').readlines(),tree_module)

	tree_value = tree_module.get_dict()
	for key in tree_value:
		with open("%s_%s.md" %(file_name,key), 'w') as fd:
			fd.write(tree_value[key])

if __name__ == '__main__':
	main()

