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


""" БЛОК АНАЛИЗОВ КРОВИ: ОАК """
print("\033[01;4m{}".format(" ВВЕДИТЕ ЗНАЧЕНИЯ ОБЩЕГО АНАЛИЗА КРОВИ: "))

try:
    wbc = OAK('Лейкоциты', '(WBC)', 0, 4, 9.5, 30, '[10^9 клеток\л]: ')
    print(wbc.show(value=float(input("\033[0m{}".format(wbc.name + wbc.nick + wbc.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + wbc.name + '!'))

try:
    rbc = OAK('Эритроциты', '(RBC)', 0, 3.6, 5.1, 30, '[10^9 клеток\л]: ')
    print(rbc.show(value=float(input("\033[0m{}".format(rbc.name + rbc.nick + rbc.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + rbc.name + '!'))

try:
    hgb = OAK('Гемоглобин', '(HGB)', 30, 130, 160, 300, '[г/л]: ')
    print(hgb.show(value=float(input("\033[0m{}".format(hgb.name + hgb.nick + hgb.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + hgb.name + '!'))

try:
    hct = OAK('Гематокрит', '(HCT)', 25, 39, 49, 80, '[%]: ')
    print(hct.show(value=float(input("\033[0m{}".format(hct.name + hct.nick + hct.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + hct.name + '!'))

try:
    plt = OAK('Тромбоциты', '(PLT)', 0, 150, 450, 1000, '[10^9 клеток\л]: ')
    print(plt.show(value=float(input("\033[0m{}".format(plt.name + plt.nick + plt.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + plt.name + '!'))

try:
    neut = OAK('Нейтрофильные гранулоциты', '(NEUT)', 0, 45, 70, 100, '[%]: ')
    print(neut.show(value=float(input("\033[0m{}".format(neut.name + neut.nick + neut.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + neut.name + '!'))

try:
    neut_p = OAK('Палочкоядерные нейтрофилы', '(NEUT P)', 0, 1, 5, 20, '[%]: ')
    print(neut_p.show(value=float(input("\033[0m{}".format(neut_p.name + neut_p.nick + neut_p.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + neut_p.name + '!'))

try:
    neut_s = OAK('Сегментоядерные нейтрофилы', '(NEUT S)', 0, 1, 5, 20, '[%]: ')
    print(neut_s.show(value=float(input("\033[0m{}".format(neut_s.name + neut_s.nick + neut_s.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + neut_s.name + '!'))

try:
    lymp = OAK('Лимфоциты', '(LYMP)', 0, 22, 46, 100, '[%]: ')
    print(lymp.show(value=float(input("\033[0m{}".format(lymp.name + lymp.nick + lymp.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + lymp.name + '!'))

try:
    mono = OAK('Моноциты', '(MONO)', 0, 2, 9, 30, '[%]: ')
    print(mono.show(value=float(input("\033[0m{}".format(mono.name + mono.nick + mono.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + mono.name + '!'))

try:
    eos = OAK('Эозинофилы', '(EOS)', 0, 1, 5, 20, '[%]: ')
    print(eos.show(value=float(input("\033[0m{}".format(eos.name + eos.nick + eos.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + eos.name + '!'))

try:
    baso = OAK('Базофилы', '(BASO)', 0, 0.01, 1, 20, '[%]: ')
    print(baso.show(value=float(input("\033[0m{}".format(baso.name + baso.nick + baso.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + baso.name + '!'))

try:
    esr = OAK('СОЭ', '(ESR)', 0, 2, 8, 30, '[мм/час]: ')
    print(esr.show(value=float(input("\033[0m{}".format(esr.name + esr.nick + esr.units)))))
except:
    print("\033[31m{}".format('Введены некорректные данные уровня ' + esr.name + '!'))
