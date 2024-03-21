# Space War -Part 1
# Getting started
# Python 3.7 on Mac

import math
import random
import time
import winsound  # WINDOWS SOUND

"""
Set up the screen de una altre forma

wn = turtle.Screen()
wn.bgcolor("black") 
wn.title("Space Invaders")
"""


# Import the Turtle module
import turtle

# Required by MacOSX to show the window
turtle.fd(0)
# Set the animations speed to the maximum
turtle.speed(0)
# Change the background color
turtle.bgcolor("black")
# Hide the default turtle
turtle.ht()
# This saves memory
turtle.setundobuffer(1)
# This speed up drawing
turtle.tracer(0)  # PODEM FER QUE DIBUIXI MES RÀPID I AIXÏ TREURE EL BUGG; PERO LLAVORS EL JOC VA MASSA RÀPID
# AIXÍ qu el possem = 0 i upgradearem la pantalla manualmente

# number enemies
number_enemies = 10
# number allies
number_allies = 5
# numero misiles para habilidades
number_missils = 4
# numero particulas explosión
number_particles = 20
# distancia explosion partículas en frames
dist_explosion = 7

# radi de colisió
radi_col = 20
# velocidad misil
missile_speed = 10

# Duración Boost
boost_time = 400
# Tiempo de aviso final boost
aviso_time = 40
boost_aviso = boost_time - aviso_time
# Tiempo respawn boost (con probabilidad)
boost_raspawn_time = 500

# Velocidades iniciales jugador, etc etc
player_speed = 4
enemy_speed = 4
ally_speed = 6

# Explosión misil por tiempo
tiempo_explosion = 50

# Add a background
turtle.bgpic("background.gif")

# Change window title
turtle.title("SpaceWar")


# Todos los seres vivos del juego
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        # Defineixo la velocitat de move amb l'speed
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            # Obliguem a que no surti
            self.setx(290)
            # El girem cap a dins
            self.rt(45)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(45)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(45)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(45)

    # Defineixo xoc si els demes estan a un radi de colisió
    def is_collision(self, other):

        if (
            (self.xcor() >= (other.xcor() - radi_col))
            and (self.xcor() <= (other.xcor() + radi_col))
            and (self.ycor() >= (other.ycor() - radi_col))
            and (self.ycor() <= (other.ycor() + radi_col))
        ):
            return True
        else:
            return False


# Subclase de Sprite---->Player
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = player_speed
        self.lives = 3
        self.status = "dead"
        self.special = "none"
        self.shapesize(stretch_wid=0.8, stretch_len=1.1, outline=None)

    # FARE QUE SI SURT DEL MAPA SURTI PER L'ALTRE COSTAT
    def move(self):
        # Defineixo la velocitat de move amb l'speed
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            # Obliguem a que no surti
            self.setx(-290)
        if self.xcor() < -290:
            self.setx(290)
        if self.ycor() > 290:
            self.sety(-290)
        if self.ycor() < -290:
            self.sety(290)

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def respawn(self):
        if self.status == "dead":
            self.status = "alive"


