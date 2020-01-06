import re

NODE_REGEX = re.compile('^(?P<type>(manager|worker))(?P<id>\\d+)$')
