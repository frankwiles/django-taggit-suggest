#!/usr/bin/env python
import sys

from os.path import dirname, abspath

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASE_NAME='test.db',
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'taggit',
            'taggit_suggest',
        ]
    )

from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['taggit_suggest']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
