import pygame
import math

# Initialize Pygame
pygame.init()

# Screen Setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors (N64-esque Palette)
black = (0, 0, 0)
gray = (128, 128, 128)

# 3D Point Class
class Point3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def rotateX(self, angle):
        radians = math.radians(angle)
        cos_x = math.cos(radians)
        sin_x = math.sin(radians)
        y = self.y * cos_x - self.z * sin_x
        z = self.y * sin_x + self.z * cos_x
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        radians = math.radians(angle)
        cos_y = math.cos(radians)
        sin_y = math.sin(radians)
        x = self.x * cos_y + self.z * sin_y
        z = -self.x * sin_y + self.z * cos_y
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        radians = math.radians(angle)
        cos_z = math.cos(radians)
        sin_z = math.sin(radians)
        x = self.x * cos_z - self.y * sin_z
        y = self.x * sin_z + self.y * cos_z
        return Point3D(x, y, self.z)

    def project(self):
        factor = 200 / (self.z + 10)
        x = self.x * factor + width / 2
        y = -self.y * factor + height / 2
        return Point3D(x, y, self.z)

# Cube (collection of points)
points = [
    Point3D(-1, 1, -1),
    Point3D(1, 1, -1),
    Point3D(1, -1, -1),
    Point3D(-1, -1, -1),
    Point3D(-1, 1, 1),
    Point3D(1, 1, 1),
    Point3D(1, -1, 1),
    Point3D(-1, -1, 1)
]

# Lines connecting the points
lines = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Rotation angles
angle_x, angle_y, angle_z = 0, 0, 0

# Clock for FPS control
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation angles
    angle_x += 0.01
    angle_y += 0.02
    angle_z += 0.03

    # Clear screen
    screen.fill(black)

    # Rotate and project points
    rotated_points = []
    for point in points:
        rotated = point.rotateX(angle_x).rotateY(angle_y).rotateZ(angle_z)
        projected = rotated.project()
        rotated_points.append(projected)

    # Draw lines
    for line in lines:
        pygame.draw.line(screen, gray, (rotated_points[line[0]].x, rotated_points[line[0]].y),
                         (rotated_points[line[1]].x, rotated_points[line[1]].y), 3)

    # Update display
    pygame.display.flip()

pygame.quit()
# [TECH DEMO]
