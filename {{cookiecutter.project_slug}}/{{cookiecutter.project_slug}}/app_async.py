import asyncio
import logging

from . import conf
from .utils.app_utils import on_startups, on_shutdowns, init_on_terminate, OnTerminate

_logger = logging.getLogger('{{cookiecutter.project_slug}}.app')


def main():
    loop = asyncio.get_event_loop()
    init_on_terminate(loop)

    try:
        _logger.info('starting')
        loop.run_until_complete(on_startups.run())
        # TODO

        loop.run_forever()
    except (KeyboardInterrupt, OnTerminate):
        pass
    except Exception as err:
        _logger.critical(str(err))
    finally:
        _logger.info('shutting')
        loop.run_until_complete(on_shutdowns.run())

    loop.close()


if __name__ == '__main__':
    main()