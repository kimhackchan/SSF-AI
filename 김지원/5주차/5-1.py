A = int(input("첫번째 학생의 성능을 입력하세요.(단, 성능은 항상 5의 배수이다.):"))
if A>100 or A<0:
    print("다시 입력해주세요")
B = int(input("두번째 학생의 성능을 입력하세요.(단, 성능은 항상 5의 배수이다.):"))
if B>100 or B<0:
    print("다시 입력해주세요")
C = int(input("세번째 학생의 성능을 입력하세요.(단, 성능은 항상 5의 배수이다.):"))
if C>100 or C<0:
    print("다시 입력해주세요")
D = int(input("네번째 학생의 성능을 입력하세요.(단, 성능은 항상 5의 배수이다.):"))
if D>100 or D<0:
    print("다시 입력해주세요")
E = int(input("다섯번째 학생의 성능을 입력하세요.(단, 성능은 항상 5의 배수이다.):"))
if E>100 or E<0:
    print("다시 입력해주세요")

if 0<A<50:
    A = 50
if 0<B<50:
    B = 50
if 0<C<50:
    C = 50
if 0<D<50:
    D = 50
if 0<E<50:
    E = 50

print(int((A+B+C+D+E)/5))
