from functional.chain_of_responsibility.abstract_based_example.chain import Chain
from functional.chain_of_responsibility.abstract_based_example.director import Director
from functional.chain_of_responsibility.abstract_based_example.manager import Manager
from functional.chain_of_responsibility.abstract_based_example.secretary import Secretary
from functional.chain_of_responsibility.abstract_based_example.team_member import TeamMember
from functional.chain_of_responsibility.abstract_based_example.vice_director import ViceDirector
from functional.chain_of_responsibility.abstract_based_example.worker import Worker

my_chain = Chain()

my_chain.chain.append(Director())
my_chain.chain.append(ViceDirector())
my_chain.chain.append(Manager())
my_chain.chain.append(Secretary())
my_chain.chain.append(Worker())
my_chain.chain.append(TeamMember())

task = 'bring a tea'
my_chain.run_task(task)
