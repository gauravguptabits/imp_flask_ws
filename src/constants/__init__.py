import os
from dotenv import load_dotenv

from .development import config as dev_config
from .production import config as prod_config
from .staging import config as stag_config

load_dotenv()

current_env = os.getenv('FLASK_ENV')

if current_env == 'development':
    # assign dev config
    config = dev_config
elif current_env == 'staging':
    # assign stag config
    config = stag_config
elif current_env == 'production':
    # assign prod config
    config = prod_config

