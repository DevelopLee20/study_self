import hashlib
import sqlite3

while True:
    menu = int(input("메뉴를 선택하세요. 1. 로그인 / 2. 회원가입 / 3. 비밀번호 찾기 "))

    if(menu == 1):

        #아이디 비밀번호 입력부
        userID = input("아이디를 입력하세요 : ").strip()
        userPW = input("비밀번호를 입력하세요 : ").strip()
        userPW = hashlib.sha256(userPW.encode()).hexdigest()

        con = sqlite3.connect("daily.db")
        cursor = con.cursor()

        cursor.execute("select count(*) from user where id = ? and password = ?",(userID,userPW)) #입력한 아이디 비밀번호가 있나 확인
        result = cursor.fetchone()[0]
        if(result == 0): #id 와 비밀번호가 일치하면 1이나오고 아니면 0이 나옴
            print("로그인에 실패했습니다.")
        else:
            print("로그인에 성공했습니다.")

        con.close()

    elif(menu == 2):

        userID = input("아이디를 입력하세요 : ").strip()
        userPW = input("비밀번호를 입력하세요 : ").strip()
        userPW2 = input("비밀번호를 다시 입력하세요 : ").strip()
        userName = input("이름을 입력하세요 : ").strip()
        userPhone = input("전화번호를 입력하세요 : ").strip()

        if(userPW != userPW2):
            print("입력한 비밀번호 두개가 일치하지 않습니다.")
            continue


        con = sqlite3.connect("daily.db")
        cursor = con.cursor()

        cursor.execute("select count(*) from user where id = ?",(userID,)) #이미 id 로 회원가입되었나 검사
        result = cursor.fetchone()[0]
        if (result):#id 에 id 가 1개 이상인경우
            print("이미 가입된 아이디입니다!")
            con.close()
            continue

        userPW = hashlib.sha256(userPW.encode()).hexdigest() #비밀번호 암호화해서 저장
        userPhone = hashlib.sha256(userPhone.encode()).hexdigest() #전화번호 암호화해서 저장
        cursor.execute("insert into user values(?,?,?,?)",(userID,userPW,userName,userPhone))
        con.commit()
        con.close()


    elif (menu == 3):
        userID = input("아이디를 입력하세요 : ").strip()
        userName = input("가입한 이름을 입력하세요 : ").strip()
        userPhone = input("가입한 전화번호를 입력하세요 : ").strip()
        userPhone = hashlib.sha256(userPhone.encode()).hexdigest() #전화번호 암호화해서 조회

        con = sqlite3.connect("daily.db")
        cursor = con.cursor()

        cursor.execute("select count(*) from user where id = ? and name = ? and phone = ?",(userID,userName,userPhone)) #입력한 정보로 아이디가 있나 확인
        result = cursor.fetchone()[0]
        if(result == 0): #db 에 회원 정보가 없으면 비밀번호 찾기 실패
            print("가입 정보가 없습니다.")
            con.close()
            continue

        userPW = input("재설정할 비밀번호를 입력하세요 : ").strip()
        userPW2 = input("재설정할 비밀번호를 다시 입력하세요 : ").strip()
        userPW = hashlib.sha256(userPW.encode()).hexdigest()
        cursor.execute("update user set password = ? where id = ?",(userPW,userID))

        print("비밀번호가 정상적으로 변경됬습니다.")
        con.commit()
        con.close()
