class Chain:
    def __init__(self):
        self.chain = []

    def run_task(self, task):
        for link in self.chain:
            result = link.process(task)
            if result:
                break
