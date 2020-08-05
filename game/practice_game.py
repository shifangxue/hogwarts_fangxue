"""
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
import random,time

def skill(c_p, k_p):
    if c_p > k_p:
        print("\t\t\t空中百裂脚 <====> 疾风迅雷腿")
    else:
        print()

def fight():
    # 初使化双方血量
    ken_hp = 1000
    chunli_hp = 1000

    while True:
        #双方随机生成功击力
        ken_power = random.randint(40, 90)
        chunli_power = random.randint(40, 90)
        #计算双方功击后剩余血量
        ken_hp=ken_hp-chunli_power
        chunli_hp=chunli_hp-ken_power
        #模仿延迟
        time.sleep(0.5)
        #打印双方血量信息及比赛结果
        print("ken_hp:",ken_hp,"(-",chunli_power,")\t\tchunli_hp:",chunli_hp,"(-",ken_power,")")
        skill(k_p=ken_power,c_p=chunli_power)
        if ken_hp<=0:
            print("----------------------------")
            print("春丽胜利了")
            break
        elif chunli_hp<=0:
            print("----------------------------")
            print("肯.马斯达斯胜利了")
            break
        elif ken_hp==chunli_hp:
            print("----------------------------")
            print("同归于尽")
    print("============over==============")

fight()
