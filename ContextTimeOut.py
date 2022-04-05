import errno
import contextlib
import ctypes
import threading

class TimeoutException(IOError):
    errno = errno.EINTR

@contextlib.contextmanager
def time_limit(timeout_secs):
    timeout_event = threading.Event()
    timer = threading.Timer(timeout_secs, lambda : timeout_event.set())
    timer.setDaemon(True)
    timer.start()
    try:
        yield timeout_event
    finally:
        timer.cancel()
        timer.join()