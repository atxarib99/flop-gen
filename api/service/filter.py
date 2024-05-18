
class Filter:

    @staticmethod
    def get_filters():
        return [{'name': 'texture', 'description': 'Flop texture', 'options': ['rainbow', 'two tone', 'monotone']}]

    @staticmethod
    def get_filter(name):
        return {'name': name, 'description': 'Flop texture', 'options': ['rainbow', 'two tone', 'monotone']}
