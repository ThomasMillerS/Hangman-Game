import pygame
pygame.init()
window = pygame.display.set_mode([500,500])
window.fill((0,0,0))
white = (255,255,255)
win = False
wrong = 0
guess = 1
correct = False
word = []
wordg = []
wordp = ("")
length = int(input("Enter the length of your word: "))
count = 1
while count <= length:
    letter = input("Enter letter number " + str(count) + ": ")
    count += 1
    word.append(letter)
count = 1
while count <= length:
    wordg.append("_")
    count += 1
print("\n" * 50)
print("The word is " + str(length) + " letters long.")
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
    count = 1
    wordp = ("")
    while count <= length:
        wordp += wordg[(count - 1)]
        wordp += " "
        count += 1
    count = 1
    print(wordp)
    print()
    print("This is guess number " + str(guess) + ".")
    answer = input("Enter your guess: ")
    print("\n" * 2)
    count = 1
    while count <= length:
        if answer == word[(count - 1)]:
            wordg[(count - 1)] = answer
            correct = True
        count += 1
    count = 1
    if correct:
        print("Correct!")
    elif not correct:
        print("Incorrect")
        wrong += 1
        if wrong > 1:
            print("You have " + str(wrong) + " failed attempts.")
        elif wrong == 1:
            print("You have 1 failed attempt.")
    correct = False
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
    if word == wordg:
        win = True
        run = False
    if wrong == 6:
        run = False
    pygame.display.flip()
print()
wordp = ("")
if win:
    while count <= length:
        wordp += word[(count - 1)]
        count += 1
    print("Word: " + wordp)
    count = 1
    print()
    print("You won!")
else:
    while count <= length:
        wordp += word[(count - 1)]
        count += 1
    print("Word: " + wordp)
    count = 1
    print()
    print("You failed.")
