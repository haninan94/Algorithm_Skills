"""
파이썬은 기본으로 10진수를 사용하기 때문에, 다른 진수의 형태를 표현하려면 접두어가 필요하다.
2진수는'0b' 접두어가 붙으며,
8진수는'0o',
16진수는 '0x'를 붙여준다.
"""
print(5 == 0b101) # True

print(65 == 0o101) # True

print(257 == 0x101) # True

# 10진수를 다른 진수로 변환하기
print(bin(5)) # 0b101

print(oct(65)) # 0o101

print(hex(257)) # 0x101

# 10진수 외 다른 진수들을 10진수로 변환하기
# int는 2번째 인자로 들어갈 진수의 값이 10으로 정해져있다. 따라서 우리가 흔히 쓰는 int 는 10진수로 표현한다.
print(int('0b101', 2)) # 5

print(int('0o101', 8)) # 65

print(int('0x101', 16)) # 257

# format 함수를 사용해서 접두어를 제거할 수 있다.
print(format(5, 'b')) # 101

print(format(65, 'o')) # 101

print(format(257, '0x')) # 257

# format 함수를 사용해서 접두어를 포함시킬 수도 있다.
print(format(5, '#b')) # 0b101

print(format(65, '#o')) # 0o101

print(format(257, '#0x')) # 0x257


