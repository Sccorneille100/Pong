import pygame
from modules.constants import WIDTH, HEIGHT, WHITE, BLACK, GREEN , FPS
from modules.ball import Ball
from modules.player import Player

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_Game")


clock = pygame.time.Clock()


def main():
	running = True

	# Defining the objects
	player_1 = Player(20, 0, 10, 100, 10, GREEN)
	player_2 = Player(WIDTH-30, 0, 10, 100, 10, GREEN)
	ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

	listOfGeeks = [player_1, player_2]

	# Initial parameters of the players
	player_1Score, player_2Score = 0, 0
	player_1YFac, player_2YFac = 0, 0

	while running:
		screen.fill(BLACK)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player_2YFac = -1
				if event.key == pygame.K_DOWN:
					player_2YFac = 1
				if event.key == pygame.K_w:
					player_1YFac = -1
				if event.key == pygame.K_s:
					player_1YFac = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					player_2YFac = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					player_1YFac = 0

		# Collision detection
		for geek in listOfGeeks:
			if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
				ball.hit()

		# Updating the objects
		player_1.update(player_1YFac)
		player_2.update(player_2YFac)
		point = ball.update()

		# -1 -> Geek_1 has scored
		# +1 -> Geek_2 has scored
		# 0 -> None of them scored
		if point == -1:
			player_1Score += 1
		elif point == 1:
			player_2Score += 1

		if point: # Someone has scored a point and the
		# ball is out of bounds. So, we reset it's position
			ball.reset()

		# Displaying the objects on the screen
		player_1.display()
		player_2.display()
		ball.display()

		# Displaying the scores of the players
		player_1.displayScore("Guest_One : ", player_1Score, 100, 20, WHITE)
		player_2.displayScore("Guest_Two : ", player_2Score, WIDTH-100, 20, WHITE)

		pygame.display.update()
		# Adjusting the frame rate
		clock.tick(FPS)
		

if __name__ == "__main__":
	main()
	pygame.quit()

