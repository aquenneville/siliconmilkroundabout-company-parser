#!/usr/bin/python
import json, sys, getopt
import glob, os
from pprint import pprint

def main(argv):
  file_name = ''
  try:
    opts, args = getopt.getopt(argv,"f:",["file_name="])
  except getopt.GetoptError:
    print('siliconmilkroundabout-company-parser.py -f <file_name>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('siliconmilkroundabout-company-parser.py -f <file_name>')
      sys.exit()
    elif opt in ("-f", "--file_name"):
      file_name = arg
  print('File name is ', file_name)
  company_list = []
  company_list = parse(file_name)
  #print header
  pprint('COMPANY | JAVA | SKILLS COUNT | JOBS COUNT | POST CODE | DISTANCE | MAPS URL '
  company_list.sort(key=lambda x: x.distance_from_home, reverse=False)
  for company in company_list:
    company.print_short
	company.write_json
  print('done')

if __name__ == "__main__":
  main(sys.argv[1:])