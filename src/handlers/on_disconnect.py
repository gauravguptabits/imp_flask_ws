from flask import current_app as app
from flask_socketio import disconnect


def on_disconnect(socketio=None):
    disconnect()
    app.logger.info('###### User Disconnected ##########')
    return
