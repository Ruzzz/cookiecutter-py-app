{{cookiecutter.const_prefix}}_DEVELOPMENT = False
{{cookiecutter.const_prefix}}_TESTING = False

{{cookiecutter.const_prefix}}_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['console']
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s | %(process)d | %(name)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '{{cookiecutter.project_slug}}': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        }
    }
}
