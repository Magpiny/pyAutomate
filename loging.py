import logging

# logging to view or debug errors in python
logging.basicConfig(filename='errorMssgs.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# DISABLE ALL CRITICAL ERROR MESSAGES
# logging.disable(logging.CRITICAL)

logging.debug("START PROGRAM")


def factorial(n):
    logging.debug("Start factorial (%s)" %(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.info("Return value is %s" %(total))
    return total


print(factorial(7))
logging.debug("END PROGRAM")

# DEBUGGING AND LOGGING IN PYTHON
