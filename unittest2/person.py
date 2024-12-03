
class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def get_fullname(self) -> str:
        return f'{self.fname} - {self.lname}'

    def create_email(self):
        