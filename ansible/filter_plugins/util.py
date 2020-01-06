import runpy

common = runpy.run_path('module_utils/hacktrinity.py')

class FilterModule:
    def filters(self):
        return {
            'range': lambda n: list(range(n)),
            'ht_type': lambda n: common['NODE_REGEX'].match(n).group('type'),
            'ht_id': lambda n: int(common['NODE_REGEX'].match(n).group('id'))
        }
