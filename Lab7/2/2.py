import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

songs = ["/home/phel/Coding/PP2/Lab7/2/Look Your Back!.mp3", "/home/phel/Coding/PP2/Lab7/2/How Soon Is Now.mp3", "/home/phel/Coding/PP2/Lab7/2/Black Hole Sun.mp3"]  
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music_playing = True
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    # screen.blit(background, (0, 0))
    pygame.display.flip()