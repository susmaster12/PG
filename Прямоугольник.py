import pygame

def draw(screen):
    screen.fill(pygame.Color("red"), pygame.Rect(1, 1, width -2, height - 2))


if __name__ == '__main__':
    try:
        w, h = map(int, input().split())
        if type(w) != int  or type(h) != int:
            raise Exception
        pygame.init()
        # размеры окна:
        size = width, height = w, h
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption("Прямоугольник")
        draw(screen)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    except Exception:
        print("Неправильный формат ввода")

