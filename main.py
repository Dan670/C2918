class system_block:
    def __init__(self):
        super().__init__()
        self.memory = "Samsung SSD 4Tb"
        self.video_card = "NVIDIA GeForce RTX 3060Ti"
        self.processor = "AMD Ryzen 7 5800x 8-Core"


class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "Aorus 240Hz 24'' "

class keyboard:
    def __init__(self):
        super().__init__()
        self.resolution = "Logitech Gaming PRO"

class headphones:
    def __init__(self):
        super().__init__()
        self.resolution = "Logitech G PRO X"

class mouse:
    def __init__(self):
        super().__init__()
        self.resolution = "Razer Viper Ultimate"




class PC(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)
        print(self.video_card)
        print(self.processor)


HyperPC = PC()
HyperPC.print_info()



