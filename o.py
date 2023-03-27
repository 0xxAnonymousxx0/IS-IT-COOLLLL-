import pygame
import random
import os



pygame.init()
pygame.mixer.init()



# game interface/window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
img = pygame.image.load('zoolander.jpg')
bgimg = pygame.image.load('ohio.png').convert_alpha()




#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)



# captions/text
pygame.display.set_caption("UwU with snakes")
pygame.display.update()
clock = pygame.time.Clock()
Font = pygame.font.SysFont(None, 35)
Fonte = pygame.font.SysFont(None, 25)
exit_game = False
game_over = False
fps = 60




def text_screen(text,color, x,y ):
    screen_text = Font.render(text,False,color)
    gameWindow.blit(screen_text,[x,y])

def text_screen_(text,color, x,y ):
    screen_text0 = Fonte.render(text,False,color)
    gameWindow.blit(screen_text0,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def tuts():
    exit_game = False
    pygame.mixer.music.load('m.mp3')
    pygame.mixer.music.play(100)
    while not exit_game:
        gameWindow.fill(black)
        text_screen('do not collide by yourself or go out of gamezone',white,150,290)
        text_screen_("IF YOU HAVE ANY PROBLEM WITH THE MUSIC,MUTE OR ADJUST YOUR VOLUME BY YOURSELF", white, 30, 400)
        text_screen("press up/down/left/right arrow key to go up/down/left/right respectively", white, 30, 350)
        text_screen("<press space to skip>", white, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    welcome()


        pygame.display.update()
        clock.tick(fps)
def welcome():
    exit_game = False
    pygame.mixer.music.load('m.mp3')
    pygame.mixer.music.play(100)
    while not exit_game:
        gameWindow.fill(black)
        text_screen('welcome to ohio',white,290,290)
        text_screen("(Press Space Bar To Play)", white, 250, 350)
        text_screen_("IF YOU HAVE ANY PROBLEM WITH THE MUSIC ,MUTE OR ADJUST YOUR VOLUME BY YOURSELF", white, 30, 400)
        text_screen("<presented by timmy the neurosergeun at the age of 9>", white, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(fps)
def music():
    pygame.mixer.music.load('o.mp3')
    pygame.mixer.music.stop()
    pygame.mixer.music.load('m.mp3')
    pygame.mixer.music.stop()


def musicn():
    pygame.mixer.music.load('o.mp3')
    pygame.mixer.music.play(100)
    pygame.mixer.music.load('m.mp3')
    pygame.mixer.music.play(100)
def music():
        pygame.mixer.music.load('o.mp3')
        pygame.mixer.music.stop()
        pygame.mixer.music.load('m.mp3')
        pygame.mixer.music.stop()


def gameloop():
    pygame.mixer.music.load('o.mp3')
    pygame.mixer.music.play(100)

    if(not os.path.exists("highscore.txt") ):
        with open ('highscore.txt','w')as f:
            f.write('0')

    with open('highscore.txt', 'r') as f:
        highscore = f.read()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    snk_list = []
    snk_length = 1

    food_x = random.randint(0,screen_width/1.5)
    food_y = random.randint(0,screen_height/1.5)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    pygame.mixer.music.load('o.mp3')
    pygame.mixer.music.play(100)



    while not exit_game:
        if game_over == True:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            text_screen(" YOU GOT FUCKED UP!!!! PRESS ENTER TO CONTINUE OR ESC TO EXIT", red,10,400 )
            text_screen_(" IF YOU HAVE ANY PROBLEM WITH THE MUSIC ,MUTE OR ADJUST YOUR VOLUME BY YOURSELF", red, 30, 450)
            text_screen("sigma score = "+ str(score) +"High score:"+str(highscore),yellow,5,0)
            text_screen("<timmy's score was infinte raised to the power infinite>", red, 10, 505)
            text_screen("<stupid!!!!....>", red, 10, 565)
            gameWindow.blit(img, (30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                            exit()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_LEFT:
                     velocity_x = - init_velocity
                     velocity_y = 0



                    if event.key == pygame.K_UP:
                        velocity_y =  - init_velocity
                        velocity_x = 0


                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y



            if abs(snake_x - food_x ) <18 and abs (snake_y - food_y)<18:

                score  += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)

                snk_length += 5
            if score > int(highscore):
                highscore = score
                pygame.mixer.music.load('b.mp3')
                pygame.mixer.music.play()





            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("sigma score = "+ str(score)+"High score:"+str(highscore),yellow,5,5)

            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]


            if snake_x <0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True


            plot_snake(gameWindow, grey, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

tuts()


