
class ServiceBase:
    def start(self):
        raise "do_start() not implemented"

    def stop(self):
        raise "do_stop() not implemented"

    def get_pidfile(self):
        return '/var/run/'+self.cf.get_name()+'.pid'
