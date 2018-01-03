import logging
import os

from core.constants.log_level import INFO, LOG_LEVEL_KEY
from core.fst_info import FstInfo
import tempfile
import base64
from subprocess import CalledProcessError

logger = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = INFO


def lambda_handler(event, context):
    log_level = os.environ.get(LOG_LEVEL_KEY)
    level_str = DEFAULT_LOG_LEVEL if log_level is None else log_level
    level = logging.getLevelName(level_str)
    logging.getLogger().setLevel(level)

    # Log the entire event for debugging.
    logger.debug(event)
    body = event['body']

    headers = {}
    headers['Content-Type'] = 'text/plain; charset=utf-8'

    fst_info = FstInfo()
    response = {}
    try:
        fst_binary = base64.b64decode(body)
        output = fst_info.get_info(fst_binary)
        logger.debug(output)
        response['statusCode'] = 200
        response['headers'] = headers
        response['body'] = output.decode('utf-8')
    except CalledProcessError as e:
        output = e.stderr.decode('utf-8') if e.stderr is not None else ''
        msg = 'fstinfo error ({}): {}'.format(e.returncode, output)
        logger.info('Client {}'.format(msg))
        response['statusCode'] = 400
        response['headers'] = headers
        response['body'] = msg
    except ValueError as e:
        logger.exception('ValueError caught')
        msg = 'content error: Payload should be base64 encoded'
        response['statusCode'] = 400
        response['headers'] = headers
        response['body'] = msg
    except:
        logger.exception('Unknown exception caught while getting FST info')
        response['statusCode'] = 500
        response['headers'] = headers
        response['body'] = 'Internal Server Error'
    return response
