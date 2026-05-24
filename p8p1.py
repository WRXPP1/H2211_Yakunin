import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='p8p1.log',
                    filemode='w',
                    format='We have next logging message: %(asctime)s:%(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")