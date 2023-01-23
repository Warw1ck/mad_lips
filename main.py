import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode([600, 500])


base_font = pygame.font.Font(None, 32)
user_text = ''
gramatic = ''
text_list = []

input_rect = pygame.Rect(250, 100, 50, 32)


color_active = pygame.Color(0, 159, 183)


color_passive = pygame.Color((254, 74, 73))
color = color_passive

active = False
game = True
final = ''


def final_print(final_text):

    final_sentence = base_font.render(final_text, True, (254, 215, 102))
    screen.blit(final_sentence, (20, 200))


def gram():

    number = random.randint(1, 4)
    if number == 1:
        gramatic_word = 'Adjective'
    elif number == 2:
        gramatic_word = 'Verb'
    elif number == 3:
        gramatic_word = 'Noun'
    elif number == 4:
        gramatic_word = 'Plural Noun'
    return number, gramatic_word


def text(word, number):

    if number == 1:
        sentence = f'Flip_flops are a staple of any {word} summer wardrobe.'
    elif number == 2:
        sentence = f'i like my donuts with {word} on them.'
    elif number == 3:
        sentence = f'What came the first, the chicken or the {word}?'
    elif number == 4:
        sentence = f'April showers brings May {word}.'
    return sentence


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game = True
            if input_rect.collidepoint(event.pos):
                active = True
                random_num, gramatic = gram()
            else:
                active = False

        if event.type == pygame.KEYDOWN and active:

            if event.key == pygame.K_BACKSPACE:

                user_text = user_text[:-1]

            else:
                user_text += event.unicode

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_UP:
                text_list.append(user_text)
                final = text(user_text, random_num)
                game = False

    screen.fill((230, 230, 234))
    if game:
        if active:
            color = color_active
            N = base_font.render(f'{gramatic}:', True, (0, 0, 0))
            screen.blit(N, (120, 100))
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (254, 215, 102))

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)
    else:
        screen.fill((0, 159, 183))
        final_print(final)
        active = False
        user_text = ''

    pygame.display.update()
    clock.tick(60)
