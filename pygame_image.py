import sys
import pygame as pg


def main():

    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    rev_bg_img = pg.transform.flip(bg_img, True, False)
    tori_img3 = pg.image.load(f"fig/3.png")
    tori_img3 = pg.transform.flip(tori_img3, True, False)
    tmr = 0
    num = 0
    flag = True
    i = 0

    while True:
        if tmr == 1600:
            i = 1600

        if flag:
            num +=1 
            if tmr%20 == 0:
                flag = False
        else:
            num -=1
            if tmr%20 == 0:
                flag = True

        img_lis = pg.transform.rotozoom(tori_img3, num, 1.0)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if tmr%3200 < 1600:
            screen.blit(bg_img, [-(tmr%1600), 0])
            screen.blit(rev_bg_img, [1600-(tmr%1600), 0])
        else:
            screen.blit(bg_img, [1600-(tmr%1600), 0])
            screen.blit(rev_bg_img, [-(tmr%1600), 0])
        
        
        screen.blit(img_lis, [300, 200+num])
        pg.display.update()
        tmr += 1    
        clock.tick(300)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()