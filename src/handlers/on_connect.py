from flask import current_app as app
import time


def on_connect(socketio):
    app.logger.info('########### User connected ###########')
    time.sleep(2)
    socketio.emit('connected', None)
    return None
