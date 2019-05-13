# 변수 만들기

* 예 : int num1;	

  -> 정수 표현. 이를 '변수 선언'이라고 함.
  
* 변수 이름 규칙
  * 영문 문자와 숫자 사용 가능
  * 대소문자 구분함
  * 문자부터 시작해야 함(숫자부터 시작하면 안됨)
  * _(밑줄 문자)로 시작 가능.
  * C 언어의 키워드(예약문자 : int, short 등)는 사용 할 수 없음.

<br /><br />
### 예제1) 자료형 정수 이름 선언 및 할당


<hr/>

#include <stdio.h>
<pre><code>
int main() {
	int num1;		// 정수형 변수 선언
	int num2;
	int num3;

	num1 = 10;		// 변수에 값 할당(저장)
	num2 = 20;
	num3 = 30;

	printf("%d %d %d\n", num1, num2, num3);		// 10 20 30: 변수에 저장된 값을 %d로 출력

	return 0;
	
}
</pre></code>


<br /><br />
### 예제2) 여러 변수 선언하기

<hr/>

#include <stdio.h>
<pre><code>

int main() {
	int num1, num2, num3;		// 정수형 변수 선언

	num1 = 10;		// 변수에 값 할당(저장)
	num2 = 20;
	num3 = 30;

	printf("%d %d %d\n", num1, num2, num3);		// 10 20 30: 변수에 저장된 값을 %d로 출력

	return 0;

}
</pre></code>


<br /><br />
### 예제3) 변수 선언과 할당을 동시에 하기

<hr/>
#include <stdio.h>
<pre><code>


int main() {
	int num1 = 10;
	int num2 = 20, num3 = 30;		// 정수형 변수 선언
		printf("%d %d %d\n", num1, num2, num3);		// 10 20 30: 변수에 저장된 값을 %d로 출력

	return 0;

}
</pre></code>


