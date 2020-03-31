from observer import Observer


class Manager(Observer):
    def notify(self, *args, **kwargs):
        worker = kwargs['worker']
        if args[0] > 70:
            print(f'I need to search some work for {worker}')
        else:
            print(f'Worker {worker} still works.')
