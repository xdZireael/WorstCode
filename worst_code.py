import pygame
import random
import time as horloge
import math as alpha_B

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

Gile="("
Gille=")"
Virgule=","


vingt_cinq=str(int(int(dix)+int(neuf)+int(quatre)+int(deux)))#somme des variables précedante pour crée une autre
crochet="[]"
#On appel les différents caractères de  pour crée les autres
crochet_o=crochet[int(zero)]
crochet_f=crochet[int(un)]


# Initialisation de pygame
pygame.init()

# Dimensions de l'ecran
WIDTH, HEIGHT = int(eval(huit+zero+zero)), int(eval(six+zero+zero))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balle Rebondsissante")

alphabet=eval(crochet_o+'"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"'+crochet_f)

def renvoie_deux_au_fait_c_est_un_str():
    
    return eval(eval("alphabet"+crochet_o+str(int(un)+int(un)+int(un))+crochet_f)+eval("alphabet"+crochet_o+quatre+crochet_f)+"ux")


def additionner(tik,tak):
    return tik+tak
def soustraire(tak,tik):
    return tak-tik

# Couleurs
WHITE=eval(Gile+deux+cinq+cinq+Virgule+deux+cinq+cinq+Virgule+deux+cinq+cinq+Gille)
BLACK=eval(Gile+zero+Virgule+zero+Virgule+un+deux+sept+Gille)
RED=eval(Gile+vingt_cinq+cinq+Virgule+zero+Virgule+zero+Gille)



# Parametres du jeu
FPS = eval(six+zero)
ball_radius = soustraire(int(vingt_cinq),int(dix))
paddle_width = int(eval(un+zero+zero))
paddle_height = eval(eval(eval("alphabet"+crochet_o+(str(int(dix)+int(dix)))+crochet_f)+eval("alphabet"+crochet_o+(str(int(dix)+int(trois)))+crochet_f))+"+"+cinq)#Pour faire 15
# Definir les positions initiales de la balle et de la raquette
ball_x = WIDTH // int(renvoie_deux_au_fait_c_est_un_str())
ball_y = HEIGHT // int(renvoie_deux_au_fait_c_est_un_str())
ball_dx = random.choice([additionner(int(renvoie_deux_au_fait_c_est_un_str()),int(renvoie_deux_au_fait_c_est_un_str())), additionner(soustraire(int(deux),int(trois)),soustraire(int(quatre),int(cinq)))])
ball_dy = (alpha_B.sqrt((soustraire(int(zero),int(quatre))**2)))*(-int(un))

paddle_x = WIDTH // (int(alpha_B.pi)-int(un)) - paddle_width // ((int(alpha_B.pi)+int(un))/int(renvoie_deux_au_fait_c_est_un_str()))
paddle_y = HEIGHT - paddle_height - 10 #Petite pause

# Score

score = int(un)
score = 0

# Police pour le score
font = pygame.font.SysFont(None, eval(trois+six))

# Fonction pour afficher le score
def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (int(dix), int(dix)))

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
        if keys[pygame.K_LEFT] and paddle_x > int(zero):#eval 
            paddle_x -= int(quatre)*int(renvoie_deux_au_fait_c_est_un_str())
        if keys[pygame.K_RIGHT] and paddle_x < soustraire(WIDTH,paddle_width):
            paddle_x = additionner(int(quatre)*int(renvoie_deux_au_fait_c_est_un_str()),paddle_x)

        # Deplacer la balle
        ball_x = additionner(ball_dx,ball_x)
        ball_y = additionner(ball_dy,ball_y)

        # Collision avec les bords
        if soustraire(ball_x , ball_radius) < int(zero) or additionner(ball_x , ball_radius) > WIDTH:
            ball_dx = soustraire(int(zero),ball_dx)

        if soustraire(ball_y , ball_radius) < soustraire(int(renvoie_deux_au_fait_c_est_un_str()),int(renvoie_deux_au_fait_c_est_un_str())):
            ball_dy = soustraire(0,ball_dy)

        # Collision avec la raquette
        if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y + ball_radius < paddle_y + paddle_height):
            ball_dy = -ball_dy
            score += 1  # Augmenter le score

        # Si la balle touche le bas de l'ecran, fin du jeu
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