class Boss:

    def __init__(self, name: str, company: str):
        self.name = name
        self.company = company
        self.workers = []

    def employe(self, worker: 'Worker'):
        if isinstance(worker, Worker) and worker not in self.workers:
            self.workers.append(worker)

    @property
    def get_workers(self):
        return self.workers

    @get_workers.setter
    def get_workers(self, list_):
        self.workers = list_

    @property
    def get_company(self):
        return self.company

    @get_workers.setter
    def get_company(self,company):
        self.company = company

class Worker:

    def __init__(self, name: str):
        self.name = name
        self.company = ''
        self.boss = ''

    def get_employed(self, boss: Boss):
        if isinstance(boss, Boss):
            self.boss = boss
            self.company = boss.company


boss = Boss('ad', '1231')
worker = Worker('12312', )
boss.employe(worker)
print(boss.workers[0].name)
