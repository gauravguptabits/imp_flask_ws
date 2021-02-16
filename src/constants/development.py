import os
from dotenv import load_dotenv
load_dotenv()

config = {
    'DEBUG': False,
    'DEEP_DEBUG': False,
    'SECRET_KEY': 'my precious',
    'enable_virtual_device': True,
    'db': {

    },
    'websocket_server': {
        'cors': '*'
    },
    'server': {
        'host': '0.0.0.0',
        'port': 5000,
    },
    'log_config': {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "default",
                "filename": os.path.join(os.getcwd(), 'log', "info.log"),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "default",
                "filename": os.path.join(os.getcwd(), 'log', "errors.log"),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi', 'info_file_handler', 'error_file_handler']
        }
    }
}
