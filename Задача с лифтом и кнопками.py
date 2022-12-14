#В доме есть 20 этажей и лифт. Строители забыли вставить в лифт кнопки с этажами. В нём имеются, кнопки, только вверх и вниз.
#Поднимают на 13 этажей, а опускают на 8 этажей. Вы сейчас на 13 этаже, вам нужно на 8. За сколько итераций вы это сделаете?
#Лифт передвигается в пределах дома. Не выше 20 и не ниже 1 этажа.


def down(now):
    if (now - 8) < 1:
        print(f"You upped in {now+13}")
        return now + 13
    else:
        print(f"You downing in {now-8}")
        return now - 8


def up(now):
    if (now + 13) > 20:
        print(f"You downing in {now-8}")
        return now - 8
    else:
        print(f"You upped in {now+13}")
        return now + 13


now = 13
count = 0
for i in range (1,50):
    if now > 8:
        now = down(now)
        count+=1
    elif now < 8:
        now = up(now)
        count +=1
print(f"Вы опустились на 8 этаж за {count} шагов")
        
