#!/usr/bin/python

import json, sys, getopt
import glob, os
from pprint import pprint
import codecs

def parse(file_name):
    
  data = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
  print "COMPANY | "
  counter = 0

  json_company = {}
  skills_list = []
  jobtitles_list = []
    
  for company in data:
    json_company["description"] = company['description'].encode('utf-8')
    json_company['name'] = company['name'].encode('utf-8')
    json_company['postcode'] = ''
    json_company['distance_from_home'] = ''
    json_company['maps_link'] = ''
    if company['jobtags'] is not None:
      # looking for skills in JAVA
      if '"Java"' in company['jobtags']:
        skills = company['jobtags'].split('|TAG|')
        for skill_entry in skills:
            # AWS, SQL, LINUX, Distance
          skill_details = json.loads(skill_entry) 
          skills_list.append(skill_details['name'].encode('utf-8'))
        json_company['skills'] = skills_list
        skills_list = []
        
        jobtitles = company['jobtitles'].split('|JOB|')
        for jobtitle_entry in jobtitles:
          jobtitle_details = json.loads(jobtitle_entry)
          jobtitles_list.append(jobtitle_details['title'].encode('utf-8'))
        json_company['jobtitles'] = jobtitles_list
        jobtitles_list = []
      pprint(json_company)
    counter = counter + 1                


def main(argv):
  file_name = ''
  try:
    opts, args = getopt.getopt(argv,"f:",["file_name="])
  except getopt.GetoptError:
    print 'siliconmilkroundabout-company-parser.py -f <file_name>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'siliconmilkroundabout-company-parser.py -f <file_name>'
      sys.exit()
    elif opt in ("-f", "--file_name"):
      file_name = arg
  print 'File name is ', file_name
  parse(file_name)
  print 'done'

if __name__ == "__main__":
  main(sys.argv[1:])
