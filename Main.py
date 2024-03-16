import random
import pygame
import socket
import threading
import TKinterGUI  # Assuming this is a custom module for TKinter GUI's

# Initialize pygame
pygame.init()
pygame.font.init()

# Set up the game window
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('AQADo Game')

# Load game assets
Board = pygame.image.load('Board.png')
p11_image = pygame.image.load('P11.png')
p12_image = pygame.image.load('P12.png')
p21_image = pygame.image.load('P21.png')
p22_image = pygame.image.load('P22.png')

# Set up fonts
font = pygame.font.SysFont('Calibri Body', 50)
font_big = pygame.font.SysFont('Calibri Body', 500)

# Initialize player positions and names
p11 = 0
p12 = 0
p21 = 0
p22 = 0
player1_name = '1'
player2_name = '2'
current_player = 2
current_player_name = player1_name


# Function to handle die movement action
def Die_Moving_Action(die):
    global p11, p12, p21, p22, current_player, die_to_move
    if die_to_move == 'p11':
        temp = p11
    elif die_to_move == 'p12':
        temp = p12
    elif die_to_move == 'p21':
        temp = p21
    elif die_to_move == 'p22':
        temp = p22

    temp1 = 0
    output = 0

    if die == 1:
        output = 1
    elif die == 2:
        output = 2
    elif die == 3:
        output = 3
    elif die == 4:
        output = -1
    elif die == 5:
        if temp < p11 and temp1 < p11:
            temp1 = p11 + 1
            output = temp1 - temp
        elif temp < p12 and temp1 < p12:
            temp1 = p12 + 1
            output = temp1 - temp
        elif temp < p21 and temp1 < p21:
            temp1 = p21 + 1
            output = temp1 - temp
        elif temp < p22 and temp1 < p22:
            temp1 = p22 + 1
            output = temp1 - temp
        if output + temp >= 10:
            output = 0
    return output

# Function to draw the game window
def Game_Window_Draw(c1, c2, c3, c4, cp):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if 787 <= location[0] <= 1067:
                    if 540 <= location[1] <= 640:
                        return 'pressed'

        screen.fill((0, 0, 124))

        screen.blit(Board, (0, 0))
        screen.blit(p11_image, (100, 658 - (c1 * 65)))
        screen.blit(p12_image, (200, 658 - (c2 * 65)))
        screen.blit(p21_image, (450, 658 - (c3 * 65)))
        screen.blit(p22_image, (550, 658 - (c4 * 65)))

        title0 = font.render('Player ' + str(cp) + ' to play', False, (255, 255, 255))
        screen.blit(title0, (787, 100))
        title1 = font.render('Press the button', False, (255, 255, 255))
        screen.blit(title1, (787, 160))
        title2 = font.render('to roll the dice', False, (255, 255, 255))
        screen.blit(title2, (805, 190))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((777, 230), (300, 300)), 0, 10)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((787, 540), (280, 100)), 0, 25)
        button = font.render('Push', False, (255, 255, 255))
        screen.blit(button, (885, 575))

        pygame.display.flip()
        clock.tick(60)

# Function waiting for next player move
def Waiting_Window_Draw(c1, c2, c3, c4):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 124))

        screen.blit(Board, (0, 0))
        screen.blit(p11_image, (100, 658 - (c1 * 65)))
        screen.blit(p12_image, (200, 658 - (c2 * 65)))
        screen.blit(p21_image, (450, 658 - (c3 * 65)))
        screen.blit(p22_image, (550, 658 - (c4 * 65)))

        title1 = font.render('Waiting for other', False, (255, 255, 255))
        screen.blit(title1, (787, 350))
        title2 = font.render(' player to play', False, (255, 255, 255))
        screen.blit(title2, (787, 380))

        pygame.display.flip()
        return client_socket.recv(1024)
        clock.tick(60)

def AI_Waiting_Window_Draw(c1, c2, c3, c4):
    counter = 0
    while True:
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 124))

        screen.blit(Board, (0, 0))
        screen.blit(p11_image, (100, 658 - (c1 * 65)))
        screen.blit(p12_image, (200, 658 - (c2 * 65)))
        screen.blit(p21_image, (450, 658 - (c3 * 65)))
        screen.blit(p22_image, (550, 658 - (c4 * 65)))

        title1 = font.render('Waiting for', False, (255, 255, 255))
        screen.blit(title1, (787, 350))
        title2 = font.render('AI to play', False, (255, 255, 255))
        screen.blit(title2, (787, 380))

        pygame.display.flip()
        clock.tick(60)
        if counter == 120:
            break

