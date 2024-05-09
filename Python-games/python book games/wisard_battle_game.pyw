class Civilian:
    hp = 100
    name = ''
    def reduce_hp(self,deta_hp):
        print(self.name,'受到',deta.hp,'点伤害')
        self_hp -= deta_hp
    def basic_attack(self,enemy):
        print(self.name,'对',enemy.name,'发起攻击')
        enemy.reduce_hp(10)
class Wisard(Civilian):
    mp = 100
    def magic_attack(self,enemy):
        if self.mp > 0:
            print(self.name,'消耗10个魔法值',enemy.name,'释放魔法')
            self.mp -= 10
            enemy.reduce_hp(30)
        else:
            self.mp = 0
            print('没有魔法值，无法攻击')
