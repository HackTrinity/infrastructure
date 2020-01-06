def range_(n):
    return list(range(n))

class FilterModule:
    def filters(self):
        return {
            'range': range_
        }
