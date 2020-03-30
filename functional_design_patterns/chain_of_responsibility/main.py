from chain import Chain
from director import Director
from manager import Manager
from secretary import Secretary
from team_member import TeamMember
from vice_director import ViceDirector
from worker import Worker

my_chain = Chain()

my_chain.chain.append(Director())
my_chain.chain.append(ViceDirector())
my_chain.chain.append(Manager())
my_chain.chain.append(Secretary())
my_chain.chain.append(Worker())
my_chain.chain.append(TeamMember())

task = 'bring a tea'
my_chain.run_task(task)
