"""
Rob Marchetti - where_am_i.py
Description: Find out where you are located based on your ip address
"""
from urllib import request
import json


def where_am_i():
    """Find City, Region and Lat/lon."""
    data = json.load(request.urlopen("http://ipinfo.io/json"))
    return (("You are close to:\t{city}, {region}, {country}\n".format(**data) +
            "\t\t\t\t\tLAT/LON: {}E ".format(data['loc'])))




#print(where_am_i())