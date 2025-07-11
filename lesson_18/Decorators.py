import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()


def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper


if __name__ == '__main__':
    @log_args_and_result
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("User", greeting="Welcome"))