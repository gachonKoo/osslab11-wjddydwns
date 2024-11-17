import geo.utils as utils

# calculate the length of hypotenuse(c) when a=3 and b=4
a, b = 3, 4
c = utils.pythagoras(a, b)  # 두 점 사이의 거리 계산을 위한 함수 호출
print('c =', c)

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle(r)  # 원의 면적을 계산하기 위한 함수 호출
print('area =', area)
