#Trivia Game
import random
class Quiz:
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer

class Level:
  def __init__(self, items):
    self.items = items
  
def define_levs(num):
  if num == 1:
    return Level([Quiz("""Where is the Golden Gate Bridge?
    A. San Fransisco
    B. Los Angeles
    C. New York City
    D. San Diago
    """, "A"), Quiz("""Who was in charge of Jim Henson's famous puppets?
    A. Miss Piggy
    B. Skeeter
    C. Kermit the Frog
    D. Fozzie Bear
    """, "C"), Quiz("""Which of these is NOT a mammal?
    A. grizzley bear
    B. human
    C. shark
    D. platypus
    """, "C"), Quiz("""Where does Harry Potter go to school?
    A. Ilvermorney School of Witchcraft and Wizardy
    B. London Public Elementary School
    C. The London Institude for Sorcerers
    D. Hogwarts School of Witchcraft and Wizardry
    """, "D"), Quiz("""The Bubonic Plauge was also known as what?
    A. COVID-19
    B. the Black Plauge
    C. The Red Plague
    D. The Bubonic Pandemic
    """, "B"), Quiz("""Which piece must you capture to win chess?
    A. a pawn
    B. the board
    C. the queen
    D. the king
    """, "D")])
  elif num == 2:
    return Level([Quiz("""Which of these countries in NOT in Africa?
    A. Egypt
    B. Saudi Arabia
    C. Chad
    D. Morroco
    """, "B"), Quiz("""Who directed E.T.?
    A. Steven Spielberg
    B. Tim Burton
    C. Alfred Hitchcock
    D. Fozzie Bear
    """, "A"), Quiz("""Which element has the chemical symbol C? 
    A. carbon dixode
    B. carbon
    C. carbohydrate
    D. calcium
    """, "B"), Quiz("""Who wrote A Christmas Carol?
    A. none of the below
    B. C.S. Lewis
    C. Herman Melvile
    D. Charles Dickens
    """, "D"), Quiz("""Who was the first woman to be an American president?
    A. Martha Washington
    B. Kamala Harris
    C. there haven't been any
    D. Hilary Clinton
    """, "C"), Quiz("""What sport is played in the NBA?
    A. basketball
    B. baseball
    C. billiards
    D. soccer
    """, "A")])

def print_lev(lev, beginner, ameteur, pro, elite, champion, birthday):
  if lev == 1:
    print ("Welcome to the beginner arena!")
    return beginner
  elif lev == 2:
    print ("Welcome to the ameteur arena!")
    return ameteur
  elif lev == 3:
    print ("Welcome to the pro arena!")
    return pro
  elif lev == 4:
    print ("Welcome to the elite arena!")
    return elite
  elif lev == 5:
    print ("Welcome to the champion arena!")
    return champion
  elif lev == True:
    print ("Welcome to Rob's Birthday Arena!")
    return birthday

def main():
  lev = 1
  for round in range(0, 10):
    beginner = define_levs(1)
    ameteur = define_levs(2)
    pl = print_lev(lev, beginner, ameteur, "pro", "elite", "champion", "birthday")
    score = 0
    for sect in range(0, 5):
      print (" ")
      print("Question " + str(sect + 1))
      question = random.randint(0,(len(pl.items)- 1))
      item = pl.items[question]
      print (item.question)
      answ = input("ANSWER: ")
      ans = answ.upper()
      pl.items.remove(item) 
      if ans == item.answer:
        print ("Correct!" )
        score += 1
      elif ans == "12/6":
        print ("Welcome Rob! Happy birthday!")
      else:
        print ("Sorry, that is not correct. The right answer was " + item.answer)
  
    print (score)
    if score > 3:
      if pl != "champion" and pl != "birthday":
        print "Congradulations! You beat the arena!"
        lev += 1
    else:
      if pl != beginner:
        "Unfortunately, you did not beat the area. Better luck next time."
        lev = lev - 1
  


main()


  

    
