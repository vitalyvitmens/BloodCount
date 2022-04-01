class OAK:
    name = ''
    nick = ''
    min = float or int
    max = float or int
    max_2 = float or int
    units = ''

    def show(self, value):
        if 0 < value < self.min:
            print("\033[33m{}".format(self.name + ' понижены!'))
        elif self.min <= value <= self.max:
            print("\033[32m{}".format(self.name + ' в норме!'))
        elif self.max < value <= self.max_2:
            print("\033[31m{}".format(self.name + ' повышены!'))
        # elif self.value is None or str:
        #     print("\033[31m{}".format('Данные ' + self.name + ' не введены!'))
        else:
            print("\033[31m{}".format('Введены некорректные данные уровня ' + self.name + '!'))


wbc = OAK()
wbc.name = 'Лейкоциты'
wbc.nick = '(WBC)'
wbc.min = 4
wbc.max = 9.5
wbc.max_2 = 30
wbc.units = '[10^9 клеток\л]: '
print(wbc.show(value=float(input("\033[0m{}".format(wbc.name + wbc.nick + wbc.units)))))


rbc = OAK()
rbc.name = 'Эритроциты'
rbc.nick = '(RBC)'
rbc.min = 3.6
rbc.max = 5.1
rbc.max_2 = 30
rbc.units = '[10^9 клеток\л]: '
print(rbc.show(value=float(input("\033[0m{}".format(rbc.name + rbc.nick + rbc.units)))))

