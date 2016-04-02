# json decoder
import simplejson as json


def find_values(id, id2, obj):
    results = []

    def _find_values(id, obj):
        try:
            for key, value in obj.iteritems():
                if value == id:
                    results.append(obj)
                elif not isinstance(value, basestring):
                    _find_values(id, value)
        except AttributeError:
            pass

        try:
            for item in obj:
                if not isinstance(item, basestring):
                    _find_values(id, item)
        except TypeError:
            pass

    if not isinstance(obj, basestring):
        _find_values(id, obj)

    def _find_hostname(id, obj):
        for item in obj:
            if item.get(id2):
                return item.get(id2)
    return _find_hostname(id, results)


def final_parser(id, obj):
    for item in obj:
        if item.get('hostname'):
            return item.get('hostname')


if __name__ == "__main__":
    data = {"name": "mayank", "hostname": "mayank-test"}
    some_dict =  find_values('mayank', "hostname", data)
    print some_dict