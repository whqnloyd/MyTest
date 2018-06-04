def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('begin call')
        time_begin = time.clock()
        result = fn(*args, **kwargs)
        print('end call')
        time_end = time.clock()
        print('%s executed in %s ms' % (fn.__name__, time_end - time_begin))
        return result

    return wrapper