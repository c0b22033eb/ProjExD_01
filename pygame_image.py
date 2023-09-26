import sys
import pygame as pg


def main():

    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tori_img3 = pg.image.load("fig/3.png")
    tori_img3 = pg.transform.flip(tori_img3, True, False)
    img_lis = [tori_img3, pg.transform.rotozoom(tori_img3, 10, 1.0)]
    tmr = 0
    num = 0

    while True:
        if num >= 1600:
            num = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr%2 == 0:
            img_rct = img_lis[0].get_rect()
            img_rct.center = num, 200
            screen.blit(img_lis[0], img_rct)
        else:
            img_rct = img_lis[1].get_rect()
            img_rct.center = num, 200
            screen.blit(img_lis[1], img_rct)
        pg.display.update()
        tmr += 1 
        num += 1       
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()