# Function to draw the game playing window
def Game_Playing_Window_Draw(c1, c2, c3, c4, num, cp, pn):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if cp == 1:
                    if 100 <= location[0] <= 155:
                        if (658 - (c1 * 65)) <= location[1] <= (658 - (c1 * 65) + 57):
                            return 'p11'

                    if 200 <= location[0] <= 255:
                        if (658 - (c2 * 65)) <= location[1] <= (658 - (c2 * 65) + 57):
                            return 'p12'
                else:
                    if 450 <= location[0] <= 505:
                        if (658 - (c3 * 65)) <= location[1] <= (658 - (c3 * 65) + 57):
                            return 'p21'

                    if 550 <= location[0] <= 605:
                        if (658 - (c4 * 65)) <= location[1] <= (658 - (c4 * 65) + 57):
                            return 'p22'

        screen.fill((0, 0, 124))

        screen.blit(Board, (0, 0))
        screen.blit(p11_image, (100, 658 - (c1 * 65)))
        screen.blit(p12_image, (200, 658 - (c2 * 65)))
        screen.blit(p21_image, (450, 658 - (c3 * 65)))
        screen.blit(p22_image, (550, 658 - (c4 * 65)))

        title1 = font.render('The number is', False, (255, 255, 255))
        screen.blit(title1, (805, 190))

        dieroll = font_big.render(str(num), False, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((777, 230), (300, 300)), 0, 10)
        screen.blit(dieroll, (830, 225))
        text1 = font.render('Player ' + str(pn) + ' to play', False, (255, 255, 255))
        screen.blit(text1, (805, 550))
        pygame.display.flip()
        clock.tick(60)

# Function to handle illegal moves
def Game_Illegal_Move(c1, c2, c3, c4, num):
    counter = 0
    while True:
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if 787 <= location[0] <= 1067:
                    if 540 <= location[1] <= 640:
                        return 'hi'

        screen.fill((0, 0, 124))

        screen.blit(Board, (0, 0))
        screen.blit(p11_image, (100, 658 - (c1 * 65)))
        screen.blit(p12_image, (200, 658 - (c2 * 65)))
        screen.blit(p21_image, (450, 658 - (c3 * 65)))
        screen.blit(p22_image, (550, 658 - (c4 * 65)))

        error = font.render('Illegal move', False, (255, 0, 0))
        error1 = font.render('Please try again', False, (255, 0, 0))
        screen.blit(error, (805, 130))
        screen.blit(error1, (805, 160))
        title1 = font.render('The number is', False, (255, 255, 255))
        screen.blit(title1, (805, 190))

        dieroll = font_big.render(str(num), False, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((777, 230), (300, 300)), 0, 10)
        screen.blit(dieroll, (830, 225))

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((787, 540), (280, 100)), 0, 25)

        button = font.render('OK', False, (255, 255, 255))
        screen.blit(button, (885, 575))

        pygame.display.flip()
        clock.tick(60)

# Function to handle situations where there are no legal moves
def No_Legal_Move():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if 170 <= location[0] <= 470:
                    if 300 <= location[1] <= 400:
                        return 'hi'

        screen.fill((0, 0, 124))
        text = font.render('No legal move with the die ', False, (255, 0, 0))
        screen.blit(text, (100, 130))
        text1 = font.render(' rolled, so next player turn', False, (255, 0, 0))
        screen.blit(text1, (100, 175))

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((170, 300), (300, 100)), 0, 25)
        button = font.render('OK', False, (255, 255, 255))
        screen.blit(button, (280, 335))

        pygame.display.flip()
        clock.tick(60)

# Function to check the legality of moves
def Check_Legality(c1, c2, c3, c4, counter, die):
    global die_to_move
    die_to_move = counter
    output = 'legal'
    change = Die_Moving_Action(die)

    if counter == 'p11':
        current = c1
        changed = Die_Moving_Action(die) + c1
    elif counter == 'p12':
        current = c2
        changed = Die_Moving_Action(die) + c2
    elif counter == 'p21':
        current = c3
        changed = Die_Moving_Action(die) + c3
    elif counter == 'p22':
        current = c4
        changed = Die_Moving_Action(die) + c4

    if changed != 0 and changed != 4 and changed != 10:
        if counter == 'p11' and changed == c2:
            output = 'False'
        elif counter == 'p12' and changed == c1:
            output = 'False'
        elif counter == 'p21' and changed == c4:
            output = 'False'
        elif counter == 'p22' and changed == c3:
            output = 'False'
        if current == 0 and change == -1:
            output = 'False'
        elif current == 10 and change != -1:
            output = 'False'

    return output

