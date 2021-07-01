# 태그 모음

## HTML 기본틀 간단하게 만들기

```html
!
```

> 위의 코드를 작성하고 Enter를 입력하면 Visual Studio Code 상에서는 쉽게 기본틀을 작성할 수 있다.

---

## 제목 텍스트 입력하기

```html
<h1>제목</h1>
<h2>제목</h2>
<h3>제목</h3>
```

> 'h + 숫자' 로 구현하면 제목 텍스트를 입력할 수 있다.

---

## 내용 텍스트 입력하기

```html
<p>내용</p>
```

---

## Enter 입력하기

```html
<br>
```

---

## 인용문 (한칸 들여쓰기) 입력하기

```html
<blockquote>인용문 작성</blockquote>
```

> 인용문을 위한 텍스트 입력 방법이지만, 들여쓰기가 한칸 되어있어 일반적으로 깨끗하게 작성하기 위해 사용해도 된다. 단 화면 내용을 읽어주는 **화면 낭독기**에 의해 읽힐때는 깔끔하지 않을 것 같다.

---

## 텍스트를 굵게 표시하기

```html
<strong>굵게 강조할 텍스트</strong>
<b>굵게 표시할 텍스트</b>
```

> **화면 낭독기** 상에서 강조하기 위해서는 strong 태그를 사용하지만 그냥 글에서만 강조하기 위해서는 b 태그를 사용한다.

---

## 기울인 텍스트 입력방법

```html
<em>기울일 텍스트</em>
<i>기울일 텍스트</i>
```

> em 태그는 강조를 위해 사용합니다.
>
> 반면에 i 태그는 다른 텍스트와 구별하기 위해서 사용합니다.

---

## 다양한 텍스트 관련 태그

```html
<abbr title="풀네임">줄일 텍스트</addr>
<cite>웹 문서 참고 텍스트</cite>
<code>컴퓨터 인식을 위한 소스 코드</code>
<small>작게 표시해도 되는 텍스트(예시: 부가정보)</small>
<sub>아래 첨자</sub>
<sup>위 첨자</sup>
<s>취소선(중간에 줄이 그어진 텍스트)</s>
<u>밑줄 표시</u>
<ins>새로운 내용 삽입</ins>
<del>기존 내용 삭제(중간에 줄이 그어진 텍스트)</del>
```

---

## 번호가 붙어있는 순서 목록 태그

```html
<ol>
    <li>항목1</li>
    <li>항목2</li>
    <li>항목3</li>
</ol>
```

```html
1. 항목1
2. 항목2
3. 항목3
```

### type과 start 속성

```html
<ol type="a" start="3">
    <li>항목1</li>
    <li>항목2</li>
    <li>항목3</li>
</ol>
```

```html
c. 항목1
d. 항목2
e. 항목3
```

> type 속성의 종류에는 "1", "a", "A", "i", "I" 가 있다.
>
> start 속성에는 시작할 번째의 정수를 넣는다.

---