# Subclase de Sprite---->Enemy
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = enemy_speed
        # Le damos una dirección random al aparecer
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = ally_speed
        # Le damos una dirección random al aparecer
        self.setheading(random.randint(0, 360))

    # Farem que rotin cap a l'altre direcció
    def move(self):
        # Defineixo la velocitat de move amb l'speed
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            # Obliguem a que no surti
            self.setx(290)
            # El girem cap a dins
            self.lt(45)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(45)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(45)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(45)


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # Li canvio la forma per fer-la mes peque
        self.shapesize(stretch_wid=0.1, stretch_len=0.5, outline=None)
        self.speed = missile_speed
        self.status = "ready"
        self.time = 0
        # Comença amagat

    # NORMALSHOOT
    def fire(self):
        if player.special != "Berserk":
            # Solo puedo disparar si todos los misiles estan ready
            if (
                (missile[0].status == "ready")
                and (missile[1].status == "ready")
                and (missile[2].status == "ready")
                and (missile[3].status == "ready")
            ):
                winsound.PlaySound("LASER.wav", winsound.SND_ASYNC)  # WINDOWS
                # Porto el missil del 1000,1000 a la posició del jugador
                self.goto(player.xcor(), player.ycor())
                # posso la direcció igual a la del jugador en comptes de la x
                self.setheading(player.heading())
                self.status = "firing"

    # Reescribim el move d'aquests sprite en concret
    def move(self):
        self.time += 1
        if self.time > tiempo_explosion:
            missile[0].status = "ready"
            missile[1].status = "ready"
            missile[2].status = "ready"
            missile[3].status = "ready"

        if (
            (missile[0].status == "ready")
            and (missile[1].status == "ready")
            and (missile[2].status == "ready")
            and (missile[3].status == "ready")
        ):
            self.time = 0
        # Com canvia la velocitat dels disparos depenent de la velocitat player
        speed_sumable = missile_speed + player.speed
        speed_sumable_behind = missile_speed - player.speed
        speed_sumable_diagonal = missile_speed + math.cos(15 / 360 * math.pi) * player.speed

        if self.status == "ready":
            self.goto(-1000, 1000)
            if self == missile[0]:
                self.speed = speed_sumable
            # player_speed=player.speed               ¡¡¡¡¡¡¡MISILE_SPEED(PLAYER_SPEED en el momento del disparo)!!!

        if self.status == "firing":
            self.fd(self.speed)  # quan s'estigui disparant que es mogui ala seva velocitat

        if missile[0].status == "firing":
            if self.status == "ready":
                if self.time < 5:
                    # DIAGONALSHOOT
                    if player.special == "DiagonalShoot":
                        if self == missile[1]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.rt(15)
                            self.status = "firing"
                            self.speed = speed_sumable_diagonal
                        if self == missile[2]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.lt(15)
                            self.status = "firing"
                            self.speed = speed_sumable_diagonal
                    # LATERALSHOOT
                    if player.special == "LateralShoot":
                        if self == missile[1]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.rt(90)
                            self.status = "firing"
                            self.speed = missile_speed  # No afecta velocitat relativa
                        if self == missile[2]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.lt(90)
                            self.status = "firing"
                            self.speed = missile_speed  # No afecta velocitat relativa
                        if self == missile[3]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.rt(180)
                            self.status = "firing"
                            self.speed = speed_sumable_behind
                    # MULTISHOOT
                    if player.special == "MultiShoot":
                        if self == missile[1]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.status = "firing"
                            self.speed = speed_sumable + 2
                        if self == missile[2]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.status = "firing"
                            self.speed = speed_sumable + 4
                        if self == missile[3]:
                            # Porto el missil del 1000,1000 a la posició del jugador
                            self.goto(player.xcor(), player.ycor())
                            # posso la direcció igual a la del jugador en comptes de la x
                            self.setheading(player.heading())
                            self.status = "firing"
                            self.speed = speed_sumable + 6

        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class PowerBoost(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 0
        self.status = "available"

    def collect(self):
        if self.status == "available":
            self.status = "collected"

    def move(self):
        if self.status == "available":
            self.fd(self.speed)

        if (self.status == "collected") or (self.status == "active"):
            self.goto(-1100, 1100)


class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.goto(-1000, -1000)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.frame = 0

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > dist_explosion:
            self.frame = 0
            self.goto(-1000, 1000)

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            # Per si no la vull quadrada,adalt abaix
            if side % 2 == 0:
                self.pen.fd(600)
                self.pen.rt(90)
            # Dreta esquerra
            else:
                self.pen.fd(600)
                self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
        # Per a que el undo no tregui el hide, els segons cops ja treura l'score

    # PUNTUACION, STATUS, ETC
    def show_status(self):
        self.pen.undo()
        msg = "Lives: %s    Score: %s    Boost: %s" % (self.lives, self.score, player.special)
        self.pen.penup()
        # Coordenadaos donde empezará a escribir
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))


