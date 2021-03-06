# 시퀀스

## 내장 시퀀스 개요
* 리스트, 튜플, 배열, 큐 등 데이터를 나열한 것을 말함. 즉, 여러 데이터를 담을 수 있는 형태를 말함

* 시퀀스를 나눠보면
  * 컨테이너 시퀀스 vs 균일 시퀀스

    * 컨테이너 시퀀스 

      * 서로 다른 자료형을 담을 수 있음 (list, tuple 등)
      * 객체에 대한 참조를 담고 있음.

    * 균일 시퀀스 

      * 단 한 개의 자료형만 담을 수 있음
      * 객체에 대한 참조 대신 자신의 메모리 공간에 각 항목의 값을 직접 담음(메모리 사용 적음)

  * 가변성에 따른 분류

    * 가변 시퀀스 : list, bytearray 형 등
    * 불변 시퀀스 : tuple, str, bytes 형

## 지능형 리스트 (Chapter 2_1)
* 지능형 리스트는 리스트 안에서 for문을 이용하여 리스트를 만듦.  
  -> ex) [ord(symbol) for symbol in symbols]
* 지능형 리스트를 사용하지 않아도 되는 경우
  * 생성된 리스트 미사용시
  * 리스트 구문이 두 줄 이상 넘어가는 경우 : 코드 분할 또는 다른 방법.
* 지능형 리스트의 경우 거기서 쓴 변수가 바깥의 변수에 영향을 주지 않음  
  -> ex) [ord(x) for x in x]를 했을 때 바깥에서 미리 정의된 x값을 바꾸지 않음.
* 지능형 리스트는 map()/filter() 조합보다 더 빠를 수 있음.
* 지능형 리스트에서 for문을 2개 사용하는 경우 앞의 것을 기준으로 리스트를 만듬.
* 리스트가 아닌 다른 종류의 시퀀스를 채우려면 제너레이터 표현식 사용해야 함.

## 제너레이터 표현식 (Chapter 2_1)
* 지능형 리스트에 비해 더 적은 메모리 사용. 이는 다른 생성자에 전달할 리스트를 통째로 만들지 않고 반복자 프로토콜을 이용하기 때문(1개씩 만듦)
* 괄호로 만듦  
  -> ex) tuple(ord(symbol) for symbol in symbols)

## 튜플 : 단순한 불변 리스트가 아님 (Chapter 2_1)
* 레코드로 이용  
  -> ex) city, year, pop = ('Tokyo', 2003, 32450)
* 튜플 언패킹
  * 위의 ex에서 city, year 등의 변수에 값을 할당한 것이 튜플 언패킹임.  
  -> ex) lax_coor = (33, -118)
        lat, long = lax
  * 초과항목의 경우 *을 사용하여 이용 가능  
  -> ex) a,b, *rest = range(5)
 
  * namedtuple() : 튜플의 필드에 이름을 붙일 수 있음 (tuple과 같은 메모리를 사용하며 dict 등의 객체보다 메모리 적게 씀)  
  -> ex) City = namedtuple('City', 'name country population coordinates')  
        # City가 큰 객체. name, country, population, coordinates는 필드명  
        tokyo = City('Tokyo', 'JP', 36.933, (35, 139))  
        tokyo.population  
        tokyo[1]  
        
## 슬라이싱 (Chapter 2_1)
* [1:5:3] : 1~5번째 값까지, 3 단위씩 건너뛴 값.
* 슬라이스에 할당 가능  
 -> ex) l = list(range(10))
        l[2:5] = [20,30]  

## 시퀀스에 덧셈, 곱셈 연산자 (Chapter 2_1)
* 리스트의 리스트 만들기
  * 값을 가진 리스트를 초기화 할 때 사용  
 -> ex) 올바른 예  
 board = [['_'] * 3 for i in range(3)]  
 -> ex) 잘못된 예  
 weird_bopard = [['_'] *3] * 3      # 같은 곳을 참조하는 리스트 3개를 만들게 됨 -> 1개 값 바꾸면 3개의 리스트의 위치값이 똑같이 바뀜
 
## 시퀀스의 복합 할당 (Chapter 2_1)
* *= 연산자의 경우 불변 시퀀스에 하는 것은 비효율적임. 이는 새 항목 추가 대신 항목 추가된 시퀀스 전체를 새로 만들기 때문.

## sort vs sorted (Chapter 2_1)
* sort는 바로 적용되므로 새 객체를 생성하지 않음. 결과값은 None 반환(객체 생성 안했으므로), sorted는 새로운 리스트를 생성해서 반환함.

## 리스트가 아닌 시퀀스들
* 배열 : 리스트 안에 숫자만 들어있다면 배열을 쓰는 것이 효율적임  
 -> ex) from array import array  
        floats = array('d', (random() for i in range(10**7)))     # 'd' : 배밀도 실수 생성
* 덱 : queue의 양쪽 어디에서든 빠르게 삽입 및 삭제 가능(양방향 큐)  
 -> ex) from collections import deque  
        dq = deque(range(10), maxlen=10)     # 10으로 최대용량 제한하여 이보다 많이 들어오면 다른 데이터가 삭제됨
  * 그 외의 큐
    * queue : 덱과 달리 공간이 꽉 차도 항목을 버리지 않고 새로운 변수를 블로킹 함.
    * multiprocessing : queue와 비슷하나 프로세스 간 통신을 지원하기 위해 설계된 고유한 Queue 클래스 구현.
