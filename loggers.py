from datetime import datetime


def logger(func):

    def func_wrapper(*args, **kwargs):

        file_name = 'logs.txt'
        start_time = datetime.now()
        result = func(*args, **kwargs)
        running_time = datetime.now() - start_time

        with open(file_name, 'a') as file:
            file.write(f'Date: {datetime.today()}, Name: {func.__name__}, Arguments: {args}, {kwargs}, Result: {result}, Execution time: {running_time} \n')
        return result

    return func_wrapper


def logger_with_path(path):
    def logger(func):
        def func_wrapper(*args, **kwargs):
            file_name = 'logs.txt'
            start_time = datetime.now()
            result = func(*args, **kwargs)
            running_time = datetime.now() - start_time

            with open(str(path + file_name), 'a') as file:
                file.write(
                    f'Date: {datetime.today()}, Name: {func.__name__}, Arguments: {args}, {kwargs}, Result: {result}, Execution time: {running_time} \n')
            return result
        return func_wrapper
    return logger