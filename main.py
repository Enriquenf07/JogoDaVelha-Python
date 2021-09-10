import pygame


TURQUESA = (72, 209, 204)

pygame.init()

LARGURA, ALTURA = 550, 550

win = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('JOGO DA VELHA')

win.fill((32, 178, 170))
firstsquare = pygame.draw.rect(win, TURQUESA, (25, 25, 150, 150))
second = pygame.draw.rect(win, TURQUESA, (190, 25, 150, 150))
third = pygame.draw.rect(win, TURQUESA, (355, 25, 150, 150))
fourth = pygame.draw.rect(win, TURQUESA, (25, 190, 150, 150))
five = pygame.draw.rect(win, TURQUESA, (190, 190, 150, 150))
six = pygame.draw.rect(win, TURQUESA, (355, 190, 150, 150))
seven = pygame.draw.rect(win, TURQUESA, (25, 355, 150, 150))
eight = pygame.draw.rect(win, TURQUESA, (190, 355, 150, 150))
nine = pygame.draw.rect(win, TURQUESA, (355, 355, 150, 150))

FPS = 60
clock = pygame.time.Clock()

run = True
draw_object = 'rect'

first_open = True
second_open = True
third_open = True
fourth_open = True
five_open = True
six_open = True
seven_open = True
eight_open = True
nine_open = True

flag1_1 = False
flag1_2 = False
flag1_3 = False
flag1_4 = False
flag1_5 = False
flag1_6 = False
flag1_7 = False
flag1_8 = False
flag1_9 = False

flag2_1 = False
flag2_2 = False
flag2_3 = False
flag2_4 = False
flag2_5 = False
flag2_6 = False
flag2_7 = False
flag2_8 = False
flag2_9 = False

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_object = 'rect'
                win.fill((32, 178, 170))
                firstsquare = pygame.draw.rect(win, TURQUESA, (25, 25, 150, 150))
                second = pygame.draw.rect(win, TURQUESA, (190, 25, 150, 150))
                third = pygame.draw.rect(win, TURQUESA, (355, 25, 150, 150))
                fourth = pygame.draw.rect(win, TURQUESA, (25, 190, 150, 150))
                five = pygame.draw.rect(win, TURQUESA, (190, 190, 150, 150))
                six = pygame.draw.rect(win, TURQUESA, (355, 190, 150, 150))
                seven = pygame.draw.rect(win, TURQUESA, (25, 355, 150, 150))
                eight = pygame.draw.rect(win, TURQUESA, (190, 355, 150, 150))
                nine = pygame.draw.rect(win, TURQUESA, (355, 355, 150, 150))

                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                five_open = True
                six_open = True
                seven_open = True
                eight_open = True
                nine_open = True

                flag1_1 = False
                flag1_2 = False
                flag1_3 = False
                flag1_4 = False
                flag1_5 = False
                flag1_6 = False
                flag1_7 = False
                flag1_8 = False
                flag1_9 = False

                flag2_1 = False
                flag2_2 = False
                flag2_3 = False
                flag2_4 = False
                flag2_5 = False
                flag2_6 = False
                flag2_7 = False
                flag2_8 = False
                flag2_9 = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if firstsquare.collidepoint(pos) and first_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (50, 50, 100, 100))
                    flag1_1 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (100, 100), 50)
                    flag2_1 = True
                    draw_object = 'rect'
                first_open = False

            if second.collidepoint(pos) and second_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (215, 50, 100, 100))
                    flag1_2 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (265, 100), 50)
                    flag2_2 = True
                    draw_object = 'rect'
                second_open = False
            if third.collidepoint(pos) and third_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (380, 50, 100, 100))
                    flag1_3 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (430, 100), 50)
                    flag2_3 = True
                    draw_object = 'rect'
                third_open = False
            if fourth.collidepoint(pos) and fourth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (50, 215, 100, 100))
                    flag1_4 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (100, 265), 50)
                    flag2_4 = True
                    draw_object = 'rect'
                fourth_open = False
            if five.collidepoint(pos) and five_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (215, 215, 100, 100))
                    flag1_5 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (265, 265), 50)
                    flag2_5 = True
                    draw_object = 'rect'
                five_open = False
            if six.collidepoint(pos) and six_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (380, 215, 100, 100))
                    flag1_6 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (430, 265), 50)
                    flag2_6 = True
                    draw_object = 'rect'
                six_open = False
            if seven.collidepoint(pos) and seven_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (50, 380, 100, 100))
                    flag1_7 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (100, 430), 50)
                    flag2_7 = True
                    draw_object = 'rect'
                seven_open = False
            if eight.collidepoint(pos) and eight_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (215, 380, 100, 100))
                    flag1_8 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (265, 430), 50)
                    flag2_8 = True
                    draw_object = 'rect'
                eight_open = False
            if nine.collidepoint(pos) and nine_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, (112, 128, 144), (380, 380, 100, 100))
                    flag1_9 = True
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, (220, 220, 220), (430, 430), 50)
                    flag2_9 = True
                    draw_object = 'rect'
                nine_open = False

            if flag1_1 and flag1_2 and flag1_3:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_1 and flag1_4 and flag1_7:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_1 and flag1_5 and flag1_9:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_2 and flag1_5 and flag1_8:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_3 and flag1_6 and flag1_9:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_3 and flag1_5 and flag1_7:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_4 and flag1_5 and flag1_6:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag1_7 and flag1_8 and flag1_9:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (220, 200, 100, 100))
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])

            elif flag2_1 and flag2_2 and flag2_3:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_1 and flag2_4 and flag2_7:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_1 and flag2_5 and flag2_9:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_2 and flag2_5 and flag2_8:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_3 and flag2_6 and flag2_9:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_3 and flag2_5 and flag2_7:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_4 and flag2_5 and flag2_6:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif flag2_7 and flag2_8 and flag2_9:
                win.fill((32, 178, 170))
                pygame.draw.circle(win, (220, 220, 220), (270, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('VITORIA', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [205, 325])
            elif not first_open and not second_open and not third_open and not fourth_open and not five_open and not six_open and not seven_open and not eight_open and not nine_open:
                win.fill((32, 178, 170))
                pygame.draw.rect(win, (112, 128, 144), (165, 200, 100, 100))
                pygame.draw.circle(win, (220, 220, 220), (335, 250), 50)
                fonte = pygame.font.Font(None, 48)
                texto1 = fonte.render('EMPATE', True, (0, 0, 0), (32, 178, 170))
                win.blit(texto1, [190, 325])
    pygame.display.update()
pygame.quit()
