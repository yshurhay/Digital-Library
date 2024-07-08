"""
WSGI config for afin_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
from pathlib import Path

from django.core.wsgi import get_wsgi_application

path_to_env = Path(__file__).parents[1].joinpath(".env")
dotenv.load_dotenv(dotenv_path=path_to_env)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

application = get_wsgi_application()
