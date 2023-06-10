class System_block:
    def __init__(self):
        super().__init__()
        self.memory = "Samsung SSD 4Tb"
        self.video_card = "NVIDIA GeForce RTX 3060Ti"
        self.processor = "AMD Ryzen 7 5800x 8-Core"


class Display:
    def __init__(self):
        super().__init__()
        self.monitor = "Aorus 240Hz 24'' "

class Keyboard:
    def __init__(self):
        super().__init__()
        self.keyboard = "Logitech Gaming PRO"

class Headphones:
    def __init__(self):
        super().__init__()
        self.headphones = "Logitech G PRO X"

class Mouse:
    def __init__(self):
        super().__init__()
        self.mouse = "Razer Viper Ultimate"




class PC(Display, System_block, Keyboard, Headphones, Mouse):
    def print_info(self):
        print(self.monitor)
        print(self.memory)
        print(self.video_card)
        print(self.processor)
        print(self.keyboard)
        print(self.headphones)
        print(self.mouse)


MyPC = PC()
MyPC.print_info()



