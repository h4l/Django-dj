#!/usr/bin/env python
# Save this as 'dj' and put it somewhere on your PATH (e.g. ~/bin).
#
# Usage: $ dj [manage.py args ...]
# 
# Locates a manage.py file in a parent of the current directory and executes it
# with the arguments to this script.
import os
from os import path
import sys
import subprocess

def find_in_parent_dirs(dir, filename):
    if filename in os.listdir(dir):
        return path.join(dir, filename)
    
    parent_dir = path.dirname(dir)
    if parent_dir == dir:
        return None
    return find_in_parent_dirs(parent_dir, filename)

def run_manage_py(path, args):
    sys.exit(subprocess.call([path] + args, 
            stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr))
        
if __name__ == "__main__":
    search_start = os.getcwd()
    
    manage_py_path = find_in_parent_dirs(search_start, "manage.py")
    if not manage_py_path:
        print >> sys.stderr, ("Couldn't find 'manage.py' in '%s' or parent "
                "directories." % (search_start))
        sys.exit(1)
    
    try:
        run_manage_py(manage_py_path, sys.argv[1:])
    except Exception:
        print >> sys.stderr, "Error running command: '%s'" % manage_py_path
        print >> sys.stderr, "       with arguments: %s" % sys.argv[1:]
        print >> sys.stderr, "Python traceback follows..."
        print >> sys.stderr
        raise
