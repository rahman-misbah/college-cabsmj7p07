class Student:
    def __init__(self, name:str, student_id:str) -> None:
        self._name = name
        self._student_id = student_id

    def get_details(self) -> None:
        print("Name:", self._name)
        print("Student ID:", self._student_id)

class GraduateStudent(Student):
    def __init__(
            self, 
            name:str,
            student_id:str, 
            thesis_topic:str
            ) -> None:

        super().__init__(name, student_id)
        self._thesis_topic = thesis_topic

    def get_details(self) -> None:
        super().get_details()
        print("Thesis Topic:", self._thesis_topic)

if __name__ == "__main__":
    student = Student("Misbah", "23CABSA539")
    grad_student = GraduateStudent("Maria", "23CABSA176", "Cyber Security")

    student.get_details()
    print()
    grad_student.get_details()