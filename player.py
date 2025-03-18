
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    @override
    def update(self, dt: float) -> None:
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.rotate(dt)

        if keys[pygame.K_j]:
            self.rotate(-dt)

        if keys[pygame.K_i]:
            self.move(dt)

        if keys[pygame.K_k]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position: pygame.Vector2 = self.position + forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return None

        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
