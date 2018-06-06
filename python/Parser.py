#!/usr/bin/python

import json, sys, getopt
import glob, os
from pprint import pprint
import codecs
Class Parser: 

	def parse(file_name):
	  
	  data = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
	  counter = 0
	  
	  parse_result = {}
	  company_list = []
	  
	  
	  company_post_codes_map = {}
	  company_post_codes_map['ABC'] = 'SE191AA'
	  
	  json_company = {}
	  skills_list = []
	  jobtitles_list = []
		
	  for company_entry in data:
		json_company['description'] = company_entry['description'].decode('utf-8')
		json_company['name'] = company_entry['name'].decode('utf-8')
		json_company['postcode'] = ''
		json_company['distance_from_home'] = ''
		json_company['maps_link'] = ''
				
		if company_entry['jobtags'] is not None:
		  # looking for skills in JAVA
		  if '"Java"' in company_entry['jobtags']:
			skills = company['jobtags'].split('|TAG|')
			json_company['uses_java'] = True
			for skill_entry in skills:
				# AWS, SQL, LINUX, Distance			  
			  skill_details = json.loads(skill_entry) 
			  skills_list.append(skill_details['name'].decode('utf-8'))
			json_company['skills'] = skills_list
			skills_list = []
			
			jobtitles = company_entry['jobtitles'].split('|JOB|')
			for jobtitle_entry in jobtitles:
			  jobtitle_details = json.loads(jobtitle_entry)
			  jobtitles_list.append(jobtitle_details['title'].decode('utf-8'))
			json_company['jobtitles'] = jobtitles_list
			jobtitles_list = []
		
		  # pprint(json_company)
		  c = Company(json_company)
		  c.print_short
		  company_list.append(c)
		counter = counter + 1
	  parse_result['companies'] = company_list
	  return 