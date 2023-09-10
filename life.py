import pygame,sys,itertools,glider_gun,time

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

ALIVE_COLOR = (255,255,255)
DEAD_COLOR = (0,0,0)
CELL_SIZE = 5

ALL_COORDINATES = list(itertools.product(list(range(0,WIDTH,CELL_SIZE)),list(range(0,HEIGHT,CELL_SIZE))))

glider_gun.setup(screen,ALIVE_COLOR,CELL_SIZE)

def simulation():

    changing_cells = []

    get_color = screen.get_at

    for coords in ALL_COORDINATES:
        (x,y) = (coords[0],coords[1])
        adjacent_cells = []
        cell_color = get_color((x,y))

        try:
            adjacent_cells.append(get_color((x+CELL_SIZE,y)))
        except:
            pass
            
        try:
            adjacent_cells.append(get_color((x,y+CELL_SIZE)))
        except:
            pass
            
        try:
            adjacent_cells.append(get_color((x-CELL_SIZE,y)))
        except:
            pass

        try:
            adjacent_cells.append(get_color((x,y-CELL_SIZE)))
        except:
            pass

        try:
            adjacent_cells.append(get_color((x+CELL_SIZE,y+CELL_SIZE)))
        except:
            pass

        try:
            adjacent_cells.append(get_color((x+CELL_SIZE,y-CELL_SIZE)))
        except:
            pass
            
        try:
            adjacent_cells.append(get_color((x-CELL_SIZE,y+CELL_SIZE)))
        except:
            pass
            
        try:
            adjacent_cells.append(get_color((x-CELL_SIZE,y-CELL_SIZE)))
        except:
            pass

        adjacent_alive_cells = adjacent_cells.count(ALIVE_COLOR)

        if adjacent_alive_cells == 3 and cell_color == DEAD_COLOR: #Dead Cell Becomes Alive
            changing_cells.append((x,y,"BORN"))

        elif (adjacent_alive_cells >3 or adjacent_alive_cells <2) and cell_color == ALIVE_COLOR:
            changing_cells.append((x,y,"DEAD"))
    
    for cells in changing_cells:
        if cells[2] == "BORN":
            pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(cells[0],cells[1], CELL_SIZE, CELL_SIZE))
        elif cells[2] == "DEAD":
            pygame.draw.rect(screen,DEAD_COLOR,pygame.Rect(cells[0],cells[1], CELL_SIZE, CELL_SIZE))
                
paused = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = True if not paused else False
            elif event.key == pygame.K_c:
                screen.fill(DEAD_COLOR)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(round(mouse_pos[0]/CELL_SIZE)*CELL_SIZE,round(mouse_pos[1]/CELL_SIZE)*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if not paused:
        simulation()

    pygame.display.update()
