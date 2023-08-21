import logging

import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S',
    filename="ads_log.log",
    filemode="w"

)
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('Debug message')