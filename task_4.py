class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours == None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email == None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment
    
emp = EmployeeSalary.get_hours("Ivan", rest_days=2)
print(emp.hours)          # 40 (потому что (7-2)*8)
print(emp.salary())       # 16000 (40 * 400)

# Генерируем email, если он не задан
emp_with_email = EmployeeSalary.get_email("Maria")
print(emp_with_email.email)  # Maria@email.com

# Меняем ставку оплаты
EmployeeSalary.set_hourly_payment(500)
print(emp.salary())       # Тепе