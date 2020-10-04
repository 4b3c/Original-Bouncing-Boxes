import pygame, random, time
pygame.init()

black = (0, 0, 0)
red = (230, 30, 30)
green = (30, 230, 30)
white = (255, 255, 255)
Score = 1

player_x = random.randint(100, 900)
player_y = random.randint(100, 500)
player_x = int(player_x / 20) * 20
player_y = int(player_y / 20) * 20

food_x = random.randint(100, 900)
food_y = random.randint(100, 500)
food_x = int(food_x / 20) * 20
food_y = int(food_y / 20) * 20

direction = 1
list = [(0, 0)]
Score = 0
string = str(Score - 1)
HighScore = Score
high_string = "HighScore = " + str(HighScore)
font = pygame.font.Font("freesansbold.ttf", 28)
fontbig = pygame.font.Font("freesansbold.ttf", 110)
Playtxt = fontbig.render("Snake", True, (white), (black))
PlayTextBox = Playtxt.get_rect()
PlayTextBox = (280, 70)
Quittxt = font.render("Quit", True, (white), (black))
QuitTextBox = Quittxt.get_rect()
QuitTextBox = (861, 54)
lvl1 = font.render("Easy", True, (white), (black))
lvl1Box = lvl1.get_rect()
lvl1Box = (81, 54)
lvl2 = font.render("Medium", True, (white), (black))
lvl2Box = lvl2.get_rect()
lvl2Box = (81, 134)
lvl3 = font.render("Hard", True, (white), (black))
lvl3Box = lvl3.get_rect()
lvl3Box = (81, 214)
ScoreText = font.render(string, True, (white), (black))
ScoreBox = ScoreText.get_rect()
ScoreBox = (800, 30)
HighScoreText = font.render(high_string, True, (white), (black))
HighScoreBox = HighScoreText.get_rect()
HighScoreBox = (700, 134)
instructions = font.render("Instructions", True, (white), (black))
instBox = instructions.get_rect()
instBox = (762, 214)
Instructions = font.render("Use the arrow keys to change the direction of your \"Snake\". Your goal is to eat the green food.", True, (white), (black))
InstructionsBox =Instructions.get_rect()
InstructionsBox = (30, 30)
back = font.render("Back", True, (white), (black))
backBox = instructions.get_rect()
backBox = (58, 515)

game_running = True
playing = False
screen = pygame.display.set_mode((1000, 600))

while game_running == True:
    running = False
    screen.fill(black)
    pygame.draw.rect(screen, (white), (70, 50, 90, 40), 4)
    pygame.draw.rect(screen, (white), (70, 130, 130, 40), 4)
    pygame.draw.rect(screen, (white), (70, 210, 90, 40), 4)
    pygame.draw.rect(screen, (white), (850, 50, 80, 40), 4)
    pygame.draw.rect(screen, (white), (690, 130, 240, 40), 4)
    pygame.draw.rect(screen, (white), (755, 210, 175, 40), 4)
    screen.blit(Playtxt, PlayTextBox)
    screen.blit(Quittxt, QuitTextBox)
    screen.blit(lvl1, lvl1Box)
    screen.blit(lvl2, lvl2Box)
    screen.blit(lvl3, lvl3Box)
    screen.blit(HighScoreText, HighScoreBox)
    screen.blit(instructions, instBox)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        epic = pygame.mouse.get_pos()     
        if epic[0] > 70 and epic[0] < 160 and epic[1] > 50 and epic[1] < 90:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                playing = True
                speed = 0.11
                player_x = random.randint(100, 900)
                player_y = random.randint(100, 500)
                player_x = int(player_x / 20) * 20
                player_y = int(player_y / 20) * 20
                Score = 1
                list = [(0, 0)]
        if epic[0] > 70 and epic[0] < 200 and epic[1] > 130 and epic[1] < 170:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                playing = True
                speed = 0.08
                player_x = random.randint(100, 900)
                player_y = random.randint(100, 500)
                player_x = int(player_x / 20) * 20
                player_y = int(player_y / 20) * 20
                Score = 1
                list = [(0, 0)]
        if epic[0] > 70 and epic[0] < 160 and epic[1] > 210 and epic[1] < 250:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                playing = True
                speed = 0.06
                player_x = random.randint(100, 900)
                player_y = random.randint(100, 500)
                player_x = int(player_x / 20) * 20
                player_y = int(player_y / 20) * 20
                Score = 1
                list = [(0, 0)]
        if epic[0] > 755 and epic[0] < 880 and epic[1] > 210 and epic[1] < 250:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                screen.fill(black)
                screen.blit(Instructions, InstructionsBox)
                pygame.draw.rect(screen, (white), (50, 510, 90, 40), 4)
                screen.blit(back, backBox)
                time.sleep(5)
                
        if epic[0] > 850 and epic[0] < 930 and epic[1] > 50 and epic[1] < 90:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                pygame.quit()
                quit()
        
    while playing == True:
        screen.fill(black)
        string = "Score = " + str(Score - 1)
        ScoreText = font.render(string, True, (white), (black))
        screen.blit(ScoreText, ScoreBox)
        if Score - 1 > HighScore:
            HighScore = Score - 1
            high_string = "HighScore = " + str(HighScore)
            HighScoreText = font.render(high_string, True, (white), (black))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and direction != 3: direction = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and direction != 4: direction = 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and direction != 1: direction = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and direction != 2: direction = 4
        
        if player_x > 0 and player_x < 980 and player_y > 0 and player_y < 580:
            if direction == 1: player_y = player_y - 20
            if direction == 2: player_x = player_x + 20
            if direction == 3: player_y = player_y + 20
            if direction == 4: player_x = player_x - 20
        else:
            playing = False
        
        if player_x == food_x and player_y == food_y:
            food_x = random.randint(100, 900)
            food_y = random.randint(100, 500)
            food_x = int(food_x / 20) * 20
            food_y = int(food_y / 20) * 20
            Score = Score + 1
            i = 0
        
        coordinates = (player_x, player_y)
        list.insert(0, coordinates)
        if len(list) > Score:
            del list[Score]
            
        i = 0
        while i < Score:
            coordinates = list[i]
            pygame.draw.rect(screen, (red), (coordinates[0], coordinates[1], 20, 20))
            i = i + 1
        
        i = 2
        while i < len(list):
            coordinates = list[i]
            if player_x == coordinates[0] and player_y == coordinates[1]:
                playing = False
            i = i + 1
                
        pygame.draw.rect(screen, (white), (player_x, player_y, 20, 20))
        pygame.draw.rect(screen, (green), (food_x, food_y, 20, 20))
        pygame.draw.rect(screen, (red), (0, 0, 1000, 600), 20)
        time.sleep(speed)
        
        pygame.display.flip()
