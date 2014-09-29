import sys
import os
import csv
import itertools

file_name = sys.argv[1]

reader = csv.reader(open(file_name,'r'))

def parse_lev_list(line):
	return line[:-1]

def parse_content(line):
	return line[-1]

def generate_file_name(old_name, append):
	return "%s_%s.md" %(old_name,append)

def list_all_false(lis):
	for i in lis:
		if i:
			return False
	return True

def append_to_files(file_name_list, content_list):
	for file_name,content in zip(file_name_list, content_list):
		with open(file_name,'a') as fd:
			fd.write(content)
			fd.write('\n\n')

lev_name_list = parse_lev_list(next(reader))

for line in reader:
	lev_flag = parse_lev_list(line)
	file_name_list = []
	content_list = []
	if list_all_false(lev_flag):
		file_name_list = map(lambda x:generate_file_name(file_name,x), lev_name_list )
		content_list   = [parse_content(line)] * len(lev_name_list)
	else:
		for i,flag in enumerate(lev_flag):
			if flag=='y' or flag=='Y':
				file_name_list.append(generate_file_name(file_name,lev_name_list[i]))
				content_list.append(parse_content(line))
	append_to_files(file_name_list, content_list)