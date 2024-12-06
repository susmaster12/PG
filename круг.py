import pygame


c = ["red", "blue", "green"]
def draw(screen, w, n):
    for i in range(n):
        pygame.draw.circle(screen, c[i % 3], size / 2, w * (n - 1))



if __name__ == '__main__':
    try:
        w, n = map(int, input().split())
        if type(w) != int or type(n) != int:
            raise Exception
        pygame.init()
        # размеры окна:
        size = width, height = w * n * 2, w * n * 2
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        pygame.display.set_caption("Круг")
        draw(screen, w, n)
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    except Exception:
        print("Неправильный формат ввода")