import os
import sys

sys.path = ["", ".."] + sys.path[1:]
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.common")
django.setup()
from core import logger
from core.scripts import perform

script_names = (
    'admins', 'genres', 'books', 'authors', 'comments', 'ratings', 'libraries', 'book_instances', 'user_libraries')

PERFORM_FUNC_NAME = "perform"
SCRIPTS_PATH = "scripts.seeds"

if __name__ == "__main__":
    try:
        perform(sys.argv, SCRIPTS_PATH, script_names, PERFORM_FUNC_NAME, True)
    except IndexError:
        logger.error("Pass script name to to arguments")
