
class Student:

    def __init__(self,student_id, name, age, score):
        self.id = student_id
        self.name = name
        self.age = age
        self.__score = 0
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            print(f"Invalid score for {self.name}: {value}")

    # Show thông tin học sinh.

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.get_grade()}")

    # Kiểm tra kết quả pass hay fail.

    def is_pass(self):
        if self.score >= 50:
            print(f"{self.name}: Pass")
        else:
            print(f"{self.name}: Fail")
        print("-" * 20)

    # Cập nhật điểm của học sinh.

    def update_score(self, new_score):
        self.score = new_score

    def get_grade(self):
        if self.score < 60:
            return "F"
        elif self.score < 70:
            return "D"
        elif self.score < 80:
            return "C"
        elif self.score < 90:
            return "B"
        else:
            return "A"