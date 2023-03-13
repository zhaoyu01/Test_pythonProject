import random
import time
com = ['中汇','中祥','华都','佳业','凯信','诚盛','恒通','汇利',

'国通','华新','华都','新通','国豪','建辉','睿渊','韵文',

'得月','陶然','吉安','永逸','宇硕,''智宇','腾辉','启讯',

'远东','沃玛','海程','海迪','腾达','腾飞','致远','顺昌',

'盛昌','森悦','利丰','天邦','东升','东圣','天欣','天成',

'开元','祥元','千橡','汇业','汇金','天禄','百利','百盈',

'福川','畅旺','汇优','汇品','博汇','博纳','中达','中盛',

'华强','浩远','中天','广宇','华能','华鲁','科陆','华峰',

'中联','九阳','亚泰','宏润','亨通','御银','烽火','恒瑞']

def name():
    names = ['测试人员李白','测试人员杜甫','测试人员陶渊明','测试人员杜甫','测试人员李清照','测试人员王勃','测试人员陆游','测试人员孟浩然','测试人员张飞','测试人员刘备','测试人员赵云','测试人员马超','测试人员关羽',]
    name_test = random.choices(names)
    for name_l in name_test:
        print(name_l)
    return name_l

def get_birthday():
    start_birthday = (1970, 10, 10, 1, 10, 10, 10, 10, 10)  # 设置开始时间元组
    end_birthday = (2020, 5, 5, 10, 10, 10, 10, 10, 10)  # 设置结束时间元组
    start = time.mktime(start_birthday)  # 生成开始时间戳
    end = time.mktime(end_birthday)  # 生成结束时间戳
    for i in range(1):
        s = random.randint(start, end)  # 选择一个开始时间和结束时间
        date_touole = time.localtime(s)  # 将时间生成元组
        date = time.strftime("%Y-%m-%d", date_touole)  # 时间元组转换成格式化字符串
        print(date)
    return date


def gender():
    genders = ['MEN','WOMEN']
    gender_test = random.choices(genders)
    for gender_l in gender_test:
        print(gender_l)
    return gender_l


def type_add():
    type_add = ['STUDENT', 'HR', 'HEADHUNTING', 'WORKPLACE']
    type_test = random.choices(type_add)
    for type_add in type_test:
        print(type_add)
    return type_add

def pic():
    pics = ['http://192.168.101.102/file/2023/2/15/16764494075544.jpg','http://192.168.101.102/file/2023/2/15/16764496104075.png']
    pic_test = random.choices(pics)
    for pic_l in pic_test:
        print(pic_l)
    return pic_l

def cmpy():
    cmpys = com
    name_test = random.choices(cmpys)
    for cmpys in name_test:
        print(cmpys)
    return cmpy





if __name__ == '__main__':
    # gender()
    # name()
    # get_birthday()
    # type_add()
    # pic()

    cmpy()