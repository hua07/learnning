class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(
            f'用户姓名{self.first_name} {self.last_name},性别：{self.gender}，年龄：{self.age}'
        )

    def greet_user(self):
        print(f'你好，{self.first_name} {self.last_name}')
    def read_login_attempts(self):
        print(f'现在共有{self.login_attempts}人尝试登录')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = User('王','华','男','18')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.read_login_attempts()
user.increment_login_attempts()
user.read_login_attempts()
user.increment_login_attempts()
user.read_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()