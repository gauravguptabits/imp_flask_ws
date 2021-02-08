from flask import current_app as app


def on_connect(socketio):
    app.logger.info('User connected')
    raise Exception('Has exception')
    # socketio.emit('connected', None)
    return
