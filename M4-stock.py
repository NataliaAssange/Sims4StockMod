def price():
    import random
    from typing import Any
    global BANA
    global QOOQ
    global HB
    BANA=random.randint(1,300)
    QOOQ=random.randint(1,300)
    HB=random.randint(1,300)
    print ('欢迎光临模拟证券交易所' \
        '\n今天的证券行情是:'\
            '\nBANA Banana Inc. ', BANA, \
            '\nQOOQ Qooqle Inc.', QOOQ, \
            '\nHB Handbook Inc.',HB,\
        '\n投资有风险，入市须谨慎！')
    return BANA,QOOQ,HB
money=100000
qty0=0
hold0=0
#买
def buy():
    try:
        qty=int(input('你想购买多少股BANA？'))
    except:
        print('对不起，输入无效，请输入一个正整数')
    else:
        global money
        global qty0
        global hold0
        if qty>0:
            hold=qty*BANA
            if money>hold:
                money=money-hold
                qty0=qty+qty0
                hold0=hold+hold0
                print('您已成功购买', qty, '股，共计', hold, '元，您的家庭资金现有', money, '元，欢迎下次光临')
            else: 
                maxq=money//BANA
                print('购买失败，您的家庭资金不足，最多可以购买', maxq,'股，请重新下单')
        else:
            print('对不起，输入无效，请输入一个正整数')
    return money,qty0,hold0
#查看持仓
def view():
    value=qty0*BANA
    profit=abs(value-hold0)
    if value>hold0:
        print('您共持有BANA',qty0,'股，市值',value,'元','预计收益',profit,'元')
    else:
        print('您共持有BANA',qty0,'股，市值',value,'元','预计亏损',profit,'元')
    return qty0
#卖
def sell():
    try:
        qty=int(input('你想出售多少股BANA？'))
    except:
        print('对不起，输入无效，请输入一个正整数')
    else:
        global money
        global qty0
        global hold0
        if qty>0:
            if qty0-qty<0:
                print('交易失败，您的持仓不足，最多可以购买', qty0,'股，请重新下单')
            else:
                hold=BANA*qty
                money=money-hold
                qty0=qty0-qty
                print('您已成功售出', qty, '股，共计', hold, '元，您的家庭资金现有', money, '元，欢迎下次光临')
        else:
            print('对不起，输入无效，请输入一个正整数')
    return money, qty0
#以下为调试
price()
buy()
price()
buy()
view()
price()
sell()
price()
view()
price()
sell()
price()
view()