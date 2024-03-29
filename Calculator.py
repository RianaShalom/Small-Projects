import pygame, collections, time

WHITE = (255, 255, 255)
GREY = (192, 192, 192)
BLACK = (0, 0, 0)
ORANGE = (179, 83, 20)

Button = collections.namedtuple("Button", ["label", "colour", "x", "y", "length", "height"]) # Elements of every button

def make_buttons(): # Nested list with all buttons and values
    length, width = 59, 49
    x1, x2, x3, x4 = 0, 59, 118, 177

    buttons = []

    buttons.append(Button("AC", ORANGE, x1, 139, length, width)) # Top row
    buttons.append(Button("POW", ORANGE, x2, 139, length, width))
    buttons.append(Button("MOD", ORANGE, x3, 139, length, width))
    buttons.append(Button("/", ORANGE, x4, 139, length, width))

    buttons.append(Button("7", GREY, x1, 188, length, width)) # 2nd row
    buttons.append(Button("8", GREY, x2, 188, length, width))
    buttons.append(Button("9", GREY, x3, 188, length, width))
    buttons.append(Button("*", ORANGE, x4, 188, length, width))

    buttons.append(Button("4", GREY, x1, 237, length, width)) # 3rd row
    buttons.append(Button("5", GREY, x2, 237, length, width))
    buttons.append(Button("6", GREY, x3, 237, length, width))
    buttons.append(Button("-", ORANGE, x4, 237, length, width))

    buttons.append(Button("1", GREY, x1, 286, length, width)) # 4th row
    buttons.append(Button("2", GREY, x2, 286, length, width))
    buttons.append(Button("3", GREY, x3, 286, length, width))
    buttons.append(Button("+", ORANGE, x4, 286, length, width))

    buttons.append(Button("0", GREY, x1, 335, length * 2, width)) # 5th row
    buttons.append(Button(".", GREY, x3, 335, length, width))
    buttons.append(Button("=", ORANGE, x4, 335, length, width))

    return buttons

def add_buttons(buttons): # Drawing the buttons
    for button in buttons:
        pygame.draw.rect(screen, button.colour, pygame.Rect(button.x, button.y, button.length, button.height))
        pygame.draw.rect(screen, BLACK, pygame.Rect(button.x, button.y, button.length, button.height), 1)
        font = pygame.font.Font(None, 25)
        functions = font.render(button.label, 1, BLACK)
        screen.blit(functions, (button.x + 10, button.y + 5))

def get_pressed_button(mx, my, buttons): # Checking if the mouse is pressing a button
    for button in buttons:
        if button.x <= mx <= button.x + button.length and button.y <= my <= button.y + button.height:
            return button
    return None

def build_expression(expression, button): # Button logic and calculation
    result = "" if expression == "0" else expression
    if button.label == "AC":
        return "0"
    elif button.label == "POW":
        return "0" if len(result) == 0 else result + "**"
    elif button.label == "MOD":
        return "0" if len(result) == 0 else result + "%"
    elif button.label == "=":
        if len(result) > 0:
            try:
                return str(eval(result))
            except:
                return "Incorrect"
        else:
            return "0"
    elif button.label in ["*", "/"]:
        return "0" if len(result) == 0 else result + button.label
    else:
        return result + button.label

def display_expression(expression): # Text display
    font = pygame.font.Font(None, 40)
    expression = font.render(expression, 9, WHITE)
    txt_length = expression.get_width()
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 234, 60))
    screen.blit(expression, (200 - txt_length , 20))
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    pygame.time.wait(100)
    screen = pygame.display.set_mode((234, 384))
    buttons = make_buttons()
    screen.fill(BLACK)
    add_buttons(buttons)
    expression = "0"
    font = pygame.font.Font(None, 40)
    while True:
        try:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    button = get_pressed_button(mx, my, buttons)
                    expression = build_expression(expression, button)
                    display_expression(expression)
                    if expression == "Incorrect":
                        time.sleep(2)
                        expression = "0"
                        display_expression(expression)
        except:
            exit()