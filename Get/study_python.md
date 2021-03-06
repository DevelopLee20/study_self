# Python 언어 노트

## 알게된 개념

> set -> 리스트의 중복을 제외하는 집합 함수
>
> |_> set 변환시 연산자 사용 가능
>
> sep = ' ' 리스트 요소 각각 사이에 추가할 요소 입력
>
> end = ' ' 리스트 끝에 추가할 요소
>
> *p -> 리스트 p의 옆 가로를 제거해줌
>
> 재귀함수 -> 재귀함수 리턴시 스텍 개념
>
> softed -> 정렬 함수
>
> find 함수는 묹열에 그 문자가 있을 때 인덱스를 리턴, 아닐때 -1을 리턴, 2개의 요소가 있을 때 앞 부터 판단한다, 문자열 전용 메소드이다.

---

## 리스트 대입 개념

```python
a = [1,2,3]
b = a
a = a + [4,5]
c = a
b += [6,7]
print(k) // [1,2,3,6,7]
print(a) // [1,2,3,4,5]
```

---

## List Comprehension - 리스트 캄프리헨션

```python
t = [x for x in input().split() if int(x)%2 == 0]
```

> 리스트에 들어갈 수의 조건을 리스트의 선언과 동시에 작성해서 조건에 맞는 즉시 대입되도록 한다

---

## for 문의 다양한 사용법

```python
print(sum[int(x) for x in input()])
print(len(a)-sum(a.count(i) for i in [1,2,3,4]))
```

---

## list 의 다양한 사용법

```python
a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7]

print(max(int(a[::-1]),int(b[::-1])))
```

> list.name[::-1] -> 역순으로 돌리기
>
> max(list.name) -> 리스트 내에서 가장 큰 요소 출력
