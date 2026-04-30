import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):

        func_name = func.__name__

        if args:
            pos_params = list(args)
        else:
            pos_params = "none"

        # keyword args
        if kwargs:
            kw_params = kwargs
        else:
            kw_params = "none"

        
        result = func(*args, **kwargs)

        # logging
        logger.info(f"function: {func_name}")
        logger.info(f"positional parameters: {pos_params}")
        logger.info(f"keyword parameters: {kw_params}")
        logger.info(f"return: {result}")

        return result

    return wrapper

@logger_decorator
def hello():
    print("Hello, World!")
    
@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def check_kwargs(**kwargs):
   return logger_decorator

if __name__ == "__main__":
    hello()
    check_args(1, 2, 3)
    check_kwargs(a=1, b=2)
    
