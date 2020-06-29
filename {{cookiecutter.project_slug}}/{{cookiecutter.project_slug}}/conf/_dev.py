from ._base import {{cookiecutter.const_prefix}}_LOGGING

{{cookiecutter.const_prefix}}_DEVELOPMENT = True
# {{cookiecutter.const_prefix}}_LOGGING['root']['level'] = 'DEBUG'
{{cookiecutter.const_prefix}}_LOGGING['loggers']['{{cookiecutter.project_slug}}']['level'] = 'DEBUG'