# Create game object
game = Game()

# Draw the game border
game.draw_border()


# Create my sprites
player = Player("triangle", "white", -280, 0)

enemy = [0] * number_enemies
for enemy_number in range(number_enemies):
    xcoor = random.randint(-200, 290)  # Evito que apareguin a sobre meu
    ycoor = random.randint(-290, 290)
    enemy[enemy_number] = Enemy("circle", "red", xcoor, ycoor)

ally = [0] * number_allies
for ally_number in range(number_allies):
    xcoor = random.randint(-290, 290)
    ycoor = random.randint(-290, 290)
    ally[ally_number] = Ally("square", "blue", xcoor, ycoor)

missile = [0] * number_missils  # 4 Misiles porque es el maximo que necesito
for missil_number in range(number_missils):
    missile[missil_number] = Missile("triangle", "yellow", -1000, 1000)

xcoor = random.randint(-290, 290)
ycoor = random.randint(-290, 290)
powerboost = PowerBoost("turtle", "green", xcoor, ycoor)

particle = [0] * number_particles
for particle_number in range(number_particles):
    particle[particle_number] = Particle("circle", "orange", 0, 0)

counter = 0

# Show score 0
game.show_status()


# Keyboard bindings    missile[0].fire,missile[1].firediagonalleft,      missile[0].fire,missile[1].firelateralleft,missile[2].firelateralright,
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile[0].fire, "space")
turtle.onkey(player.respawn, "r")
turtle.listen()


