
from metux.srvman.service_simple import ServiceSimple
from metux.srvman.config import Config
from metux.srvman import term

class SrvRunner:
    def __alloc(self, cf):
        t = cf.get_type()
        if t == 'simple':
            return ServiceSimple(cf)
        raise Exception("unsupported service type "+t)

    def __init__(self, cf):
        self.cf  = cf
        self.srv = self.__alloc(cf)

    def __print_ret(self, ret):
        term.bold()
        if ret == 0:
            term.mode('okgreen')
            term.write('OK\n')
        else:
            term.mode('fail')
            term.write('Failed\n')
        term.mode('reset')
        return ret

    def __print_srv(self):
        term.fgcolor('yellow')
        term.write(self.cf.get_name())
        term.reset()

    def start(self):
        term.write("Starting service: ")
        self.__print_srv()
        term.write(" ... ")
        return self.__print_ret(self.srv.start())

    def stop(self):
        term.write("Stopping service: ")
        self.__print_srv()
        term.write(" ... ")
        return self.__print_ret(self.srv.stop())

    def run(self, op):
        if op == 'start':
            return self.start()
        if op == 'stop':
            return self.stop()
        if op == 'reload':
            return self.reload()
        if op == 'restart':
            return self.restart()
        return 23;

def get(cf):
    return SrvRunner(cf)

def load(cfn):
    return get(Config(cfn))
