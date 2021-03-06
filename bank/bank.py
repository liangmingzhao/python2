
# 银行操作
#   开户,查询,存款,取款,转账,改密,锁卡,解锁,补卡,销户

from cards import Card
from users import  User
import random
import pickle
import os

class Bank:
    def __init__(self):
        pass
        self.users = []  # 当前银行系统的所有用户
        self.file_path = 'users.txt'  # 本地文件路径

        # 启动银行系统后,立刻获取user.txt文件中之前保存的所有用户
        self.__get_users()
        print('=> 原来的所有用户:', self.users)

    # 保存用户对象到文件中
    def __save_users(self):
        # 写入文件
        fp = open(self.file_path, 'wb')
        pickle.dump(self.users, fp)
        fp.close()
        print('=> 当前所有用户:', self.users)

    # 每次运行项目后都要重新获取user.txt文件中的所有用户
    def __get_users(self):
        # 读取文件
        if os.path.exists(self.file_path):
            fp = open(self.file_path, 'rb')
            self.users = pickle.load(fp)
            fp.close()

# ----------------------- 华丽的风景线 --------------------------#
    # 开户
    def create_user(self):
        pass
        # 1.创建卡
        #  卡号
        cardid = self.__create_cardid()
        print('=> 成功创建卡号:', cardid)
        # 卡密码
        passwd = self.__set_password()
        if not passwd:
            return
        # 卡余额
        money = float(input('请您输入要预存的金额:'))
        # 创建卡对象
        card = Card(cardid, passwd, money)
        print('=> 创建卡成功:', card)

        # 2.创建用户
        name = input('请输入您的真实姓名:')
        idcard = input('请输入您的身份证号码:')
        phone = input('请输入您的手机号码:')
        # 创建用户
        user = User(name, phone, idcard, card)
        print('=> 创建用户成功: ', user)

        # 3.将新用户存储
        # 将新用户加入到银行系统中
        self.users.append(user)
        # 存储
        self.__save_users()

    # 创建随机,唯一卡号
    def __create_cardid(self):
        while True:
            # 生成随机卡号
            cardid = '8888'
            for i in range(4):
                cardid += str(random.randint(0, 9))

            # 如果有一个用户的卡号和cardid相同,则break继续执行while,否则返回cardid
            for user in self.users:
                if user.card.cardid == cardid:
                    break
            else:
                return cardid

    # 设置密码
    def __set_password(self):
        # 允许输错3次
        for i in range(3):
            passwd = input('请您输入密码:')
            passwd2 = input('请再输入一次:')
            # 验证2次密码是否一致
            if passwd == passwd2:
                return passwd
            print('=> 2次密码不一致,请重新输入...')
        else:
            print('=> 您输入了3次错误密码.')
            return False

# ----------------  华丽的风景线  -------------------------------------#
    # 查询
    def search_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码: 考虑允许输错3次,否则锁卡
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('=> 密码错误!')
            return

        # 3.显示余额
        print('当前余额:', user.card.money)

    # 输入卡号
    def __input_cardid(self):
        cardid = input('请输入要查询的银行卡号:')
        # 如果卡号存在 则返回所在的用户对象,否则默认返回None
        for user in self.users:
            if user.card.cardid == cardid:
                return user

    # 存款
    def save_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('=> 密码错误!')
            return
        # 3.输入存款金额,并将user.card.money+=100
        money = float(input('请您输入要存入的金额:'))
        user.card.money += money

        # 4.self.__save_users()
        self.__save_users()

    # 取款
    def get_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('=> 密码错误!')
            return
        # 3.输入取款金额,并将user.card.money-=100
        while True:
            money = float(input('请您输入要取出的金额:'))
            if user.card.money < money:
                print('=> 余额不足!')
                continue
            user.card.money -= money
            break

        # 4.self.__save_users()

    # 转账
    def transform_money(self):
        pass
        # 1.输入转出的卡号
        # 2.输入转出的卡密码
        # 3.输入对方的卡号
        # 4.输入转账金额,并
        #   将自己user.card.money -= 100
        #   将对方user.card.money += 100
        # 5.self.__save_users()

    # 改密
    def modify_password(self):
        pass
        # 1.输入卡号
        # 2.输入身份证
        # 3.输入旧密码,再输入新密码
        # 4.self.__save_users()

    # 锁卡
    def lock_card(self):
        pass
        # 1.输入卡号
        # 2.输入密码
        # 3.锁卡 user.card.islock = True
        # 4.self.__save_users()

    # 解锁
    def unlock_card(self):
        pass
        # 1.输入卡号
        # 2.输入密码
        # 3.解锁 user.card.islock = False
        # 4.self.__save_users()

    # 补卡
    def makeup_card(self):
        pass
        # 1.输入身份证
        # 2.创建新卡,并替换旧卡: user.card = card
        # 3.self.__save_users()
    # 销户
    def delete_user(self):
        pass
        # 1.输入身份证
        # 2.删除用户
        # 3.self.__save_users()