# Main game loop
while game.lives >= 0:
    # Change score
    game.show_status()

    # GAME OVER
    while game.lives == 0:
        game.pen.undo()
        msg = "GAME  OVER score: %s" % (game.score)
        game.pen.penup()
        # Coordenadaos donde empezará a escribir
        game.pen.goto(-200, 0)
        game.pen.write(msg, font=("Arial", 30, "normal"))
        player.goto(0, -20)

    # RESPAWN
    while player.status == "dead":
        game.pen.undo()  # Quita el último mensaje, para no acumular
        msg = "Select direction and press R to respawn"
        game.pen.penup()
        # Coordenadaos donde empezará a escribir
        game.pen.goto(-200, 0)
        game.pen.write(msg, font=("Arial", 16, "normal"))

        turtle.update()
        time.sleep(0.03)

        player.goto(-280, 0)

        for enemy_number in range(number_enemies):
            if (
                (enemy[enemy_number].xcor() < -200)
                and (enemy[enemy_number].ycor() < 100)
                and (enemy[enemy_number].ycor() > -100)
            ):
                xcoor = random.randint(-290, 290)
                ycoor = random.randint(-290, 290)
                enemy[enemy_number].goto(xcoor, ycoor)
        # Borro misils del mapa al morir
        for missile_number in range(number_missils):
            missile[missile_number].goto(-1000, 1000)
        player.speed = 6
        if powerboost.status != "available":
            powerboost.status = "available"  # Com vull que estigui el boost al respawnear
            player.special = "None"
            player.color("white")
            player.shape("triangle")
            xcoor = random.randint(-290, 290)
            ycoor = random.randint(-290, 290)
            powerboost.goto(xcoor, ycoor)

    # PLAYING
    if player.status == "alive":
        turtle.update()
        time.sleep(0.03)

        # Velocitat definida a move (que esta definida amb el speed)
        player.move()

        for missil_number in range(number_missils):
            missile[missil_number].move()

        for particle_number in range(number_particles):
            particle[particle_number].move()

        powerboost.move()

        # POWERBOOST
        if powerboost.status == "available":
            if player.is_collision(powerboost):
                powerboost.status = "active"
                winsound.PlaySound("BOOST.wav", winsound.SND_ASYNC)  # WINDOWS

                counter = 0
                n = random.randint(0, 4)
                if n == 0:
                    player.special = "Phantom"
                    player.shape("classic")
                if n == 1:
                    player.special = "DiagonalShoot"
                    player.shape("arrow")
                if n == 2:
                    player.special = "LateralShoot"
                    player.shape("arrow")
                if n == 3:
                    player.special = "MultiShoot"
                    player.shape("arrow")
                if n == 4:
                    player.special = "Berserk"
                    player.color("red")
                    player.shape("classic")

        if powerboost.status == "active":
            counter += 1
            if (counter < boost_time) and (counter > boost_aviso):
                n = random.randint(0, 2)
                if n == 0:
                    player.shape("triangle")
                if n == 1:
                    player.shape("classic")
                if n == 2:
                    player.shape("arrow")

            if counter >= boost_time:
                powerboost.status = "collected"
                winsound.PlaySound("NO_BOOST.wav", winsound.SND_ASYNC)  # WINDOWS

                player.special = "None"
                player.color("white")
                player.shape("triangle")

        if powerboost.status == "collected":
            rand = random.randint(0, boost_raspawn_time)
            if rand == 500:
                powerboost.status = "available"
                xcoor = random.randint(-290, 290)
                ycoor = random.randint(-290, 290)
                powerboost.goto(xcoor, ycoor)
        # ALLIES
        for ally_number in range(number_allies):
            ally[ally_number].move()

            # Si chocan envio els enemics a un altre coordenada
            if player.is_collision(ally[ally_number]):
                if player.special == "Berserk":
                    # Do the explosion
                    for particle_number in range(number_particles):
                        particle[particle_number].explode(ally[ally_number].xcor(), ally[ally_number].ycor())

                    # Respawn ally
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    ally[ally_number].goto(x, y)
                    game.score -= 1
                    winsound.PlaySound("BAD.wav", winsound.SND_ASYNC)  # WINDOWS

            for missil_number in range(number_missils):
                if missile[missil_number].is_collision(ally[ally_number]):
                    if player.special != "Phantom":
                        # Do the explosion
                        for particle_number in range(number_particles):
                            particle[particle_number].explode(ally[ally_number].xcor(), ally[ally_number].ycor())

                        # Respawn ally
                        x = random.randint(-290, 290)
                        y = random.randint(-290, 290)
                        ally[ally_number].goto(x, y)
                        missile[missil_number].status = "ready"
                        game.score -= 1
                        winsound.PlaySound("BAD.wav", winsound.SND_ASYNC)  # WINDOWS

        # ENEMIES
        for enemy_number in range(number_enemies):
            enemy[enemy_number].move()

            # Si chocan envio els enemics a un altre coordenada
            if player.is_collision(enemy[enemy_number]):
                if (player.special != "Phantom") and (player.special != "Berserk"):
                    player.status = "dead"
                    game.lives -= 1
                    if game.lives != 0:
                        winsound.PlaySound("MUERTE.wav", winsound.SND_ASYNC)  # WINDOWS
                    else:
                        winsound.PlaySound("GAME_OVER.wav", winsound.SND_ASYNC)  # WINDOWS

                if player.special == "Berserk":
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    enemy[enemy_number].goto(x, y)
                    game.score += 1
                    # Do the explosion
                    for particle_number in range(number_particles):
                        particle[particle_number].explode(player.xcor(), player.ycor())

                    winsound.PlaySound("GOOD.wav", winsound.SND_ASYNC)  # WINDOWS

            for missil_number in range(number_missils):
                if missile[missil_number].is_collision(enemy[enemy_number]):
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    enemy[enemy_number].goto(x, y)
                    missile[missil_number].status = "ready"
                    game.score += 1
                    # Do the explosion
                    for particle_number in range(number_particles):
                        particle[particle_number].explode(missile[missil_number].xcor(), missile[missil_number].ycor())

                    winsound.PlaySound("GOOD.wav", winsound.SND_ASYNC)  # WINDOWS


delay = input("Press enter to finish. >")
