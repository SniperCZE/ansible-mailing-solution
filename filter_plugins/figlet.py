# -*- coding: utf-8 -*-
#
# Simple figlet filter
#
# This filter uses Python implementation of figlet, pyfiglet. It also supports
# many different fonts that are packed with pyfiglet.
#

try:
  from pyfiglet import Figlet
except ImportError:
  Figlet = None

from ansible import errors


def figlet(text, font='standard', width=80, *args, **kwargs):
  if not Figlet:
    raise errors.AnsibleFilterError('The figlet filter requires pyfiglet module')
  formatter = Figlet(font=font, width=width)
  return formatter.renderText(text)


class FilterModule(object):
  filter_map =  {
    'figlet': figlet
  }

  def filters(self):
    return self.filter_map

