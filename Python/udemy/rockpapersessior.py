rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose=[rock,paper,scissors]
random_choose=random.randint(0,2)
print(choose[random_choose])

user=int(input("Type 0 for Rock,1 for paper, 2 for scissor"))
if user==random_choose:
    print("It's Draw")
elif user==0 and random_choose==1:
    print("you loose")
