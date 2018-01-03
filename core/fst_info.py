import logging
import tempfile

from .process_runner import ProcessRunner

logger = logging.getLogger(__name__)

class FstInfo:
    def __init__(self, path='bin/fstinfo'):
        self._path = path

    def get_info(self, fst_bytes):
        params = [self._path]
        runner = ProcessRunner(params)
        runner.run(fst_bytes)
        output = runner.get_stdout()
        error = runner.get_stderr()
        logger.debug(output)
        logger.debug(error)
        return output
