# coding:utf-8

# 생성자 사용 안할시
result = 0

def addr(num):
    global result
    result += num
    return result




# python 생성자 사
class Calculator:
    def __init__(self):
        self.result = 0

    def addr(self, num):
        self.result += num
        return self.result


calc1 = Calculator()
calc2 = Calculator()

print calc1.addr(5)
print calc1.addr(10)
print calc1.result
print calc2.addr(20)
print calc2.addr(50)
print calc2.result

print "==" * 50

class Programmer:
    pass


kim = Programmer()
lee = Programmer()
park = kim

print kim
print lee
print kim is lee
print park is kim



class Service:
     secret = "영구는 배꼽이 두 개다"
     def setname(self, name):
         self.name = name
     def sum(self, a, b):
         result = a + b
         print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))


pey = Service()

pey.setname("홍길동")

print pey.name

pey.name = "홍길동1"

print pey.name

print "==" * 50

class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)

# + 연산자를 객체에 사용하게 되면 HousePark 클래스의 __add__ 라는 함수가 자동으로 호출된다.
pey + juliet

# - 연산자는 __sub__라는 함수를 자동으로 호출
pey - juliet


