import pygame

def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, "white", (0, 0), (width - 1, height - 1),5)
    pygame.draw.line(screen, "white", (0, height - 1), (width - 1, 0),5)

if __name__ == '__main__':
    w, h = map(int, input().split())
    try:
        if type(w) != int  or type(h) != int:
            raise Exception
        pygame.init()
        # размеры окна:
        size = width, height = w, h
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption("Крест")
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

