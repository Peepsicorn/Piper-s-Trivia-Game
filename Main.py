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
    """, "B"), Quiz("""Which piece must you checkmate to win chess?
    A. a pawn
    B. the board
    C. the queen
    D. the king
    """, "D"), Quiz("""What is the biggest country in the world?
    A. U.S.A.
    B. Russia
    C. Spain
    D. Kansas
    """, "B"), Quiz("""What does TV stand for?
    A. Terrible Vision
    B. Televison
    C. Telephone
    D. Timed Viewing
    """, "C"), Quiz("""Which of these is a star?
    A. Earth
    B. the Big Dipper
    C. the sun
    D. Pluto
    """, "C"), Quiz("""Where is the Louve Muesam?
    A. Paris
    B. London 
    C. Berlin
    D. Hogwarts 
    """, "A"), Quiz("""Who was Benjamin Franklin?
    A. a U.S. president
    B. the king of England
    C. an inventor
    D. a famous hockey player
    """, "C"), Quiz("""Which of these sports would NOT be played in the winter olympics?
    A. ice hockey
    B. swimming
    C. speed skating
    D. curling
    """, "B")])
  elif num == 2:
    return Level([Quiz("""Which of these countries in NOT in Africa?
    A. Egypt
    B. Saudi Arabia
    C. Chad
    D. Morocco
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
    """, "A"), Quiz("""Who was the Queen of England in 2020?
    A. Queen Elizabeth II
    B. Queen Victoria
    C. Queen Beyonce
    D. King Henry V
    """, "A"), Quiz("""A standerd guitar has how many strings?
    A. 5
    B. 6
    C. 7
    D. 8
    """, "B"), Quiz("""Animals that eat meat are called what?
    A. herbavores
    B. omnivores
    C. carnivores
    D. ATEM
    """, "C"), Quiz("""Who painted the Mona Lisa?
    A. Van Gogh
    B. Vermeer
    C. Degas
    D. Da Vinci
    """, "D"), Quiz("""What was the Titanic marketed as?
    A. The First Flying Ship
    B. The Unsinkable Ship
    C. The Greatest Ship
    D. The Most Comfortble Ship in America
    """, "B"), Quiz("""Which one of these is NOT a card game?
    A. Hearts
    B. Castle
    C. Poker
    D. Mancala
    """, "D")])
  elif num == 3:
    return Level([Quiz("""Which of these states is NOT part of the Rocky Mountain Range?
    A. Idaho
    B. Colorado
    C. Nevada
    D. all of the above
    """, "C"), Quiz("""What is the Twitter equivilent of posting on Facebook?
    A. Tweeting
    B. Posting
    C. Chirping
    D. Friending
    """, "A"), Quiz("""What species is Canis Familiaris?
    A. a wolf
    B. a household dog
    C. a coyote
    D. a human
    """, "B"), Quiz("""How many paintings did Vincent Van Gogh sell in his lifetime?
    A. 196
    B. 23
    C. 0
    D. 1
    """, "D"), Quiz("""What day did wWII end?
    A. D-day
    B. V-K Day
    C. V-J Day
    D. V-G Day
    """, "C"), Quiz("""What is the record for the most red cards given in a soccer game?
    A. 6
    B.11
    C. 36
    D. 24
    """, "C"), Quiz("""What country accounts for more than half of the western coast of South America?
    A. Ecuador
    B. Peru
    C. Brazil
    D. none of the above
    """, "D"), Quiz("""What does Taser stand for?
    A. Two-dart Axon Serious Electroshock Rifle
    B. Thomas A Swift Electic Rifle
    C. Terribly Advertisied So-so Electric Rifle
    D. none of these, it's not an acronym
    """, "B"), Quiz("""A t-rex leaves gient footprints that turn into what type of fossils?
    A. carbon film
    B. mold
    C. cast
    D. trace
    """, "D"), Quiz("""What is the name of the head pig in Animal Farm?
    A. Old Major
    B. Snowball
    C. Napolean
    D. Hamm
    """, "C"), Quiz("""How many Catherines did Henry VIII marry?
    A. 1
    B. 2
    C. 3
    D. 4
    """, "C"), Quiz("""How long have humans been riding horses?
    A. 5,000 years
    B. 6,000 years
    C. 7,000 years
    D. 8,000 years
    """, "B")])
  elif num == 4:
    return Level([Quiz("""Which of the fallowing is NOT a caital city?
    A. Berlin, Germany
    B. Sidney, Austrailia
    C. Moscow, Russia
    D. Bamako, Mali
    """, "B"), Quiz("""Of these broadway musicals, which is the highest grossing?
    A. Cats
    B. Les Miserables
    C. Hamilton
    D. Wicked
    """, "D"), Quiz("""How many hearts does an octopus have?
    A. 1
    B. 2
    C. 3
    D. 4
    """, "C"), Quiz("""Where did the pop art movement originate?
    A. England 
    B. U.S.A.
    C. Germany
    D. The Netherlands
    """, "A"), Quiz("""Which of these was NOT a use for the Roman forum?
    A. school
    B. trade
    C. worship
    D. theater
    """, "D"), Quiz("""How long is a olympic swimming pool?
    A. 25 meters
    B. 50 meters
    C. 75 meters
    D. none of the above
    """, "B"), Quiz("""How many deserts are in Europe?
    A. 0
    B. 1
    C. 2
    D. 3
    """, "A"), Quiz("""What was Jabberwocky?
    A. a song
    B. a book
    C. a poem
    D. a play
    """, "C"), Quiz("""Which crystalline formations are on cave cealings?
    A. crystals
    B. stalagtites
    C. stalagmites
    D. diamonds
    """, "B"), Quiz("""Which of these items was patented first?
    A. the cash register
    B. chewing gum
    C. the rubber band
    D. the dishwasher
    """, "A"), Quiz("""How many pounds of candy is sold in the U.S. each year?
    A. 1 million
    B. 2 million
    C. 3 million
    D. 600 million
    """, "D"), Quiz("""How many balls is a golfer allowed to carry?
    A. 5
    B. 10
    C. 15
    D. none of the above
    """, "D")])
  elif num == 5:  
    return Level([Quiz("""How many countries border Germany?
    A. 2
    B. 3
    C. 4
    D. 9
    """, "D"), Quiz("""What is the oldest suriving musical instument?
    A. flute
    B. lyre
    C. bagpipes
    D. drum
    """, "A"), Quiz("""What did Albert Einsten win the Nobel Prize for in 1921?
    A. Photoelectic effect
    B. relativity
    C. zero-point energy
    D. all of the above
    """, "B"), Quiz("""Mary Shelley's most famous book is titled Frankenstien or the Modern _______?
    A. Saten
    B. Prometheus
    C. Genesis
    D. Monster
    """, "B"), Quiz("""Which of these U.S. presidents was NOT assainated?
    A. William McKinley
    B. Benjamin Harrison
    C. James Garfield
    D. A and C
    """, "B"), Quiz("""Which of these is NOT a reason mulch is used for gardening?
    A. to prevent weeds
    B. to keep soil cool
    C. to dry soil out
    D. to make the garden look better
    """, "C"), Quiz("""Which Beatle had dyslexia?
    A. Paul Mccartney
    B. Jhon Lennon
    C. Ringo Star
    D. George Harris
    """, "B"), Quiz("""How many ribs are in the human body?
    A. 20
    B. 24
    C. 30
    D. 38
    """, "B"), Quiz("""What is the square root of the area of Vatican City?
    A. 0.44 km
    B. 0.52 km
    C. 0.23 km
    D. 0.01 km
    """, "A"), Quiz("""What does J.K. in J.K. Rowling stand for?
    A. Josie Kate
    B. June Kimberly
    C. Joanne Katherine
    D. Julia Kylie
    """, "B"), Quiz("""During which one of these years was the war of 1812 being fought?
    A. 1811
    B. 1812
    C. 1813
    D. B and C
    """, "B"), Quiz("""Which of these chilren's games DOES NOT need words to play?
    A. Mr. Fox
    B. Marco Polo
    C. Keep Away
    D. Mafia
    """, "D")])
  elif num == 6:
    return Level ([Quiz("""What first happened on December 6th?
    A. the Encylopedia Brittianica was published
    B. a city hosted licensed taxicabs
    C. an edition of the Washington Post was published
    D. all of the above
    """, "D"), Quiz("""Which of these important events happened on December 6th?
    A. NASA released photgraphs suggesting liquid on Mars
    B. the Washington Monument was completed
    C. 13th Amendment to the Constitution was ratified
    D. all of the above
    """, "D"), Quiz("""Which of these people were born on December 6th?
    A. Henry VI
    B. The daughter of Marie Curie
    C. The son of Johannes Bach
    D. all of the above
    """, "D"), Quiz("""Who died on December 6th?
    A. Saint Nicholas
    B. discoverer of carbon dioxide, Joseph Black
    C. Jefferson Davis
    D. all of the above
    """, "D"), Quiz("""What is the zodiac sign of December 6th?
    A. Gemini
    B. Pisces
    C. Sagittarius
    D. none of the above
    """, "C"), Quiz("""What is the birthstone color of December?
    A. Green
    B. Blue
    C. Red
    D. none of the above
    """, "B")])

def create_pu():
  pu = random.randint(10000, 99999)
  return str(pu)

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
  elif lev == 10:
    print ("Welcome to Rob's Birthday Arena!")
    return birthday

def main():
  lev = 1
  streak = 0
  print ("Welcome to Emma and Piper's trivia game!")
  print ("There are five areanas to get through in this game, each with five questions. Answer four or more correctly and you move ahead! But, be careful! Answer three or less correctly and you'll move down a arena. If you get five questions in a row, you'll earn a power-up which you can use to answer any question to get it correct. You can only hold one power-up at a time. Good luck!")
  print ("")
  power = True
  for round in range(0, 10):
    beginner = define_levs(1)
    ameteur = define_levs(2)
    pro = define_levs(3)
    elite = define_levs(4)
    champion = define_levs(5)
    birthday = define_levs(6)
    pl = print_lev(lev, beginner, ameteur, pro, elite, champion, birthday)
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
        streak += 1
      elif ans == "12/6":
        print ("Welcome Rob! Happy birthday!")
        lev = 10
        break
      elif ans == power:
        print ("Power-up used")
        score += 1
        power = False
      else:
        print ("Sorry, that is not correct.")
        streak = 0
      
      if streak == 5:
        power = create_pu()
        print ("Congrats! You got a power-up: " + power)
        streak = 0
      else:
        print ("You're streak is " + str(streak))

    if score > 3:
      if pl != champion and pl != birthday:
        print ("Congradulations! You beat the arena!")
        lev += 1
      else:
        print ("Great job! Thanks for playing.")
        break
    else:
      if pl != beginner and pl != birthday:
        ("Unfortunately, you did not beat the area. Better luck next time.")
        lev = lev - 1
  
  print ("")
  print ("""Credits:
  This game is dedicated to one of the best fathers of all time: Robert Mathews
  Designed by: Emma and Piper Mathews
  Coded by: Piper Mathews
  Questions by: Piper Mathews with help from Google
  Produced by Peepsicorn Games""")
      
  


main()


  

    
