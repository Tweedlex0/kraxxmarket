import sys
import time
import pygame




print("Wait, your game is loading...")
def progress_bar(iteration, total, length=40):
    percent = (iteration / total)
    filled_length = int(length * percent)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2%} Complete')
    sys.stdout.flush()

# Example usage
total_items = 100
for i in range(total_items + 1):
    time.sleep(0.1)  # Simulate some work being done
    progress_bar(i, total_items)

print()  # Move to the next line after completion




import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

# Определение начальных параметров квадрата
square_color = (255, 0, 0)  # Красный цвет
square_size = 50
square_x = 375  # Начальная позиция по оси X
square_y = 275  # Начальная позиция по оси Y
square_speed = 0.6  # Скорость движения квадрата

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Если нажата клавиша "влево"
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:  # Если нажата клавиша "вправо"
        square_x += square_speed
    if keys[pygame.K_UP]:  # Если нажата клавиша "вверх"
        square_y -= square_speed
    if keys[pygame.K_DOWN]:  # Если нажата клавиша "вниз"
        square_y += square_speed

    # Заливка фона
    screen.fill((0, 0, 0))  # Черный цвет

    # Рисуем квадрат
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Обновление экрана
    pygame.display.flip()

