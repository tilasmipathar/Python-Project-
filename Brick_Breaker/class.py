import pygame
pygame.init()
pygame.mixer.init()

# screen constants
screensize = (600, 350)

# images
pygame.display.set_caption("Block Breaker")
icon = pygame.image.load('block breaker.png')
pygame.display.set_icon(icon)
background = pygame.image.load("background.jfif")

# colours
BRICK_COLOUR = (255, 94, 94)
PADDLE_COLOUR = (247, 188, 98)
BALL_COLOUR = (249, 60, 22)
TEXT_COLOUR = (255, 255, 255)
LINE_COLOUR = (20, 200, 100)

# paddle constants
paddle_width = 70
paddle_height = 10
paddle_start_x = (screensize[0] / 2) - (paddle_width / 2)
paddle_start_y = screensize[1] - paddle_height - 10

# ball constants
ball_diameter = 10
ball_radius = ball_diameter / 2
ball_start_y = paddle_start_y - 3 * ball_diameter
ball_start_x = (screensize[0] / 2) - ball_radius

# brick constants
brick_height = 11
brick_width = 40

# state constants
GAME_START = 0
PLAYING_GAME = 1
GAME_WIN = 2
GAME_OVER = 3
LEVEL_WIN = 4

# sounds
paddle_sound = pygame.mixer.Sound("paddle.mp3")
brick_sound = pygame.mixer.Sound("brick.mp3")
ball_bounce_sound = pygame.mixer.Sound("bounce.mp3")

# game screen
game_y = 60

