from other.dependency_injection.computer import *
from other.dependency_injection.processor import *

amd_computer = Computer(AMDProcessor())
intel_computer = Computer(IntelProcessor())
arm_computer = Computer(ARMProcessor())

print(amd_computer)
print(intel_computer)
print(amd_computer)
