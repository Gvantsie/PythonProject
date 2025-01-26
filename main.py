# ბიბლიოთეკის შემოტანა
import pygame
import random

# es aris satesto kodi

# პაგეიმის ინიციალიზაცია
pygame.init()

width = 800
height = 600

# პაიგემის ფანჯრის შექმნა
screen = pygame.display.set_mode((width, height))
#ფანჯრის სახელის გადარქმევა
pygame.display.set_caption('Test Pygame Game!')
#ფანჯრის ლოგოს შეცვლა
icon = pygame.image.load("unnamed.png")
pygame.display.set_icon(icon)

#ფონის ფოტოს შემოტანა
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (width, height))

#ფანჯრის ფონის ფერი
background_color = (52, 195, 235)

#ფერები
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (233, 144, 183)

#მთავარი მოთამაშე
circle_color = WHITE
circle_x = 100
circle_y = 300
circle_radius = 40
speed = 5

#ტყვიის ობიექტი
bullets = []
bullet_speed = 10
bullet_radius = 10

#მტრების კლასი
class Enemy:
    #მტრის ატრიბუტების/მახასიათებლების განსაზღვრა
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        self.x -= self.speed #მტერი მოძრაობს მარჯვნიდან მარცხნივ

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

enemies = []
enemy_timer = 0
ENEMY_SPAWN_RATE = 60

#თამაშის ციკლი
running = True
while running:
    #ივენთები
    for event in pygame.event.get():
        #როდესაც ვაჭერთ X-ს რომ დაიხუროს ფანჯარა
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                circle_color = RED
            if event.key == pygame.K_b:
                circle_color = BLUE
            if event.key == pygame.K_g:
                circle_color = GREEN
            if event.key == pygame.K_p:
                circle_color = PINK

            if event.key == pygame.K_SPACE:
                bullets.append([circle_x + circle_radius, circle_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= speed
    if keys[pygame.K_DOWN]:
        circle_y += speed
    if keys[pygame.K_LEFT]:
        circle_x -= speed
    if keys[pygame.K_RIGHT]:
        circle_x += speed

    for bullet in bullets:
        bullet[0] += bullet_speed

    bullets = [bullet for bullet in bullets if bullet[0] < width]

    circle_x = max(circle_radius, min(width - circle_radius, circle_x))
    circle_y = max(circle_radius, min(height - circle_radius, circle_y))

    #ახალი მტრების გამოჩენა
    enemy_timer += 1
    if enemy_timer >= ENEMY_SPAWN_RATE:
        enemy_y = random.randint(0, height - 40) #y კოორდინატის რენდომად შერჩევა
        new_enemy = Enemy(width, enemy_y, 40, 40, 5)#  ახალი ენემი ობიექტის შექმნა
        enemies.append(new_enemy) #მტრების სიაში ახალი მტრის ჩამატება
        enemy_timer = 0

    for enemy in enemies:
        enemy.move()

    screen.blit(background,(0,0))

    #მოთამაშის გამოჩენა ეკრანზე(შექმნა)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    #ტყვიების გამოჩენა ეკრანზე
    for bullet in bullets:
        pygame.draw.circle(screen, RED, (bullet[0], bullet[1]), bullet_radius)

    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
