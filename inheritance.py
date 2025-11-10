class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def get_shift_number(self):
        return self.__shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


def main():
    print("Answer the following questions")
    print("--------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number: "))

    worker = ProductionWorker(name, number, shift_number, pay_rate)

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    if worker.get_shift_number() == 1:
        print("Shift: Day")
    else:
        print("Shift: Night")
    print("Pay Rate:", worker.get_hourly_pay_rate())


main()
