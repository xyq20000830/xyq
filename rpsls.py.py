#coding=utf-8
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：谢雨秋
日期：2019.11.15
"""
import random


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name == '石头':
        return 0
    elif name == '史波克':
        return 1
    elif name == '纸':
        return 2
    elif name == '蜥蜴':
        return 3
    elif name == '剪刀':
        return 4


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number == 0:
        return '石头'
    elif number == 1:
        return '史波克'
    elif number == 2:
        return '纸'
    elif number == 3:
        return '蜥蜴'
    elif number == 4:
        return '剪刀'


def rpsls():
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    print("欢迎使用RPSLS游戏")
    print("----------------")
    while True:
        print("请输入您的选择:")
        player_choice = input()
        if player_choice not in ['石头', '史波克', '纸', '蜥蜴', '剪刀']:
            print('Error:No Correct Name!')
            continue
        print('您的选择为：' + player_choice)

        # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
        player_choice_number = name_to_number(player_choice)

        # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
        comp_number = random.randrange(0, 4)

        # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象，存入变量computer_choice
        computer_choice = number_to_name(comp_number)

        # 在屏幕上显示计算机选择的随机对象
        print('计算机的选择为：' + computer_choice)

        # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
        #  如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
        if player_choice_number == comp_number:
            print('您和计算机出的一样呢！')
        elif player_choice_number == 0 and comp_number == (3 or 4):
            print('您赢了！')
        elif player_choice_number == 1 and comp_number == (0 or 4):
            print('您赢了！')
        elif player_choice_number == 2 and comp_number == (0 or 1):
            print('您赢了！')
        elif player_choice_number == 3 and comp_number == (1 or 2):
            print('您赢了！')
        elif player_choice_number == 4 and comp_number == (2 or 3):
            print('您赢了！')
        else:
            print('计算机赢了！')


# 对程序进行测试
if __name__ == '__main__':
    rpsls()