class block_breaker():

    def __init__(self):
        # screen
        self.screen = pygame.display.set_mode(screensize)

        # clock
        self.clock = pygame.time.Clock()
        # stats(level,points,lives)
        self.level = 1
        self.points = 0
        self.lives = 3
        # object creation
        self.paddle = pygame.Rect(paddle_start_x, paddle_start_y, paddle_width, paddle_height)
        self.ball = pygame.Rect(ball_start_x, ball_start_y, ball_diameter, ball_diameter)
        self.create_game()

    def create_game(self):
        self.state = GAME_START
        if self.level % 2:
            self.ball_vel = [3, 3]
        else:
            self.ball_vel = [-3, 3]
        if self.level == 1:
           self.create_level1()
        elif self.level == 2:
            self.create_level2()

    def create_level1(self):
        y_coordinate = 25 + game_y
        brick_x_space = 10
        brick_y_space = 10
        self.bricks = []
        for i in range(4):
            x_coordinate = 30
            for j in range(11):
                self.bricks.append(pygame.Rect(x_coordinate, y_coordinate, brick_width,brick_height))
                x_coordinate += brick_width + brick_x_space
            y_coordinate += brick_y_space + brick_height

    def create_level2(self):
        y_coordinate = 25 + game_y
        brick_y_space = 5
        self.bricks = []
        for i in range(7, 0, -1):
            x_coordinate = 35 + (7 - i) * brick_width
            for j in range(i):
                self.bricks.append(pygame.Rect(x_coordinate, y_coordinate, brick_width, brick_height))
                x_coordinate += 2 * brick_width
            y_coordinate += brick_y_space + brick_height

    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, BRICK_COLOUR, brick)

    def check_inputs(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.paddle.left -= 4
            if self.paddle.left <= 0:
                self.paddle.left = 0

        elif key[pygame.K_RIGHT]:
            self.paddle.right += 4
            if self.paddle.right >= screensize[0]:
                self.paddle.right = screensize[0]

        if key[pygame.K_SPACE] and self.state == GAME_START:
            self.state = PLAYING_GAME
            if self.level % 2:
                self.ball_vel = [3, 3]
            else:
                self.ball_vel = [-3, 3]

        elif key[pygame.K_RETURN] and self.state == LEVEL_WIN:
            self.level += 1
            self.lives += 1
            self.create_game()

        elif key[pygame.K_RETURN] and self.state in [GAME_OVER, GAME_WIN]:
            self.game_run = False

    def ball_move(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top -= self.ball_vel[1]

        if self.ball.right >= screensize[0]:
            self.ball.right = screensize[0]
            self.ball_vel[0] = -self.ball_vel[0]
            pygame.mixer.Sound.play(ball_bounce_sound)

        elif self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] = -self.ball_vel[0]
            pygame.mixer.Sound.play(ball_bounce_sound)

        if self.ball.top <= game_y:
            self.ball.top = game_y
            self.ball_vel[1] = -self.ball_vel[1]
            pygame.mixer.Sound.play(ball_bounce_sound)

    def collisions(self):
        if self.ball.colliderect(self.paddle):
            self.ball.top = paddle_start_y - ball_diameter
            self.ball_vel[1] = -self.ball_vel[1]
            pygame.mixer.Sound.play(paddle_sound)

        elif self.ball.bottom >= screensize[1]:
            self.lives -= 1
            if self.lives > 0:
                self.state = GAME_START
            else:
                self.state = GAME_OVER

        for brick in self.bricks:
            if self.ball.colliderect(brick):
                self.points += 1
                if self.ball.centerx > brick.right or self.ball.centerx < brick.left:
                    self.ball_vel[0] = -self.ball_vel[0]
                else:
                    self.ball_vel[1] = -self.ball_vel[1]
                self.bricks.remove(brick)
                pygame.mixer.Sound.play(brick_sound)
                break

        if not len(self.bricks):
            self.state = LEVEL_WIN

    def show_stats(self):
        if pygame.font:
            self.font = pygame.font.Font(None, 40)
        else:
            self.font = None
        if self.font:
            message = "LEVEL: " + str(self.level) + " SCORE: " + str(self.points) + " LIVES: " + str(self.lives)
            font_sentence = self.font.render(message, False, TEXT_COLOUR)
            size = self.font.size(message)
            x = (screensize[0] - size[0]) / 2
            y = 15
            self.screen.blit(font_sentence, (x, y))

    def show_message(self, message):
        if pygame.font:
            self.font = pygame.font.Font(None, 30)
        else:
            self.font = None
        if self.font:
            size = self.font.size(message)
            font_sentence = self.font.render(message, False, TEXT_COLOUR)
            x = (screensize[0] - size[0]) / 2
            y = screensize[1] - size[1] - 70
            self.screen.blit(font_sentence, (x, y))

    def screen_run(self):
        self.game_run = True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run = False
            self.clock.tick(55)
            self.check_inputs()
            self.screen.fill(TEXT_COLOUR)
            self.screen.blit(background, [0, 0])

            if self.state == GAME_START:
                self.show_message("PRESS SPACE TO START")
                self.ball.left = self.paddle.left + self.paddle.width / 2 - ball_radius
                self.ball.top = ball_start_y
            elif self.state == PLAYING_GAME:
                self.ball_move()
                self.collisions()
            elif self.state == LEVEL_WIN and self.level == 2:
                self.show_message("GAME WIN, PRESS ENTER TO EXIT")
                self.state = GAME_WIN
            elif self.state == LEVEL_WIN:
                self.show_message("LEVEL COMPLETE, PRESS ENTER FOR NEXT LEVEL")
            elif self.state == GAME_OVER:
                self.show_message("GAME OVER, PRESS ENTER TO EXIT")

            pygame.draw.rect(self.screen, PADDLE_COLOUR, self.paddle)
            pygame.draw.circle(self.screen, BALL_COLOUR, (self.ball.left + ball_radius, self.ball.top + ball_radius), ball_radius, width = 0)
            self.draw_bricks()
            self.show_stats()
            pygame.draw.line(self.screen, LINE_COLOUR, (0, game_y), (screensize[0], game_y))
            pygame.display.update()

if __name__ == "__main__":
    block_breaker().screen_run()