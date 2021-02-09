from flask import Flask, render_template
from flask_socketio import SocketIO
from logging.config import dictConfig

from src.constants import config
from src.common import authenticated_only, log_exception
from src.handlers import on_connect, on_disconnect, on_business_error, on_general_error

dictConfig(config.get('log_config', None))
app = Flask(__name__)
socketio = SocketIO(app,
                    cors_allowed_origins=config.get('websocket_server', {}).get('cors', None),
                    engineio_logger=config.get('DEEP_DEBUG', False),
                    logger=config.get('DEBUG', False))


@app.route('/')
def index():
    return render_template('login.html')


@socketio.on('connect')
@authenticated_only
def on_connect_event():
    """
    Trigger
    :return:
    """
    return on_connect(socketio)


@socketio.on('disconnect')
def on_disconnect_event():
    """
    Trigger disconnect event handler here.
    :return:
    """
    return on_disconnect()


@socketio.on_error()
@log_exception
def on_specific_error(e):
    """
    Trigger application error handler here.
    :param e:
    :return:
    """
    return on_business_error(e)


@socketio.on_error_default
@log_exception
def on_default_error(e):
    """
    Trigger general purpose handler here.
    :param e:
    :return:
    """
    return on_general_error(e)


def register_virtual_device(enable_virtual_device=False):
    """
    Spawn thread for virtual device.
    :return:
    """
    app.logger.info('Use Virtual device:\t'.format(enable_virtual_device))
    if enable_virtual_device:
        # selective import
        from src.virtual_device.ebike import register_virtual_device

        app.logger.info('Starting virtual device')
        register_virtual_device(socketio)
    return


if __name__ == '__main__':
    register_virtual_device(config.get('enable_virtual_device'))
    socketio.run(app,
                 host=config.get('server', {}).get('host', None),
                 port=config.get('server', {}).get('port', None),
                 log_output=config.get('DEBUG', False),
                 use_reloader=False,
                 debug=config.get('DEBUG', False))


