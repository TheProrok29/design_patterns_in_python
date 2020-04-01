import time


class Engine:
    def __init__(self, type_):
        if type_ == 'gasoline':
            time.sleep(3)
        elif type_ == 'diesel':
            time.sleep(5)
        else:
            time.sleep(4)
        print('Engine created')
