"""linting code"""
import os
import sys
import pylint.epylint

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
PACKAGE = os.path.join(SCRIPT_DIR, "./")

def run_lint():
    """ linting code function"""
    config_file = os.path.realpath(os.path.join(SCRIPT_DIR, "pylintrc"))
    return_code = pylint.epylint.lint(PACKAGE, ['--rcfile={}'.format(config_file)])
    if return_code:
        return False
    return True

if __name__ == "__main__":
    sys.exit(0 if run_lint() else 1)
