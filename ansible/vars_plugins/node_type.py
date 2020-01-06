import runpy

from ansible.inventory.host import Host
from ansible.plugins.vars import BaseVarsPlugin

common = runpy.run_path('module_utils/hacktrinity.py')

class VarsModule(BaseVarsPlugin):
    def get_vars(self, loader, path, entities):
        if not entities or len(entities) > 1 or not isinstance(entities[0], Host):
            return {}

        match = common['NODE_REGEX'].match(entities[0].get_name())
        if not match:
            return {}

        return {
            'ht_node': {
                'type': match.group('type'),
                'id': int(match.group('id'))
            }
        }