# Function to handle victory conditions
def Victory(player_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if 170 <= location[0] <= 470:
                    if 300 <= location[1] <= 400:
                        return 'hi'

        screen.fill((0, 0, 124))
        text = font.render('The winner is:', False, (255, 255, 255))
        screen.blit(text, (200, 130))
        text1 = font.render(player_name, False, (255, 255, 255))
        screen.blit(text1, (200, 175))

        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((170, 300), (300, 100)), 0, 25)
        button = font.render('OK', False, (255, 255, 255))
        screen.blit(button, (280, 335))

        pygame.display.flip()
        clock.tick(60)

# Function that checks if a piece has moved to a position where another piece is and moves that piece if needed
def Check_Need_To_Change(c1, c2, c3, c4, counter, die):
    global p11
    global p12
    global p21
    global p22

    if counter == 'p11':
        changed = Die_Moving_Action(die) + c1
    elif counter == 'p12':
        changed = Die_Moving_Action(die) + c2
    elif counter == 'p21':
        changed = Die_Moving_Action(die) + c3
    elif counter == 'p22':
        changed = Die_Moving_Action(die) + c4

    if changed != 0 and changed != 4 and changed != 10:
        if counter == 'p11' and changed == c3:
            p21 = 0
        elif counter == 'p11' and changed == c4:
            p22 = 0
        elif counter == 'p12' and changed == c3:
            p21 = 0
        elif counter == 'p12' and changed == c4:
            p22 = 0
        elif counter == 'p21' and changed == c1:
            p11 = 0
        elif counter == 'p21' and changed == c2:
            p12 = 0
        elif counter == 'p22' and changed == c1:
            p11 = 0
        elif counter == 'p22' and changed == c2:
            p12 = 0

# Function to check if a player has won
def Check_Victory():
    global p11, p22, p12, p21
    if p11 == 10 and p12 == 10:
        return player1_name
    elif p21 == 10 and p22 == 10:
        return player2_name
    else:
        return 'no winner'

# Function to switch players
def Switch_Player():
    global current_player, current_player_name
    if current_player == 1:
        current_player = 2
        current_player_name = player2_name
    else:
        current_player = 1
        current_player_name = player1_name

def Play_Game_Local():
    global p11, p12, p21, p22, current_player, current_player_name, screen, screen
    while True:
        if Check_Victory() != 'no winner':
            screen = pygame.display.set_mode((600, 500))
            Victory(current_player_name)
            break

        Switch_Player()

        waste = Game_Window_Draw(p11, p12, p21, p22, current_player_name)

        legal = True
        number = random.sample(range(1, 6), 1)
        number = int(number[0])

        while legal:
            if current_player == 1:
                if Check_Legality(p11, p12, p21, p22, 'p11', number) == 'False':
                    if Check_Legality(p11, p12, p21, p22, 'p12', number) == 'False':
                        screen = pygame.display.set_mode((600, 500))
                        waste = No_Legal_Move()
                        screen = pygame.display.set_mode((1200, 720))
                        break
            elif current_player == 2:
                if Check_Legality(p11, p12, p21, p22, 'p21', number) == 'False':
                    if Check_Legality(p11, p12, p21, p22, 'p22', number) == 'False':
                        break
            global die_to_move
            die_to_move = Game_Playing_Window_Draw(p11, p12, p21, p22, number, current_player, current_player_name)

            if Check_Legality(p11, p12, p21, p22, die_to_move, number) == 'legal':
                legal = False
                Check_Need_To_Change(p11, p12, p21, p22, die_to_move, number)
                add = Die_Moving_Action(number)

                if die_to_move == 'p11':
                    p11 += add
                    if p11 > 10:
                        p11 = 10
                elif die_to_move == 'p12':
                    p12 += add
                    if p12 > 10:
                        p12 = 10
                elif die_to_move == 'p21':
                    p21 += add
                    if p21 > 10:
                        p21 = 10
                elif die_to_move == 'p22':
                    p22 += add
                    if p22 > 10:
                        p22 = 10

            else:
                waste = Game_Illegal_Move(p11, p12, p21, p22, number)

    waste = waste + waste

