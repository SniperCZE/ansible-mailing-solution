# -*- coding: utf-8 -*-

from ansible import errors
import os, re

#  y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF

def onoff(value, *args, **kwargs):
  if value == True or (isinstance(value, str) and value.lower() in ['y', 'yes', 'true', 'on']):
    return 'on'
  else:
    return 'off'


class FilterModule(object):
  filter_map =  {
    'onoff': onoff
  }

  def filters(self):
    return self.filter_map

