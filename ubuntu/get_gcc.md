# 우분투 gcc 설치 과정

gcc 컴파일러 install

```txt
sudo apt-get install gcc
```

~~vim 인데 왠지 모르겠지만 vi 명령어 작동~~, test.c 파일이 있으면 편집모드 없으면 생성후 편집모드

```txt
vi test.c
```

디렉토리 내용 확인

```txt
ls
```

test 이름으로 test.c 파일을 컴파일

```txt
gcc -o test test.c
```

test.exe 실행

```txt
./test
```

test.c 파일 내용 확인

```txt
cat test.c
```

test.c를 test파일명으로 어셈블리어 프로그램 생성(열어보면 어셈블리어 코드 있음)

```txt
gcc -s -o test.o test.c
```

.o 오브젝트 파일만 생성

```txt
gcc -c
```

역 어셈블: 목적파일 test.o를 역 어셈블하여 내용 확인

```txt
objdump -d test.o
```

옵션 설명: 생성될 파일의 이름 설정

```txt
-o 파일명
```

중간 과정 모두 파일로 저장

```txt
gcc --save-temps test.c -o test
```
