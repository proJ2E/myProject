def Get_Values():
    user_id = input("ID를 입력해주세요 : ")
    password = input("비밀번호를 입력해주세요 : ")
    day = input('검색할 날짜를 입력해주세요 (월단위는 month) \n'
                     'today or yyyy/mm/dd or month \n : ')
    if day == 'month':
        mon = input('검색할 달을 입력해주세요 ex) 3 \n : ')
    else:
        mon = "00"
    exposed_num = int(input('Best 글의 개수를 정해주세요 : '))

    user_input_data = {
        'user_id' : user_id,
        'password' : password,
        'day' : day,
        'mon' : mon,
        'exposed_num' : exposed_num
    }

    return user_input_data