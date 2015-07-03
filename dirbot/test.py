import json

class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s

obj = MyObj('helloworld')


def convert_to_builtin_type(obj):
    d = { '__class__':obj.__class__.__name__,
          '__module__':obj.__module__,
        }
    d.update(obj.__dict__)
    return d

print json.dumps(obj, default=convert_to_builtin_type)



def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)

        class_ = getattr(module,class_name)

        args = dict((key.encode('ascii'),value) for key,value in d.items())

        inst = class_(**args)
    else:
        inst = d
    return inst

encoded_object = '{"s": "helloworld", "__module__": "__main__", "__class__": "MyObj"}'

myobj_instance = json.loads(encoded_object,object_hook=dict_to_object)
print myobj_instance

