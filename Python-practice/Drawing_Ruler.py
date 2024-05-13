def draw_ruler(num_inches, major_lenght):
    draw_line(major_lenght, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_lenght-1)
        draw_line(major_lenght, str(j))

def draw_interval(center_lenght):
    if center_lenght > 0:
        draw_interval(center_lenght-1)
        draw_line(center_lenght)
        draw_interval(center_lenght-1)

def draw_line(tick_lenght, tick_label=""):
    line = "-"*tick_lenght
    if tick_label:
        line += " "+tick_label
    print(line)


draw_ruler(2,4)