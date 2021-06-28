import GraphDistance
import logging
import timeit

import UnitTest

logger = logging.getLogger()
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')

# Create formatters and add it to handlers
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)    # Handler for writing logs in console
f_handler.setFormatter(f_format)    # Handler for writing logs in file
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.setLevel(logging.INFO)       # Setting logger level at info


def compute_time():
    graphDist = GraphDistance.GraphDistance().calculate_distance(logger)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    logger.warning(f'START time : {str(start_time)}')
    compute_time()
    logger.warning(f'END time : {str(timeit.default_timer())}')
    logger.critical(f'TOTAL time taken : {str(timeit.default_timer() - start_time)}')
    unitTest = UnitTest.TestGraphDistance()
    unitTest.run_test_cases()
    logger.critical(f'All Test classes executed')