# Main game loop
def Play_Game_Online(address):
    counter = 0
    global p11, p12, p21, p22, current_player, current_player_name, screen, screen, boardstate
    current_player = 1
    while True:
        counter += 1

        if counter == 1:
            response = createConnection(address)

            if response == 'P2':
                data = client_socket.recv(1024)
                response = data.decode('utf-8')
                current_player = 2
                current_player_name = player2_name
                response1 = []
                temp1 = ''
                for item in response:
                    if item != ',':
                        temp1 += item
                    else:
                        response1.append(temp1)
                        temp1 = ''
                response1.append(temp1)

            if response == 'P1':
                response1 = ['0', '0', '0', '0']

        boardstate = response1
        p11 = int(boardstate[0])
        p12 = int(boardstate[1])
        p21 = int(boardstate[2])
        p22 = int(boardstate[3])

        waste = Game_Window_Draw(p11, p12, p21, p22, current_player_name)

        legal = True

        number = random.sample(range(1, 6), 1)
        number = int(number[0])

        while legal:
            if current_player == 1:
                if Check_Legality(p11, p12, p21, p22, 'p11', number) == 'False':
                    if Check_Legality(p11, p12, p21, p22, 'p12', number) == 'False':
                        screen = pygame.display.set_mode((600, 500))
                        waste = No_Legal_Move()
                        screen = pygame.display.set_mode((1200, 720))
                        break
            elif current_player == 2:
                if Check_Legality(p11, p12, p21, p22, 'p21', number) == 'False':
                     if Check_Legality(p11, p12, p21, p22,'p22', number) == 'False':
                        break
            global die_to_move
            die_to_move = Game_Playing_Window_Draw(p11, p12, p21, p22, number, current_player, current_player_name)

            if Check_Legality(p11, p12, p21, p22, die_to_move, number) == 'legal':
                legal = False
                Check_Need_To_Change(p11, p12, p21, p22, die_to_move, number)
                add = Die_Moving_Action(number)

                if die_to_move == 'p11':
                    p11 += add
                    if p11 > 10:
                        p11 = 10
                elif die_to_move == 'p12':
                    p12 += add
                    if p12 > 10:
                        p12 = 10
                elif die_to_move == 'p21':
                    p21 += add
                    if p21 > 10:
                        p21 = 10
                elif die_to_move == 'p22':
                    p22 += add
                    if p22 > 10:
                        p22 = 10

            else:
                waste = Game_Illegal_Move(p11, p12, p21, p22, number)

        if Check_Victory() != 'no winner':
            screen = pygame.display.set_mode((600, 500))
            message = 'Win'
            client_socket.sendall(str(message).encode('utf-8'))
            Victory(current_player_name)
            break

        message = str(p11) + ',' + str(p12) + ',' + str(p21) + ',' + str(p22)
        client_socket.sendall(str(message).encode('utf-8'))
        data = Waiting_Window_Draw(p11, p12, p21, p22)
        response = data.decode('utf-8')
        if response == 'Win':
            Victory('Your Opponent')
            break
        response1 = []
        temp1 = ''
        for item in response:
            if item != ',':
                temp1 += item
            else:
                response1.append(temp1)
                temp1 = ''
        response1.append(temp1)

    waste = waste + waste

def AI_Logic(current_ai_counter, dieroll):
    global p11,p12,p21,p22
    AIp11 = p11
    AIp12 = p12
    AIp21 = p21
    AIp22 = p22
    Check_Need_To_Change(AIp11,AIp12,AIp21,AIp22,current_ai_counter,dieroll)
    adding = Die_Moving_Action(dieroll)
    if current_ai_counter == 'p21':
        AIp21 += adding
        if AIp21 > 10:
            AIp21 = 10
    elif current_ai_counter == 'p22':
        AIp22 += adding
        if AIp22 > 10:
            AIp22 = 10

    opponentAverage = (AIp11 + AIp12)/2
    AIAverage = (AIp21 + AIp22)/2
    AIDelta = AIAverage - opponentAverage

    return AIDelta

