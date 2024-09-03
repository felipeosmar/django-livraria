"""
Extract heavy logic from project_name/settings.py, manage.py and wsgi.py
"""

import logging

from django.conf import settings
from django.utils.module_loading import import_string


class CustomLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        messages = []
        data = kwargs.get("extra", {})
        for key, value in sorted(data.items()):
            if "pass" in key:
                value = "*" * 6

            messages.append("{}={!r}".format(key, value))
        return "{} {}".format(msg, ", ".join(messages)), kwargs


def get_logger(name):
    return CustomLoggerAdapter(logging.getLogger(name), {})


def get_project_package(project_dir):
    if (project_dir / "project_name").exists():
        return "project_name"
    return "app"


DEFAULT_SETTINGS = {}


def get_configuration(name):
    return getattr(settings, name.upper(), DEFAULT_SETTINGS.get(name))


def get_object_from_configuration(name):
    return import_string(get_configuration(name))
