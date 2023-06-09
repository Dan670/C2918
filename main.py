class Football_club:
    def __init__(self):
        super().__init__()
        self.students1 = "90 students"
        self.teachers1 = "3 teachers"
        self.balls1 = "10 balls"


class Baseball_club:
    def __init__(self):
        super().__init__()
        self.students2 = "90 students"
        self.teachers2 = "3 teachers"
        self.balls2 = "100 balls"
        self.bats = "30 bats"


class School(Football_club, Baseball_club):
    def print_info(self):
        print(self.students1)
        print(self.teachers1)
        print(self.balls1)
        print(self.students2)
        print(self.teachers2)
        print(self.balls2)
        print(self.bats)
