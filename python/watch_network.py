import logging
from enum import Enum
from time import time
import socket



class Sites(Enum):
    MODEM = ("192.168.0.1", 80)
    ROUTER_BACKED_PI = ("192.168.0.100", 1022)
    SOMETHING_NAMED = ("doihaveinter.net", 80)
    UPSTAIRS_ROUTER = ("192.168.0.100", 8080)
    SOMETHING_REMOTE = ("1.1.1.1", 80)


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler = logging.FileHandler('/var/log/connection_monitoring')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



def is_connection_to_site_up(address, port) -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((address, port))
        return True
    except:
        print("Connection error")
        return False
    finally:
        s.close()

def main():
    log = get_logger()
    next_run = time()
    while True:
        if next_run < time():
            next_run += 60
            for site in Sites:
                site_available = is_connection_to_site_up(site.value[0], site.value[1])
                log.info(f"{site.name} at {site.value} is {'up' if site_available else 'down'}")


if __name__ == "__main__":
    main()