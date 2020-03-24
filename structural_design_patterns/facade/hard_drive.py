class HardDrive:
    def read(self, lba, size):
        print(f"Some data from sector {lba} with size {size}")

    def write(self, data):
        print(f"Saving data {data}")

    def read_boot_loader(self):
        print(f"Reading boot loader...")