def Play_Game_AI():
    global p11, p12, p21, p22, current_player, current_player_name, screen, screen
    while True:
        if Check_Victory() != 'no winner':
            screen = pygame.display.set_mode((600, 500))
            Victory(current_player_name)
            break

        Switch_Player()

        waste = Game_Window_Draw(p11, p12, p21, p22, current_player_name)

        legal = True
        number = random.sample(range(1, 6), 1)
        number = int(number[0])

        while legal:
            if current_player == 1:
                if Check_Legality(p11, p12, p21, p22, 'p11', number) == 'False':
                    if Check_Legality(p11, p12, p21, p22, 'p12', number) == 'False':
                        screen = pygame.display.set_mode((600, 500))
                        waste = No_Legal_Move()
                        screen = pygame.display.set_mode((1200, 720))
                        break
            elif current_player == 2:
                if Check_Legality(p11, p12, p21, p22, 'p21', number) == 'False':
                     if Check_Legality(p11, p12, p21, p22,'p22', number) == 'False':
                        break
            global die_to_move

            if current_player == 1:
                die_to_move = Game_Playing_Window_Draw(p11, p12, p21, p22, number, current_player, current_player_name)

            else:
                AI_Waiting_Window_Draw(p11,p12,p21,p22)
                if Check_Legality(p11, p12, p21, p22, 'p21', number) == 'False':
                    die_to_move = 'p22'
                elif Check_Legality(p11, p12, p21, p22, 'p22', number) == 'False':
                    die_to_move = 'p21'
                else:
                    if AI_Logic('p21', number) > AI_Logic('p22', number):
                        die_to_move = 'p21'
                    else:
                        die_to_move = 'p22'

            if Check_Legality(p11, p12, p21, p22, die_to_move, number) == 'legal':
                legal = False
                Check_Need_To_Change(p11, p12, p21, p22, die_to_move, number)
                add = Die_Moving_Action(number)

                if die_to_move == 'p11':
                    p11 += add
                    if p11 > 10:
                        p11 = 10
                elif die_to_move == 'p12':
                    p12 += add
                    if p12 > 10:
                        p12 = 10
                elif die_to_move == 'p21':
                    p21 += add
                    if p21 > 10:
                        p21 = 10
                elif die_to_move == 'p22':
                    p22 += add
                    if p22 > 10:
                        p22 = 10

            else:
                waste = Game_Illegal_Move(p11, p12, p21, p22, number)

    waste = waste + waste


# Function to draw main menu
def Menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if 75 <= location[0] <= 552:
                    if 175 <= location[1] <= 275:
                        return 'name'
                    if 280 <= location[1] <= 380:
                        return 'gameLocal'
                    if 385 <= location[1] <= 485:
                        return 'gameOnline'
                    if 490 <= location[1] <= 590:
                        return 'gameAI'
                    if 600 <= location[1] <= 700:
                        quit()

        screen.fill((0, 0, 124))

        text = font.render('Welcome', False, (255, 255, 255))
        screen.blit(text, (225, 100))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 175), (450, 100)), 0, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 280), (450, 100)), 0, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 385), (450, 100)), 0, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 490), (450, 100)), 0, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 505), (450, 100)), 0, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((75, 610), (450, 100)), 0, 10)
        text1 = font.render('Enter Player Names', False, (255, 255, 255))
        text2 = font.render('Play Game Locally', False, (255, 255, 255))
        text3 = font.render('Play Game Online', False, (255, 255, 255))
        text4 = font.render('Play Game vs AI', False, (255, 255, 255))
        text5 = font.render('Quit', False, (255, 255, 255))
        screen.blit(text1, (140, 210))
        screen.blit(text2, (145, 315))
        screen.blit(text3, (150, 420))
        screen.blit(text4, (155, 530))
        screen.blit(text5, (275, 645))
        pygame.display.flip()
        clock.tick(60)

def createConnection(host):
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12347
    client_socket.connect((host, port))
    data = client_socket.recv(1024)
    response = data.decode('utf-8')
    return response


while True:
    screen = pygame.display.set_mode((600, 800))
    buttonClick = Menu()

    if buttonClick == 'name':
        name1, name2 = TKinterGUI.entryGUI()
        if temp != '':
            player1_name = name1
        if temp1 != '':
            player2_name = name2

    elif buttonClick == 'gameLocal':
        screen = pygame.display.set_mode((1200, 720))
        Play_Game_Local()

    elif buttonClick == 'gameOnline':
        #ipaddress = input('')
        ipaddress = TKinterGUI.IPInput()
        screen = pygame.display.set_mode((1200, 720))
        Play_Game_Online(ipaddress)

    elif buttonClick == 'gameAI':
        player2_name = 'AI'
        screen = pygame.display.set_mode((1200, 720))
        Play_Game_AI()