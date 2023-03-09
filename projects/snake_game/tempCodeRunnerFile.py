        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w") and direction != "DOWN"):
                direction = "UP"