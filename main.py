import pygame as pg

pg.init()

WIDTH = 360
HEIGHT = 480
game_screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("Test drawings")
game_screen.fill((109, 130, 156))
#icon_my_game = pg.image.load('worm.png')
pg.display.set_icon(icon_my_game)
pg.display.flip()
#my_font = pg.font.Font('Roboto_Slab.zip', 18)
#text = my_font.render('хорошего дня' , (True)  , (245,144,201))
#game_screen.blit(text , (20,69))

#цикл
run_game = True
while run_game:
    pg.draw.rect(game_screen,(56, 32, 27) , (90,300,200,500), 0)
    pg.draw.polygon(game_screen, (56, 32, 27) , [[80, 300], [190, 200], [300, 300]], 0)
    pg.draw.rect(game_screen, (237, 227, 138), (110, 320, 160, 130), 0)
    pg.draw.line(game_screen, (56, 32, 27), [190,300], [190,900], 10)
    pg.draw.ellipse(game_screen,(247, 221, 87), (20,20,75,75) , 0)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_game = False
# Выход из игры:
pg.quit()
