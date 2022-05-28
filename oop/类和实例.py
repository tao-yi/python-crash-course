'''
在Python中,所有的数据类型都可以视为对象。
'''

# Student(People) 括号中的People是要继承的父类
# 如果不写，那么父类就是object类
class Student():
  # __init__方法的第一个参数永远是self
  # self指向创建的实例本身，调用时不用传
  # python解释器会自动把self变量传进这个参数s
  def __init__(self, name:str, score:int):
    self.name = name
    self.score = score
    
  def print_score(self):
    print(f'{self.name}: {self.score}')
  
  # 类中定义的函数第一个参数必须是self
  def test(self):
    print('test')

# s1指向的是一个Student对象的地址
s1 = Student('Bart Simpson', 59)
print(s1)
s2 = Student('Lisa Simpson', 87)
s1.print_score()
s2.print_score()
s1.test()

# Python允许对实例变量绑定任何数据，可以自由地给一个实例变量绑定属性
# 由于类可以起到模板的作用，因此可以在创建实例的时候
# 把一些我们认为必须绑定的属性强制填写进去，通过__init__方法
s1.age = 15
