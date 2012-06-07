#!/usr/bin/env python
# Copyright (c) 2012, Hal Blackburn <hwtb2@caret.cam.ac.uk>,
#                     CARET <http://www.caret.cam.ac.uk/>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Save this as 'dj' and put it somewhere on your PATH (e.g. ~/bin).
#
# Usage: $ dj [manage.py args ...]
# e.g.:
#     $ dj runserver
# 
# Locates a manage.py file in a parent of the current directory and executes it
# with the arguments to this script.
import os
from os import path
import sys
from django.core.management import execute_from_command_line

DJANGO_SETTINGS_MODULE = "DJANGO_SETTINGS_MODULE"

DJANGO_SETTINGS_FILE = "settings.py"
DJANGO_URLS_FILE = "urls.py"
PYTHON_INIT_FILE = "__init__.py"

DJANGO_PROJECT_DIR_FILES = set(
        [DJANGO_SETTINGS_FILE, DJANGO_URLS_FILE, PYTHON_INIT_FILE])

def is_django_project_dir(path):
    """Determines if a directory seems to be a Django project dir."""
    # Check if the set of files in the dir at path are a superset of the files
    # which a dir must contain for it to be considered a Django project. 
    return set(os.listdir(path)) >= DJANGO_PROJECT_DIR_FILES

def find_parent_dir(dir_path, predicate):
    if predicate(dir_path):
        return dir_path

    parent_dir = path.dirname(dir_path)
    if parent_dir == dir_path:
        return None
    return find_parent_dir(parent_dir, predicate)

def default_settings_module(django_project_dir):
    return "%s.settings" % path.basename(django_project_dir)

def ensure_settings_exists(settings_module):
    try:
        __import__(settings_module)
    except NameError:
        print >> sys.stderr, ("Could not import settings module: %s" %
                settings_module)
        print >> sys.stderr, ("Python traceback follows:")
        print >> sys.stderr
        raise

def run_manage(django_project_dir, args):
    assert django_project_dir == path.abspath(django_project_dir)
    # Set a default value for the settings module envar
    os.environ.setdefault(DJANGO_SETTINGS_MODULE,
            default_settings_module(django_project_dir))

    # Setup the sys path as it would be when running from manage.py in the
    # parent dir of a Django project 
    project_parent = path.dirname(django_project_dir)
    sys.path.insert(0, project_parent)

    # Get the settings module to use and ensure it exists...
    settings_module = os.environ.get(DJANGO_SETTINGS_MODULE)
    ensure_settings_exists(settings_module)

    # Run the management tool
    execute_from_command_line(sys.argv)

def no_project_found(search_start):
    print >> sys.stderr, ("Error: Couldn't find a Django project in '%s' or "
            "parent directories." % (search_start))
    print >> sys.stderr, ("  A dir is considered a Django project if it "
            "contains the files:")
    for filename in sorted(DJANGO_PROJECT_DIR_FILES):
        print >> sys.stderr, "    - %s" % filename

if __name__ == "__main__":
    search_start = os.getcwd()

    # find the closest Django project dir in or above the current dir
    django_project_dir = find_parent_dir(search_start, is_django_project_dir)
    if not django_project_dir:
        no_project_found(search_start)
        sys.exit(1)

    run_manage(django_project_dir, sys.argv)

