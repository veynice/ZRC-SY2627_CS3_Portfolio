class CD:
    def __init__(self, announce):
        self.__announce = announce

    def talk(self):
        print("Walay klase")

    def announce(self):
        print(f"Announcement from {self.__announce}: Walay klase karong adlawa.")

class CurriculumImplementationDivision(CD):
    def __init__(self, announce):
        super().__init__(announce)
        self._signature = "Curriculum Implementation Division"
        self._proposal = "Your proposal has been approved."
        self._schoolCalendar = "The school calendar has been updated."
        self._examSchedule = "The exam schedule has been released."

    def sign(self):
        print("Gi pirmahaan na sa Curriculum Implementation Division.")

    def checks(self):
        print("Gi check na sa Curriculum Implementation Division ang inyong proposal.")

class StudentServicesDivision(CD):
    def __init__(self, announce):
        super().__init__(announce)
        self._residenceHall = "Student Services Division"
        self._guidanceCounselor = "Guidance and Counseling"

    def help(self):
        print("Nitabang ang Student Services Division sa pagdumala sa mga estudyante.")

    def guide(self):
        print("Nitabang ang Guidance and Counseling sa pagtabang sa mga estudyante.")

class SirGie(CurriculumImplementationDivision):
    def __init__(self, teacher):
        super().__init__(teacher)
        self.gwapo = "Sir Gie"

    def monitor(self):
        print("Nitabang og monitor si Sir Gie sa Lithium.")

class SirBon(CurriculumImplementationDivision):
    def __init__(self, potassium):
        super().__init__(potassium)
        self.pogi = "Sir Bon"

    def monitor(self):
        print("Nitabang og monitor si Sir Bon sa Potassium.")

class SirArt(CurriculumImplementationDivision):
    def __init__(self, sodium):
        super().__init__(sodium)
        self.bright = "Sir Art"

    def monitor(self):
        print("Nitabang og monitor si Sir Art sa Sodium.")

class Venice(SirGie):
    def __init__(self, student):
        super().__init__(student)
        self.smart = "Venice"

    def study(self):
        print("Nagtuon si Venice sa Math while ga announce si Campus Director.")

class Lovely(StudentServicesDivision):
    def __init__(self, chief):
        super().__init__(chief)
        self.lovely = "Lovely"

    def teach(self):
        print("Nagtudlo si Ma'am Lovely sa mga estudyante sa Math while ga announce si Campus Director.")

print("Campus Director Announcement:")
campus_director = CD("Campus Director")
campus_director.announce()