import pygame
import random

# Initialisation de pygame
pygame.init()

# Dimensions de l'ecran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balle Rebondsissante")

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def additionner(tik,tak):
    return tik+tak


def soustraire(tak,tik):
    return tak-tik


Gile="("
#On crée une variable zero pour dire 0...

zero=str(int(0))
un=str(int(1))
deux=str(int(2))
trois=str(int(3))
quatre=str(int(4))
cinq=str(int(5))
six=str(int(6))
sept=str(int(7))
huit=str(int(8))
neuf=str(int(9))
dix=str(int(10))

vingt_cinq=str(int(int(dix)+int(neuf)+int(quatre)+int(deux)))#somme des variables précedante pour crée une autre
crochet="[]"
#On appel les différents caractères de  pour crée les autres
crochet_o=crochet[int(zero)]
crochet_f=crochet[int(un)]


exec(alphabet[int(vingt_cinq)-int(deux) + int(trois)-int(deux)-int(un)]+"="+zero) 
print(x)


for i in range(9,9,1):
    print(8)# ne passe pas dans la boucle

# Couleurs
WHITE = (255, 255, 255)
BLACK=(0,0,0)
BLACK =eval(Gile+"0,0,"+un+deux+sept+")")
RED = (255, 0, 0)

# Parametres du jeu
FPS = 60
ball_radius = 15
paddle_width = 100
paddle_height = 15

# Definir les positions initiales de la balle et de la raquette
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([4, -4])
ball_dy = -4

paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - paddle_height - 10

# Score
score = int(zero)

# Police pour le score
font = pygame.font.SysFont(None, 36)

# Fonction pour afficher le score
def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Fonction principale du jeu
def game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, score

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(BLACK)

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controler la raquette avec les touches flechees
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:#eval 
            paddle_x -= 8
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += 8

        # Deplacer la balle
        ball_x += ball_dx
        ball_y += ball_dy

        # Collision avec les bords
        if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
            ball_dx = -ball_dx

        if ball_y - ball_radius < 0:
            ball_dy = -ball_dy

        # Collision avec la raquette
        if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y + ball_radius < paddle_y + paddle_height):
            ball_dy = -ball_dy
            score += 1  # Augmenter le score

        # Si la balle touche le bas de l'e'cran, fin du jeu
        if ball_y + ball_radius > HEIGHT:
            print(f"Game Over! Votre score final est {score}")
            running = False

        # Dessiner la balle
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # Dessiner la raquette
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Afficher le score
        draw_score()

        # Mettre a jour l'ecran
        pygame.display.flip()

        # Controler la vitesse du jeu
        clock.tick(FPS)

    pygame.quit()

# Lancer le jeu

game()