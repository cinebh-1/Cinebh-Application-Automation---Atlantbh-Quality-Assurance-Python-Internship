import json
# The DictObject is a utility class to access dictionary values using object notation
class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)
    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)
#From here we will feed data into our test
projection = DictObject.from_dict({
        'search_term': 'afterburn',
        'city': 'Sarajevo',
        'cinema': 'Meeting Point Cinema',
        'genre': 'Action',
        'time': '19:00'
})