import pygame


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 501, 501
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Прямоугольники с Ctrl+Z')

    running = True
    flag = True
    rects = []
    pygame.draw.rect(screen, 'white', [143, 70, 0, 0], 0)
    while running:

        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                rects.append([event.pos[0], event.pos[1], event.pos[0], event.pos[1]])
            if event.type == pygame.MOUSEBUTTONUP:
                flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    if rects:
                        del rects[-1]
                        screen.fill('black')
                        for i in rects:
                            pygame.draw.rect(screen, 'white', i, 4)

        if pygame.mouse.get_pressed()[0]:
            screen.fill('black')
            rects[-1][-2] = pygame.mouse.get_pos()[0] - rects[-1][0]
            rects[-1][-1] = pygame.mouse.get_pos()[1] - rects[-1][1]
            for i in rects:
                pygame.draw.rect(screen, 'white', i, 4)
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
