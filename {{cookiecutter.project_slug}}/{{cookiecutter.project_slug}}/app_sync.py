import logging

from . import conf

_logger = logging.getLogger('{{cookiecutter.project_slug}}.app')


def main():
    try:
        _logger.info('starting')
        # TODO

    except KeyboardInterrupt:
        pass
    except Exception as err:
        _logger.critical(str(err))
    finally:
        _logger.info('shutting')


if __name__ == '__main__':
    main()
