import pygame
import os

pygame.init()

#============Constants===========#
width, height = 900, 600
board_width, board_height = 600, 600
fps = 60
montserrat = "fonts/Montserrat/Montserrat-Bold.ttf"
font1 = pygame.font.Font(montserrat, 26)
font2 = pygame.font.Font(montserrat, 40)
font3 = pygame.font.Font(montserrat, 50)


#==========colors==================#
class colors:
    black = (0,0,0)
    white = (255,255,255)
    grey = (50,50,50)
    light_grey = (150,150,150)
    blue = (0, 158, 248)
    red = (255,0,0)
    purple = (130,10,130)


#Setting up the screen
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("chess")

#===========Position arrays========#
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []


#=============Assets=============#
class assets:
    background = pygame.image.load(os.path.join("chess assets", "chess_board.png"))
    background = pygame.transform.scale(background, (board_width, board_height))

    move_sound = pygame.mixer.Sound("chess assets/move.wav")
    capture_sound = pygame.mixer.Sound("chess assets/capture.wav")
    check_sound = pygame.mixer.Sound("chess assets/check.wav")
    castle_sound = pygame.mixer.Sound("chess assets/castle.wav")
    mate_sound = pygame.mixer.Sound("chess assets/mate.wav")
    promotion_sound = pygame.mixer.Sound("chess assets/promote.wav")

    w_king = pygame.image.load(os.path.join("chess assets", "w_king.png"))
    w_king = pygame.transform.scale(w_king, (board_width/8, board_height/8))
    b_king = pygame.image.load(os.path.join("chess assets", "b_king.png"))
    b_king = pygame.transform.scale(b_king, (board_width/8, board_height/8))
    w_queen = pygame.image.load(os.path.join("chess assets", "w_queen.png"))
    w_queen = pygame.transform.scale(w_queen, (board_width/8, board_height/8))
    b_queen = pygame.image.load(os.path.join("chess assets", "b_queen.png"))
    b_queen = pygame.transform.scale(b_queen, (board_width/8, board_height/8))
    w_rook = pygame.image.load(os.path.join("chess assets", "w_rook.png"))
    w_rook = pygame.transform.scale(w_rook, (board_width/8, board_height/8))
    b_rook = pygame.image.load(os.path.join("chess assets", "b_rook.png"))
    b_rook = pygame.transform.scale(b_rook, (board_width/8, board_height/8))
    w_bishop = pygame.image.load(os.path.join("chess assets", "w_bishop.png"))
    w_bishop = pygame.transform.scale(w_bishop, (board_width/8, board_height/8))
    b_bishop = pygame.image.load(os.path.join("chess assets", "b_bishop.png"))
    b_bishop = pygame.transform.scale(b_bishop, (board_width/8, board_height/8))
    w_knight = pygame.image.load(os.path.join("chess assets", "w_knight.png"))
    w_knight = pygame.transform.scale(w_knight, (board_width/8, board_height/8))
    b_knight = pygame.image.load(os.path.join("chess assets", "b_knight.png"))
    b_knight = pygame.transform.scale(b_knight, (board_width/8, board_height/8))
    w_pawn = pygame.image.load(os.path.join("chess assets", "w_pawn.png"))
    w_pawn = pygame.transform.scale(w_pawn, (board_width/8, board_height/8))
    b_pawn = pygame.image.load(os.path.join("chess assets", "b_pawn.png"))
    b_pawn = pygame.transform.scale(b_pawn, (board_width/8, board_height/8))

white_images = [assets.w_pawn, assets.w_queen, assets.w_king, assets.w_knight, assets.w_rook, assets.w_bishop]
black_images = [assets.b_pawn, assets.b_queen, assets.b_king, assets.b_knight, assets.b_rook, assets.b_bishop]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop'] #To link the images with the black_pieces and white_pieces


def draw_board():
    screen.fill(colors.grey)
    screen.blit(assets.background, (0,0))

def draw_pieces(turn_step, selection):
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * 75, white_locations[i][1] * 75))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, colors.red, [white_locations[i][0] * 75, white_locations[i][1] * 75,
                                                 75, 75], 3)


    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * 75, black_locations[i][1] * 75))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, colors.red, [black_locations[i][0] * 75, black_locations[i][1] * 75, 75, 75], 3)


def move_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = moves_pawn(location, turn)
        elif piece == 'rook':
            moves_list = moves_rook(location, turn)
        elif piece == 'knight':
            moves_list = moves_knight(location, turn)
        elif piece == 'bishop':
            moves_list = moves_bishop(location, turn)
        elif piece == 'queen':
            moves_list = moves_queen(location, turn)
        elif piece == 'king':
            moves_list = moves_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


