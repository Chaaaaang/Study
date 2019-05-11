


# 문자열 출력하기

##### * 참고 : C1010 error : https://jepo.tistory.com/45 에서 해결
##### * markdown 사용법 : https://gist.github.com/ihoneymon/652be052a0727ad59601

* 프로그래밍(코딩) 과정 : 소스 코드 편집 -> 컴파일 -> 실행 과정 반복.
  -> C_stamp.c -> C_stamp.obj -> C_stamp.exe 로 생성됨.(c 소스코드가 exe로 생성되는 과정)

* #include : 헤더 파일을 포함하는 문법.
* printf 함수를 쓰려면 stdio.h 헤더 파일 필요함.
* main : c언어로 프로그램 만들 때 가장 처음에 실행되는 함수. -> main 없으면 커마일 안됨.
* 중괄호 : 코드의 범위를 나타내는데 구조체를 정의 할 때는 세미콜론(;)을 붙임.
* return 0 : 반환값을 함수 바깥으로 전달함.
* 코드가 1줄이어서 중괄호 생략해도 들여쓰기 해야 함.
  -> 들여쓰기 안해도 에러는 발생하지 않으나 코드 가독성이 좋음 : 공백 2칸, 4칸, Tab 등이 있음.

<pre><code>
ex)

#include <stdio.h>

int main()
{
	printf("%s\n", "Hello world!");
	printf("Hello world!\n");

	return 0;
}

</pre></code>

// 서식 지정자
#include <stdio.h>

int main() 
{
	// %s가 Hello world!로 바뀌는 것임.
	// 서식사용자는 내용 여러 개 출력, 출력 형태 바꿀 때 유용.
	printf("%s\n", "Hello, world!");
	printf("%s %s\n", "Hello,", "1234");

	// 공백도 출력에 영향 줌.
	printf("%s%s\n", "Hello,", " 1234");
	return 0;

}

// Q : main이 여러 개면?
// A : .c 파일 추가해서 main 여러 개 하면 오류 뜸 -> 1개만 있어야 함.
*/

/*


if (a>10)
	printf("a");

*/
