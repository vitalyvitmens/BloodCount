class OAK:
    def __init__(self, name, nick, limit_low, minimum_reference, maximum_reference, limit_high, units):
        self.name = name
        self.nick = nick
        self.limit_low = limit_low
        self.minimum_reference = minimum_reference
        self.maximum_reference = maximum_reference
        self.limit_high = limit_high
        self.units = units

    def show(self, value):
        if self.limit_low < value < self.minimum_reference:
            print("\033[33m{}".format(self.name + ' понижены!'))
        elif self.minimum_reference <= value <= self.maximum_reference:
            print("\033[32m{}".format(self.name + ' в норме!'))
        elif self.maximum_reference < value <= self.limit_high:
            print("\033[31m{}".format(self.name + ' повышены!'))
        else:
            print("\033[31m{}".format('Введены некорректные данные уровня ' + self.name + '!'))


wbc = OAK('Лейкоциты', '(WBC)', 0, 4, 9.5, 30, '[10^9 клеток\л]: ')
print(wbc.show(value=float(input("\033[0m{}".format(wbc.name + wbc.nick + wbc.units)))))

rbc = OAK('Эритроциты', '(RBC)', 0, 3.6, 5.1, 30, '[10^9 клеток\л]: ')
print(rbc.show(value=float(input("\033[0m{}".format(rbc.name + rbc.nick + rbc.units)))))

hgb = OAK('Гемоглобин', '(HGB)', 30, 130, 160, 300, '[г/л]: ')
print(hgb.show(value=float(input("\033[0m{}".format(hgb.name + hgb.nick + hgb.units)))))
