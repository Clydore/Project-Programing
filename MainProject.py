def redintro():
  print """
  Red riding hood has always been happy. Her parents have loved
  her and she's never gone to bed hungry.
  """
  raw_input()
  print """
  She's sitting with her parents at the table with a newspaper
  spread out before them. It was showcasing the jobs that they
  could take.
  """
  raw_input()
  print"""
  Her parents decide to take the far away job. They would be
  gone for  two weeks. Red was happy though. Her parents loved
  her and would be back soon.
  """
  raw_input()
  print """
  two weeks later
  """
  raw_input()
  print """
  Red was sitting next to the door waiting. Her parents had left
  two weeks ago and were about to come home.
  'You shouldn't be sitting next to the window miss' said the
  maid, 'You'll catch a cold miss.' but Red didn't care. Her
  parents were coming home.
  """
  raw_input()
  print"""
  There was a knock on the door. 'Mom! Dad!' shouted red as
  she rushed to the door. But her parent's weren't there.
  On the front step was a man holding a letter. As he handed
  it to her he said 'my condolences miss'
  """
  raw_input()
  print"""
  Red wasn't happy anymore.
  """

def wolfIntro():
  raw_input()
  print """
  You are laying in bed morning the loss of your parents and you can hear the
  slow drops of rain on your roof...
  """
  raw_input()
  print """
  Suddenly there is a knock on the door
  """
  raw_input()

def princeIntro():
  global wolfSword
  if wolfSword == True:
    print """
    It's been five day's since my confrontation with Wolf. Five days that I've
    been carying his sword. Five days since I've found cheshire cat. Five days
    Since I've enbarked on my quest to destroy all of the brothehood and make
    sure no one ever has to suffer the way I did again.
    """
  else:
    print"""
    It's been five day's since my confrontation with Wolf. Five days since 
    I've found cheshire cat. Five days since I've enbarked on my quest to destroy all 
    of the brothehood and make sure no one ever has to suffer the way I did again.
    """
#below this is the global variable libary.

wolfSword = False #whether or not red chose to take scrooges sword


#below this is the story.
redintro()

wolfIntro()

princeIntro()
