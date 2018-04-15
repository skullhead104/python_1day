class Address:
    def __init__(self, name, phone_number, e_mail, addr):

        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("="*20)
        print("이름: ", self.name)
        print("연락처: ", self.phone_number)
        print("이메일: ", self.e_mail)
        print("주소: ", self.addr)
        print("=" * 20)

def setAddress():
    name = input("이름 : ")
    phone_number = input("연락처 : ")
    e_mail = input("이메일 : ")
    addr = input("주소 : ")
    data = Address(name, phone_number, e_mail, addr)
    return data

def print_menu():
    print("1. 연락처 등록")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택 ==> ")
    return int(menu)


def run():
    menu = print_menu()
    if menu == 1: setAddress()
    elif menu == 2:
        = setAddress()
    data.print_info()

if __name__=="__main__":
    run()



