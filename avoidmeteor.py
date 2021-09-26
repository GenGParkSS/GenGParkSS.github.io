import random
import pygame
import time

####################################################
# 기본 초기화 (필수 요소들)
pygame.init()

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#sound effect
bgm=pygame.mixer.Sound("C:/Users/sungs/OneDrive/바탕 화면/NewProject/bgm.mp3")
bgm.play()
coin=pygame.mixer.Sound("C:/Users/sungs/OneDrive/바탕 화면/NewProject/coin.mp3")
gameover=pygame.mixer.Sound("C:/Users/sungs/OneDrive/바탕 화면/NewProject/gameover.mp3")

#화면 타이틀 설정
pygame.display.set_caption("avoid meteors")

#FPS
clock=pygame.time.Clock()

####################################################

#1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 만들기
background = pygame.image.load("C:/Users/sungs/OneDrive/바탕 화면/NewProject/background.png")

#캐릭터 만들기
character = pygame.image.load("C:/Users/sungs/OneDrive/바탕 화면/NewProject/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width/2) - (character_width/2)
character_ypos = screen_height - (character_height)

#이동 위치
to_x=0
character_speed=10

#똥
poop = pygame.image.load("C:/Users/sungs/OneDrive/바탕 화면/NewProject/meteor.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_xpos = random.randint(0,screen_width - poop_width)
poop_ypos = 0
poop_speed = 10

#점수
score=0

#폰트
game_font = pygame.font.Font(None,40)

#메시지
game_result = "Game Over"

running = True
while running:
    dt = clock.tick(30)
    #2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0

    #3. 게임 캐릭터 위치 정의
    character_xpos += to_x

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width

    poop_ypos += poop_speed

    if poop_ypos > screen_height:
        poop_ypos = 0
        poop_xpos = random.randint(0, screen_width - poop_width)

    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_xpos
    poop_rect.top = poop_ypos
    
    if poop_ypos == 0:
        score+=1
        coin.play()

    if character_rect.colliderect(poop_rect):
        bgm.stop()
        gameover.play()

        running = False

    
    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character, (character_xpos, character_ypos))
    screen.blit(poop, (poop_xpos,poop_ypos))

    a = game_font.render(str(int(score)),True,(255,255,255))
    screen.blit(a, (10,10))
    pygame.display.update()



pygame.time.delay(6000)


pygame.quit()