from timeloop import Timeloop
from datetime import timedelta
import time
import numpy as np
import logging


def register_virtual_device(socketio):
    """
    Register the virtual device callback to get invoked periodically.
    :param socketio:
    :return:
    """
    tl = Timeloop()
    tl._add_job(send_event, interval=timedelta(seconds=1), args={'socketio': socketio})
    # @tl.job(interval=timedelta(seconds=1))
    # def on_e_bike_event_received():
    #     return send_event(socketio)
    return tl.start()


def send_event(args):
    """
    Mimics as virtual device which generates the reading and broadcast the reading to all
    connected socket
    :return:None
    """
    socketio = args.get('socketio', None)
    if not socketio:
        logging.warning('No socket object to publish virtual device reading')
        return None

    current_speed = np.random.randint(100)
    event_name = 'speed_change'
    payload = {
        'speed': current_speed,
        'ts': int(time.time()) * 1000,
        'text': 'Server log id - {0}'.format(current_speed)
    }
    logging.info('Sending: {}\t{}'.format(event_name, current_speed))
    socketio.emit(event_name, payload)
    return None
