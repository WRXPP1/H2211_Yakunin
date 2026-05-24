import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='p8p2.log',
                    filemode='w',
                    format='We have next logging message: %(asctime)s:%(levelname)s - %(message)s')

try:
    print(10/0)
except Exception:
    logging.exception("Exception")