# 나머지 연산의 곱셈의 역원을 구하는 함수
# 시간복잡도 O(n)
def Inverse(n):
    x = -1
    for i in range(1, 26):
        if (n * i) % 26 == 1:
            x = i;
    if x == -1:
        print("행렬식이 역원을 가지지 못하는 좋지 않은 키입니다.")
        exit()
    return x

# 확장 유클리드 알고리즘
# 시간복잡도 O(log(max(A, B)))
def EEA(a):
    r1,r2 = a, 26
    s1,s2 = 1, 0
    
    while(r2>0):
        q = r1 // r2
        r = r1 - q * r2
        r1,r2 = r2,r
        s = s1 - q * s2
        s1,s2 = s2,s
        
    if r1 != 1:
        print("행렬식이 역원을 가지지 못하는 좋지 않은 키입니다.")
        exit()
    if s1 < 0:
        s1 = 26 + s1
    return s1

#평문
string = input("메시지를 입력하세요 : ")
string = string.replace(" ", "")

#Key1,2,3,4
k1 = int(input("첫 번째 키를 입력하세요 : "))
k2 = int(input("두 번째 키를 입력하세요 : "))
k3 = int(input("세 번째 키를 입력하세요 : "))
k4 = int(input("네 번째 키를 입력하세요 : "))

#알파벳 정수 치환 a = 1, b = 2...
P = []
for c in string.lower():
    P.append(ord(c) - ord('a') + 1)

if len(P) % 2 == 1:
    P.append(24)

# 암호화
C = []
for i in range(0, len(string), 2):
    C.append((k1 * P[i] + k2 * P[i+1]) % 26)
    C.append((k3 * P[i] + k4 * P[i+1]) % 26)

# 정수 알파펫 치환 1 = a, 2 = b...1
cryptTxt = []
for i in C:
    i = i if i > 0 else 26
    cryptTxt.append(chr(ord('a') - 1 + i))

# 역키 inverse key
# m1 = Inverse(k1*k4 - k2*k3) * k4
# m2 = Inverse(k1*k4 - k2*k3) * (-k2)
# m3 = Inverse(k1*k4 - k2*k3) * (-k3)
# m4 = Inverse(k1*k4 - k2*k3) * k1
m1 = EEA(k1*k4 - k2*k3) * k4
m2 = EEA(k1*k4 - k2*k3) * (-k2)
m3 = EEA(k1*k4 - k2*k3) * (-k3)
m4 = EEA(k1*k4 - k2*k3) * k1

# 복호화
plainTxt = []
for i in range(0, len(C), 2):
    plainTxt.append((m1 * C[i] + m2 * C[i+1]) % 26)
    plainTxt.append((m3 * C[i] + m4 * C[i+1]) % 26)

# 복호화된 정수 리스트를 문자 리스트로 변환
for idx, val in enumerate(plainTxt):
    val = val if val > 0 else 26
    plainTxt[idx] = chr(ord('a') - 1 + val)

# 출력
print("평문 : {}".format(string))
print("암호화 :", end=" ")
for i in cryptTxt:
    print(i, end="")
print("\n복호화 :", end=" ")
for i in plainTxt:
    print(i, end="")