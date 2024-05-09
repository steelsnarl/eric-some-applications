from random import randint
from time import sleep
for i in range(50):
    print('\n')
        
play_again = 'y'
while play_again == 'y':
    turn = 1
    Pscore = 0
    Cscore = 0
    while turn <= 10:
        print('第'+str(turn)+'回合')
        playor = input('您要输入什么(剪刀,石头,布，退出)\n输入: ')
        cpu = randint(0,2)
        if playor == '剪刀' or playor == '石头' or playor == '布':
            print('你输入了'+ playor)
            if cpu == 0:
                CPU = '剪刀'
                print('计算机输入了剪刀')
            if cpu == 1:
                CPU = '石头'
                print('计算机输入了石头')
            if cpu == 2:
                CPU = '布'
                print('计算机输入了布')
            if playor == CPU:
                print('打平了')
            elif (playor == '剪刀' and CPU == '石头') or (playor == '石头' and CPU == '布') or (playor == '布' and CPU == '剪刀') :
                print('你输了!!!')
                Cscore +=1
            elif (playor == '剪刀' and CPU == '布') or (playor == '石头' and CPU == '剪刀') or (playor == '布' and CPU == '石头') :
                print('你赢了!!!')
                Pscore += 1
            elif playor == '退出':
                print('再见')
                break
            turn += 1
        else:
            print('输入错误')
            Pscore -= 1
            break
    if (Cscore == Pscore):
        print('你有'+str(Pscore)+'分,'+'计算机有'+str(Cscore)+'分,打平了.')
    elif (Pscore  > Cscore):
        print('你有'+str(Pscore)+'分,'+'计算机有'+str(Cscore)+'分,你赢了!')
    else:
        print('你有'+str(Pscore)+'分,'+'计算机有',str(Cscore)+'分,你输了.')
    play_again = input('要在玩一次吗(y/n)?\n输入: ')
sleep(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    
