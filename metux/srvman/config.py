import yaml

class Config:
    def __init__(self, fn):
        with open(fn, 'r') as stream:
            try:
                self.cf = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_name(self):
        return self.cf['name']

    def get_description(self):
        return self.replace_vars(self.cf['description'])

    def get_type(self):
        return self.cf['service']['type']

    ## fixme: only using defaults
    def replace_vars(self, s):
        if type(s) == type(True):
            return s

        for n in self.cf['vars']:
            if 'name' in n:
                if 'default' in n:
                    val = n['default']
                else:
                    val = ''
                s = s.replace('${vars:'+n['name']+'}', str(val))
        return s

    def get_service_attr(self, attr):
        if attr not in self.cf['service']:
            return ''
        return self.replace_vars(self.cf['service'][attr])

    def get_service_bool(self, attr):
        b = self.get_service_attr(attr)
        if type(b) == type(True):
            return b
        return (b == 'yes' or b == 'on' or b == 'true')

    def get_service_args(self):
        if 'args' not in self.cf['service']:
            print "service missing args"
            return []

        l = []
        for a in self.cf['service']['args']:
            l.append(self.replace_vars(a))
        return l
