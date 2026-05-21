#클래스 변수와 메소드 -- 객체를 생성하지 않아도 사용이 가능한 멤버 [클래스명.멤버명]

#클래스를 설계할때 미리 만들어놓은 변수로서 객체로 만들지 않아도 클래스에 1개씩 존재하는 변수
#보통, 값은 클래스의 객체들이 같은 값을 공유하는 목적으로 사용하는 변수를 클래스변수로 만들어 사용함

#'신림 고등학교' 학생들의 명단 관리 솔루션...서비스 개발
#학생마다 다른정보[이름,학년]를 저장하는 Student 클래스를 선언 후 객체 생성
#학생들의 학교명을 저장할건데...모두 같은 학교의 학생들임... 그렇다면 굳이 객체마다 그 값을 
#모든 학생객체들이 '신림고등학교' 하나의 변수값을 공유하는것이 더 효율적, '클래수변수로 만들수 있음.0
class Student:
    school_name='신림고등학교' 
    def __init__(self, name, grade):
        self.name= name
        self.grade= grade
        print()
#------------------------------------------

s1=Student('지만','1학년')
s2=Student('윤호','2학년')

#각 객체마다 가지고 있는 값을 출력.
print(s1.school_name+'-'+s1.grade + ':' +s1.name)
print(s2.school_name+'-'+s2.grade + ':' +s2.name)

#school_name 이라는 클래스변수는 객체마다 존재하는 변수가 아님..
#그렇기에 위처럼 s1.xxx, s2.xxx 라는 형태처럼 객체명으로 접근하는 것이 어색함..
#그래서 클래스변수의 사용은 가급적[클래스명.멤버명]으로 사용하는 것을 권장함!!

#각 객체마다 가지고 있는 값을 출력.
print(Student.school_name+'-'+s1.grade + ':' +s1.name)
print(Student.school_name+'-'+s2.grade + ':' +s2.name)
print()

#클래스변수도 값 변경 가능
Student.school_name='송파고등학교'
print(Student.school_name+'-'+s1.grade + ':' +s1.name)
print(Student.school_name+'-'+s2.grade + ':' +s2.name)
print()

#클래스 변수가 있으니..클래스 메소드도 존재함.[클래스명.메소드명()]
#그렇기에 객체생성이 없어도 호출 가능함...

class MyClass:
    #일반메소드
    def show(self):
        print('This is show method............')
    
    #클래스 메소드(객체를 생성하지 않아도 호출할 수 있는 함수)
    #이 메소드가 클래스 메소드라는 것을.. 파이썬에게 알려줘야 함. 즉, 표시를 해야 함
    #이 때 사용하는 문법이 ['데코레이터' @]라고 부름
    #이 데코레이터는 쉽게 이해하면 파이썬이 읽는 주석이라고 보면 됨.
    @classmethod
    def  output(self):
         print('This is output class method!!!!!!!!!!!!!!!!!!!!!!!!!!')

#일반메소드는 객체를 생성하지 않으면 호출이 불가능...
MyClass().show() #객체생성 후 메소드 호출
#show() #error
#MyClass.show() #error

#객체 생성없이 클래스 메소드를 호출해보기
MyClass.output()

