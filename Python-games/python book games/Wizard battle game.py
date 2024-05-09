import random
class Civilian:
    global hp
    hp = 100
    self_hp = hp
    name = ''
    def reduce_hp(self,deta_hp):
        print(self.name,'受到',deta_hp,'点伤害')
        self_hp -= deta_hp
    def basic_attack(self,enemy):
        print(self.name,'对',enemy.name,'发起攻击')
        enemy.reduce_hp(10)
class Wizard(Civilian):
    global mp
    mp = 100
    def magic_attack(self,enemy):
        if self.mp > 0:
            print(self.name,'消耗10个魔法值',enemy.name,'释放魔法')
            self.mp -= 10
            enemy.reduce_hp(30)
        else:
            self.mp = 0
            print('没有魔法值，无法攻击')
class Warrior(Civilian):
    def basic_attack(self,enemy):
        Civilian.basic_attack(self,enemy)
        print('挑衅:你太弱小了，根本不配跟我战斗！')
    def sword_attack(self,enemy):
        print(self.name,'对',enemy.name,'使用华丽剑技')
        enemy.reduce_hp(20)
achilles = Warrior()
achilles.name = '阿喀琉斯'
heracles = Warrior()
heracles.name = '赫拉克勒斯'
achilles.sword_attack(heracles)
heracles.basic_attack(achilles)

    
