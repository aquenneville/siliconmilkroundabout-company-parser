from pprint import pprint
import json
import io

Class Company:

  name = ""
  description = ""
  post_code = ""
  skills_list = []
  jobtitles_list = []
  uses_java = False
  distance_from_home = 0
  maps_url = ""
  
  def __init__(self, name, description, post_code, skills_list, jobtitles_list, uses_java, distance_from_home, maps_url):
    self.name = name
	self.description = description
	self.post_code = post_code
	self.skills_list = skills_list
	self.jobtitles_list = jobtitles_list
	self.uses_java = uses_java
	self.distance_from_home = distance_from_home
	self.maps_url = maps_url
  
  def __init__(self, map):
    self.name = map['name']
	self.post_code = map['post_code']
	self.skills_list = map['skills_list']
	self.jobtitles_list = map['jobtitle_list']
	self.uses_java = map['uses_java']
	self.distance_from_home = map['distance_from_home']
	self.maps_url = map['maps_url']
	
  def print_short(self):
    print(' name: ' + self.name + ' uses java: ' + self.uses_java + ' skills count: ' + len(skills_list) + ' job count: ' + len(self.jobtitle_list) + ' post_code: ' + self.post_code + ' distance: ' + distance_from_home + ' maps url: ' + self.maps_url)

  def write_json(self):
    with open(self.name+'.txt', 'w', encoding='utf8') as outfile:
      str_ = json.dumps(self,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
  