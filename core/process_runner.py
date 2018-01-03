import logging
from subprocess import PIPE, run

logger = logging.getLogger(__name__)

class ProcessRunner:
    def __init__(self, args=None):
        self._args = [] if args is None else args
        logger.info("Executing subprocess with args: {}".format(self._args))

    def run(self, input_stream):
        self._result = run(self._args,
                           input=input_stream,
                           stdout=PIPE,
                           stderr=PIPE)
        self._result.check_returncode()

    def get_stdout(self):
        return self._result.stdout

    def get_stderr(self):
        return self._result.stderr