#Pawn Movement
def moves_pawn(position, color):
    moves_list = []
    if color == 'white':
        #Move 1 square
        if (position[0], position[1] - 1) not in black_locations and \
                (position[0], position[1] - 1) not in white_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        #Move 2 squares
        if (position[0], position[1] - 2) not in black_locations and \
                (position[0], position[1] - 2) not in white_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        #Capture a piece to the right
        if (position[0] + 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        #Capture a piece to the left
        if (position[0] - 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] - 1))

    else:
        #Move 1 square
        if (position[0], position[1] + 1) not in black_locations and \
                (position[0], position[1] + 1) not in white_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        #Move 2 squares
        if (position[0], position[1] + 2) not in black_locations and \
                (position[0], position[1] + 2) not in white_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        #Capture a piece to the right
        if (position[0] + 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        #Capture a piece to the left
        if (position[0] - 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    return moves_list

#Rook Movement
def moves_rook(position, color): 
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    direction_of_movement = [(0, 1), (0, -1), (1, 0), (-1, 0)] #right, left, down, up

    for i in range(len(direction_of_movement)): 
        path = True
        chain = 1

        x, y = direction_of_movement[i]

        while path:
            nextChainSpace = (position[0] + (chain * x), position[1] + (chain * y)) #the next space in the line of the rooks movement
            if nextChainSpace not in friends_list:
                if 0 <= nextChainSpace[0] <= 7 and 0 <= nextChainSpace[1] <= 7:
                    moves_list.append(nextChainSpace)
                    if nextChainSpace in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
            else:
                path = False
    return moves_list

#Kight Movement
def moves_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations

    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

#Bishop Movement
def moves_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    direction_of_movement = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  #down-right, down-left, up-right, down-left

    for i in range(len(direction_of_movement)): 
        path = True
        chain = 1

        x, y = direction_of_movement[i]

        while path:
            nextChainSpace = (position[0] + (chain * x), position[1] + (chain * y))
            if nextChainSpace not in friends_list:
                if 0 <= nextChainSpace[0] <= 7 and 0 <= nextChainSpace[1] <= 7:
                    moves_list.append(nextChainSpace)
                    if nextChainSpace in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
            else:
                path = False
    return moves_list

#Queen Movement
def moves_queen(position, color):
    moves_list = moves_bishop(position, color)
    second_list = moves_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

#King Movement
def moves_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


#Checking the valid moves for a selected piece
def check_valid_moves(black_options, white_options, turn_step, selection):
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

#Displaying the valid moves for the selected piece
def draw_valid(moves):
    for i in range(len(moves)):
        pygame.draw.circle(screen, colors.red, (moves[i][0] * 75 + 37, moves[i][1] * 75 + 37), 5)

#Check if the king is being attacked
def check(black_options, white_options, turn_step, w_check, b_check):
    #if black moved a piece
    if turn_step == 3:
        if 'king' in white_pieces:   
            king_index = white_pieces.index('king')    
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    assets.check_sound.play()
                    w_check = True
                else:
                    w_check = False
            print(w_check)
                    
    #if white moved a piece
    elif turn_step == 1:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    assets.check_sound.play()
                    b_check = True
                else:
                    b_check = False

    return w_check, b_check
                        
def draw_check(black_options, white_options, turn_step, counter):
    #if white's turn
    if turn_step < 2:
        if 'king' in white_pieces:   
            king_index = white_pieces.index('king')    
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < fps/2:
                        pygame.draw.rect(screen, colors.purple, [white_locations[king_index][0] * 75,
                                                        white_locations[king_index][1] * 75, 75, 75], 4)                    
                    
    #if black's turn
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < fps/2:
                        pygame.draw.rect(screen, colors.purple, [black_locations[king_index][0] * 75,
                                                        black_locations[king_index][1] * 75, 75, 75], 4)


def main():
    clock = pygame.time.Clock()
    running = True
    black_options = move_options(black_pieces, black_locations, 'black')
    white_options = move_options(white_pieces, white_locations, 'white')

    #=====Game Variables=====#
    #0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
    turn_step = 0
    #Stores the index of the piece selected from black_pieces or white_pieces
    #A large value for when no piece is selected. 
    selection = 100     
    #stores the valid moves for a selected piece
    valid_moves = []
    #Check if a piece is captured
    piece_captured = False

    # check variables/ flashing counter
    counter = 0
    winner = ''
    w_check = False
    b_check = False
    game_over = False
    

    while running:
        clock.tick(fps)
        draw_board()
        draw_pieces(turn_step, selection)
        if selection != 100:        #Displays the valid moves for the selected piece
            valid_moves = check_valid_moves(black_options, white_options, turn_step, selection)
            draw_valid(valid_moves)

        #Display check
        if counter < fps:
            counter += 1
        else:
            counter = 0
        draw_check(black_options, white_options, turn_step, counter)
        pygame.display.flip()


        #changes the cursor when the cursor is within the button
        mouse_pos = pygame.mouse.get_pos()
        mouse_coords = (mouse_pos[0] // 75, mouse_pos[1] // 75)
        if mouse_coords in white_locations or mouse_coords in black_locations:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0] // 75
                y_coord = event.pos[1] // 75
                click_coords = (x_coord, y_coord)
                
                if turn_step <= 1:
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1  #Piece selected

                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            piece_captured = True
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_black.append(black_pieces[black_piece])

                            if black_pieces[black_piece] == 'king':
                                winner = 'white'    
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)                  

                        black_options = move_options(black_pieces, black_locations, 'black')
                        white_options = move_options(white_pieces, white_locations, 'white')
                        w_check, b_check = check(black_options, white_options, turn_step, w_check, b_check)
                        if piece_captured == True and b_check == False:
                            assets.capture_sound.play()    #Play capture sound if a black piece is captured and black is not in check   
                        elif piece_captured == False and b_check == False:
                            assets.move_sound.play()    #Play move sound if a piece is moved and the black king is not in check

                        #Reset the variables
                        piece_captured = False
                        turn_step = 2
                        selection = 100
                        valid_moves = []


                if turn_step > 1:
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3   #Piece selected

                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            piece_captured = True
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_white.append(white_pieces[white_piece])
                            
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)                            

                        black_options = move_options(black_pieces, black_locations, 'black')
                        white_options = move_options(white_pieces, white_locations, 'white')
                        w_check, b_check = check(black_options, white_options, turn_step, w_check, b_check)
                        if piece_captured == True and w_check == False:
                            assets.capture_sound.play()     #Play capture sound if a white piece is captured and white is not in check  
                        elif piece_captured == False and w_check == False:
                            assets.move_sound.play()    #Play move sound if a piece is moved and white  is not in check

                        #Reset the variables
                        piece_captured = False
                        turn_step = 0
                        selection = 100
                        valid_moves = []

                if winner != '':
                    print(winner)



