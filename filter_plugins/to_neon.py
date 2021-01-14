# -*- coding: utf-8 -*-

from ansible import errors
import os, re


def format_list(list_, indent_level, indent_symbol='  ', old_format=False, in_list=False):
  indent = indent_symbol * indent_level

  list_ = sorted(list_)

  if old_format:
    result = '{}[{}{}{}{}]'.format(
      indent,
      os.linesep,
      os.linesep.join([
        '{}{}'.format(indent + indent_symbol, to_neon(value, indent_level + 1, old_format=old_format, in_list=True))
        for value in list_
        ]),
      os.linesep,
      indent)
  else:
    result = os.linesep.join([
      '{}- {}'.format(indent, to_neon(value, indent_level + 1, old_format=old_format, in_list=True))
      for value in list_
    ])

  return '{}{}'.format(os.linesep, result)


def format_dict(dict_, indent_level, indent_symbol='  ', old_format=False, in_list=False):
  indent = indent_symbol * indent_level

  if old_format and in_list:
    result = '[{}{}{}{}]'.format(
      os.linesep,
      os.linesep.join([
        '{}{}: {}'.format(indent + indent_symbol, key, to_neon(value, indent_level + 1, old_format=old_format))
        for key, value in sorted(dict_.items())
        ]),
      os.linesep,
      indent)

    if not in_list:
      result = '{}{}'.format(indent, result)

  else:
    result = os.linesep.join([
      '{}{}: {}'.format(indent, key, to_neon(value, indent_level + 1, old_format=old_format))
      for key, value in sorted(dict_.items())
    ])

  if not in_list:
    result = '{}{}'.format(os.linesep, result)

  return result


def to_neon(value, indent_level=0, indent_symbol='  ', old_format=False, in_list=False, *args, **kwargs):
  if isinstance(value, dict):
    return '{}'.format(format_dict(value, indent_level, indent_symbol, old_format=old_format, in_list=in_list))
  elif isinstance(value, list):
    return '{}'.format(format_list(value, indent_level, indent_symbol, old_format=old_format, in_list=in_list))
  elif value is None:
    return 'Null'

  if re.search('[\[\]{}()<>\/*\-\+\?\^\'\":=]', str(value)):
    if re.search('[\']', str(value)):
      return '"{}"'.format(str(value))
    return "'{}'".format(str(value))
  return str(value)


class FilterModule(object):
  filter_map =  {
    'to_neon': to_neon
  }

  def filters(self):
    return self.filter_map

