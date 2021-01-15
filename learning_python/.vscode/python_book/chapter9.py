#第九章  类
#类的格式：
class Dog():
    """ 一次模拟小狗的简单尝试 """
    def __init__(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗被命令蹲下 """
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('luck', 4)

print(f'my dog name is{my_dog.name.title()},it is {my_dog.age}yeas old')
my_dog.sit()
my_dog.roll_over()


#动手试一试
#9-1餐馆：创建一个名为Restaurant的类，其方法__init__（）设置两个属性：restaurant_name 和 cuisine_type
#创建一个名为describe_restautant()的方法和一个名为，open_restaurant()的方法，其中前者打印前述两项
#信息，而后者打印一条信息，指出餐馆正在营业。
#根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restautant(self):
        print(
            f'这个餐厅的名字是{self.restaurant_name.title()},专门售卖{self.cuisine_type.title()}'
        )

    def open_resturant(self):
        print(f'{self.restaurant_name.title()}正在营业中')


restaurant = Restaurant('肯德基', '熟食')
print(f'这个餐馆的名字是：{restaurant.restaurant_name},主要营业的是{restaurant.cuisine_type}')
restaurant.describe_restautant()
restaurant.open_resturant()

#9-2 三家餐馆：根据你完成9-1的实例，并对每个每个实例调用方法describe_restaurant()。
restaurant1 = Restaurant('必胜客', '快餐')
restaurant1.describe_restautant()
restaurant2 = Restaurant('汉堡王', '汉堡')
restaurant2.describe_restautant()

#9-3用户：创建一个名为User的类，其中包含属性first_nameh last_name,还有用户简介通常会使用到的其他几个属性
#。在类User中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法
#它向用户发出个性化的问候。创建多个表示不用用户的实例，并对每个实例都调用上述两个方法。


class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(
            f'用户姓名{self.first_name} {self.last_name},性别：{self.gender}，年龄：{self.age}'
        )

    def greet_user(self):
        print(f'你好，{self.first_name} {self.last_name}')


user = User('王', '华', '男', '18')
user.describe_user()
user.greet_user()


#9-4就餐人数：在9-1的基础上，添加一个名为number_served的属性，并将其默认值设置为0.根据这个类创建一个名为restaurant
#的实例；打印有多少人在这家餐馆就餐过， 然后修改这个值并再次讨论它。
#添加一个名为set_number_server()的方法，它让你能够设置就餐人数，调用这个方法并向它传递一个值，然后再次打印这个值
#添加一个名为 increment_number()的方法，它让你能够 将就餐人数递增，调用这个方法向它传递一个这样的值：你认为
#这家餐馆每天可以接待的就餐人数。
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restautant(self):
        print(
            f'这个餐厅的名字是{self.restaurant_name.title()},专门售卖{self.cuisine_type.title()}'
        )

    def open_resturant(self):
        print(f'{self.restaurant_name.title()}正在营业中')

    def guess_number_served(self):
        print(f'现在每天有{self.number_served}人在这家餐馆就餐。')

    def set_number_server(self, many_people):
        self.number_served = many_people

    def increment_number(self, increment):
        self.number_served += increment


restaurant = Restaurant('烧烤自助', '烤肉')
restaurant.guess_number_served()
restaurant.number_served = 23
restaurant.guess_number_served()
restaurant.set_number_server(16)
restaurant.guess_number_served()
restaurant.increment_number(10)
restaurant.guess_number_served()


#9-5尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。编写一个名为
#increment_login_attempts()的方法，它将属性login_attempts的值加1，再编写一个名为reset_login_attempts的方法
#它将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次，。打印属性login_attempts的值，确定它
#被正确地递增；然后，调用方法reset_login_attempts(),并再次打印属性login_attempts的值，确认它被重置为0.
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


user = User('王', '华', '男', '18')
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
