#James Padula
#3/31/2026
#9.5 Login Attempts

class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0  

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

me = User('Your', 'Name')

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(f"Attempts: {me.login_attempts}") 

me.reset_login_attempts()
print(f"Reset: {me.login_attempts}")