
import subprocess
from service_base import ServiceBase

class ServiceSimple(ServiceBase):
    def __init__(self, cf):
        self.cf = cf
        self.verbose = False

    def _call(self, args):
        cmd = [ 'start-stop-daemon', '--pidfile', self.get_pidfile() ]

        if self.verbose:
            cmd += '--verbose'

        return subprocess.call(cmd+args)

    def _opt_mkpidfile(self):
        if not self.cf.get_service_bool('auto-pidfile'):
            return [ '--make-pidfile', '--remove-pidfile' ]
        return []

    def _opt_exec(self):
        return [ '--exec', self.cf.get_service_attr('program') ]

    def _opt_background(self):
        if not self.cf.get_service_bool('auto-background'):
            return [ '-b' ]
        return []

    def start(self):
        return self._call(
            [ '--start' ] +
            self._opt_mkpidfile() +
            self._opt_background() +
            self._opt_exec() +
            self.cf.get_service_args())

    def stop(self):
        return self._call(
            [ '--stop', '--oknodo' ] +
            self._opt_mkpidfile() + self._opt_exec())
