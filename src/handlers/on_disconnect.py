from flask import current_app as app


def on_disconnect(socketio=None):
    app.logger.info('User connected')
    return
