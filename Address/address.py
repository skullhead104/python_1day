class Address:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("이름: ", self.name)
        print("연락처: ", self.phone_number)
        print("이메일: ", self.e_mail)
        print("주소: ", self.addr)

def run():
    data = Address('홍길동','010-****-****', 'hong@naver.com', '세종')
    data.print_info()

if __name__=="__main__":
    run()



