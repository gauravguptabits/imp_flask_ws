import functools
from flask import current_app as app


def log_exception(f):
    """
    A decorator function to authenticate the user events.
    :param f:
    :return:
    """
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        app.logger.exception('onSpeedError: An error occurred')
        return f(*args, **kwargs)
    return wrapped
