print('Игра началась!')

desk = list(range(1,10))

def draw_desk(desk):
   print("-" * 13)
   for i in range(3):
      print("|", desk[0+i*3], "|", desk[1+i*3], "|", desk[2+i*3], "|")
      print("-" * 13)

def take_input(player):
   valid = False
   while not valid:
      ans = input("Куда поставим " + player+"? ")
      try:
         ans = int(ans)
      except:
         print("Это не число")
         continue
      if ans >= 1 and ans <= 9:
         if(str(desk[ans-1]) not in "XO"):
            desk[ans-1] = player
            valid = True
         else:
            print("Клетка занята!")
      else:
        print("Это клетка за пределами поля!")

def check_win(desk):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if desk[each[0]] == desk[each[1]] == desk[each[2]]:
          return desk[each[0]]
   return False

def func(desk):
    counter = 0
    win = False
    while not win:
        draw_desk(desk)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(desk)
           if tmp:
              print(tmp, "победил!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_desk(desk)
func(desk)