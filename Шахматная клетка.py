import pygame

def draw(screen, a, n):
    d = a / n
    for i in range(n):
        for g in range(n):
            if (i + g) % 2 != 0:
                pygame.draw.rect(screen, "white", (i * d, g * d, d, d))


if __name__ == '__main__':
    try:
        a, n = map(int, input().split())
        if (type(a) != int  or type(n) != int) or a % n != 0:
            raise Exception
        pygame.init()
        # размеры окна:
        size = width, height = a, a
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption("Прямоугольник")
        draw(screen, a, n)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    except Exception:
        print("Неправильный формат ввода")
