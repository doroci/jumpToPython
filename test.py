# coding:utf-8

for i in [1, 2, 3, 4]:
    if i == 1:
        print("i is 0")
    elif i == 2:
        print("i is 1")
    elif i == 3:
        print("i is 2")
    else:
        print("else")


print ("==" * 50)

# 문자열 concatenate
head = "hello"
tail = " world"
print(head + tail)

# *은 반복 횟수를 의미
print (head * 3)

# 파이썬은 0부터 인덱싱을 한다.
a = "Life is too short, You need Python"
print(a[0])

# 음수는 문자열 끝부터 인덱싱을 한다.
print(a[-2])

# 문자열 슬라이딩
print(a[0]+a[1]+a[2]+a[3])
print(a[0:4]) # 위와 같이 해도 되지만 이렇게 사용하는게 효과적
print(a[12:17])

# a[시작 번호:끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.
print("a[19:]: " +a[19:])
# 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
print("a[:19]: " +a[:19])
# 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.
print("a[:]: " +a[:])

b = 'pithon'
print (b[:1] +'y' +b[2:])

print("==" * 50)
# 숫자대입: %d, 문자대입: $s
print("I eat %d apples" % 3)
print("I eat 3 %s" % "apples")

print ("==" * 50)

# count(): 숫자세기
cnt = "count Down test"
print (cnt.count('o'))

# find(): 해당 위치 찾기: 0부터 카운트를 하며 존재하지 않는다면 -1을 반환한다.
print (cnt.find("D"))
print (cnt.index("D"))  # find와 달리 존재하지 않을 경우 에러를 반환한다.

# lstrip(): 왼쪽 공백 지우기, rstrip(): 오른쪽 공백 지우기, strip(): 양쪽 공백 지우기
trip = " hi "
# trip.lstrip() ..

# replace()
print (cnt.replace("count", "start"))

# split()
split = cnt.split()
print (split[0] +split[1] +split[2])

print ("==" * 50)

# 리스트: 문자열과, 숫자가 같이 배열안에 들어 갈 수 있다.
d = [1, 2, 'Life', 'is', ['1', '2', '3']]
print d[-1][1]
print d[1:3]

print ("==" * 50)

# 리스트 연산(+, *)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print list1 + list2
print list1 * 3 # n번 반복

# 정수 + 문자열 연산이므로 type 에러가 나기 때문에 같은 타입으로 변환해줘야함.
# print list1 + "hi"
print str(list1) + "hi"

print ("==" * 50)

# del: 리스트 요소 삭제
del list1[0]
print list1

# index(): 해당 값에 대한 인덱스를 알려준다.
print list2.index(6)

# insert(a, b): 리스트의 a번째 위치에 b를 삽입하는 함수이다.
list2.insert(0, '100')
print list2

# remove: 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
rm = [1, 2, 3, 1, 2, 3]
rm.remove(3)
print rm
print ("==" * 50)

# pop: 리스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수이다.
print rm.pop()
print rm

print ("==" * 50)

# count(x): 리스트 내에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수이다.
print rm.count(1)

# extend(x): x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
ex = [1,2,3]

# ex += 100,200 or ex = ex +[100,200] 3가지 같은 표현식
ex.extend([100,200])

print ex

# append(x): 마지막 엘리먼트에 x를 추가
t = [1, 3, 10, 4]
t.append(5)
print t

# sort(): 정렬
#t.sort(None, None, True)
t.sort()
print t

# reverse(): 역순으로 정렬해준다. 정렬은 하지 않음
t.reverse()
print t


print ("==" * 50)

# if
# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# if, elif, else


# while
cnt = 0
while cnt < 10:
    cnt += 1
    print "나무를 %d번 찍었습니다." % cnt
    if cnt == 10:
        print "나무 넘어갑니다"


# for
f = [(1, 2), (3, 4), (5, 6)]
for (first, last) in f:
    print first + last


# range(a, b): a이상 b미만 까지
ra = range(1, 11)
print ra


sum1 = 0
for i in range(1, 11):
    sum1 += i

print sum1


# len: 리스트 내 요소의 개수를 돌려주는 함수이다

print len(range(1, 11))

# 리스트 내포: [표현식 for 항목 in 반복가능객체 if 조건]
a = [1, 2, 3, 4]
result =[]
for num in a:
    result.append(num * 3)

print result

result = [num * 3 for num in a]
print result



