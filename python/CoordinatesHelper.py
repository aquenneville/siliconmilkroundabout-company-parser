import urllib.request
import json

Class PostcodeToCoordinateHelper:

	def convert(postcode):
		res = urllib.request.urlopen("http://api.postcodes.io/postcodes/SE18XX").read()
		data = json.loads(res)
		c = Coordinates(data["result"]["longitude"], data["result"]["latitude"])
		return c
	
	def createGoogleMapsLink(Coordinate x, Coordinate y):
	  # https://developers.google.com/maps/documentation/urls/guide
	  return "https://www.google.com/maps/dir/?api=1&origin="+x.latitude+","+x.longitude+"&destination="+y.latitude+","+y.longitude