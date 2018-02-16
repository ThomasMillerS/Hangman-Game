import pygame
pygame.init()
window = pygame.display.set_mode([500,500])
window.fill((0,0,0))
white = (255,255,255)
win = False
wrong = 0
guess = 1
a = "_ "
p = "_ "
l = "_ "
e = "_"

print("The word is 5 letters long.")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.line(window,white,(100,450),(450,450),5)
    pygame.draw.line(window,white,(150,450),(150,50),5)
    pygame.draw.line(window,white,(150,50),(350,50),5)
    pygame.draw.line(window,white,(350,50),(350,75),5)
    pygame.display.flip()
    print()
    print(a + p + p + l + e)
    print()
    print("This is guess number " + str(guess) + ".")
    answer = input("Enter your guess: ")
    print()
    print()
    print()
    if answer == "a":
        print("Correct!")
        a = "a "
    elif answer == "p":
        print("Correct!")
        p = "p "
    elif answer == "l":
        print("Correct!")
        l = "l "
    elif answer == "e":
        print("Correct!")
        e = "e "
    else:
        print("Incorrect")
        wrong += 1
        if wrong > 1:
            print("You have " + str(wrong) + " failed attempts.")
        elif wrong == 1:
            print("You have 1 failed attempt.")
    if wrong >= 1:
        pygame.draw.circle(window,white,(350,110),35,5)
    if wrong >= 2:
        pygame.draw.line(window,white,(350,145),(350,270),5)
    if wrong >= 3:
        pygame.draw.line(window,white,(350,150),(300,240),5)
    if wrong >= 4:
        pygame.draw.line(window,white,(350,150),(400,240),5)
    if wrong >= 5:
        pygame.draw.line(window,white,(350,270),(300,365),5)
    if wrong >= 6:
        pygame.draw.line(window,white,(350,270),(400,365),5)
    guess += 1
    if (a + p + p + l + e) == "a p p l e ":
        win = True
        run = False
    if wrong == 6:
        run = False
    pygame.display.flip()
print()
if win:
    print(a + p + p + l + e)
    print()
    print("You won!")
else:
    print("You failed.")
