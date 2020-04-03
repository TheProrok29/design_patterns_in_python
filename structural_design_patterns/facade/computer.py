from structural_design_patterns.facade.cpu import CPU
from structural_design_patterns.facade.hard_drive import HardDrive
from structural_design_patterns.facade.memory import Memory
from structural_design_patterns.facade.motherboard import Motherboard


class Computer:
    def __init__(self):
        self.cpu = CPU(4, 4000, 16, 'ABCD')
        self.memory = Memory()
        self.hard_drive = HardDrive()
        self.motherboard = Motherboard(
            self.cpu, self.memory, self.hard_drive, 8, ['jack', 'power', 'hdmi'], (30, 30)
        )

    def start(self):
        self.cpu.freeze()
        self.memory.load('0x00', self.hard_drive.read('100', '1024'))
        self.hard_drive.read_boot_loader()
        self.cpu.jump('0x00')
        self.cpu.execute()
