import functools


def authenticated_only(f):
    """
    A decorator function to authenticate the user events.
    :param f:
    :return:
    """
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # Todo: Will put validation logic here. Ex - JWT or Cookie validation.
        return f(*args, **kwargs)
    return wrapped
