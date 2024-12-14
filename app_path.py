from os.path import dirname, abspath
import sys


def get_application_path() -> str:
    """
    Get the application path that works both in cx_Freeze executable mode
    and normal script mode.

    Returns:
        str: The absolute path to the application directory
    """
    if getattr(sys, "frozen", False):
        application_path = dirname(sys.executable)
    else:
        application_path = dirname(abspath(__file__))

    return application_path
