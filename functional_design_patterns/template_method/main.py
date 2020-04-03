from functional_design_patterns.template_method.accountant import Accountant
from functional_design_patterns.template_method.secretary import Secretary

secretary = Secretary('Marie')
accountant = Accountant('Elen')

secretary.work_day()
print('////////')
accountant.work_day()
