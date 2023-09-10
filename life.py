import pygame,sys,itertools,time

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

ALIVE_COLOR = (255,255,255)
DEAD_COLOR = (0,0,0)
CELL_SIZE = 5

ALL_COORDINATES = list(itertools.product(list(range(0,WIDTH,CELL_SIZE)),list(range(0,HEIGHT,CELL_SIZE))))

def glider_gun():
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(10*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(11*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(10*5,31*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(11*5,31*5, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(23*5,27*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(22*5,27*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(21*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(20*5,29*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(20*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(20*5,31*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(21*5,32*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(22*5,33*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(23*5,33*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(24*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(25*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(25*5,32*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(26*5,29*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(26*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(26*5,31*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(27*5,30*5, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(30*5,29*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(30*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(30*5,27*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(31*5,29*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(31*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(31*5,27*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(32*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(32*5,26*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(34*5,26*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(34*5,25*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(34*5,30*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(34*5,31*5, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(44*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(44*5,27*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(45*5,28*5, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen,ALIVE_COLOR,pygame.Rect(45*5,27*5, CELL_SIZE, CELL_SIZE))

#glider_gun()

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
