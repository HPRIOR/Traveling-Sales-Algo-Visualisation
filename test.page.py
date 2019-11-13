from tkinter import *
from cities import *

#road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
#             ("Delaware", "Dover", 39.161921, -75.526755),
#             ("Minnesota", "Saint Paul", -44.95, 93.094)]
#
#
#def change_visualise_data(road_map):
#    data_road_map = []
#    [data_road_map.append(list(line)) for line in road_map]
#    for line in data_road_map:
#        line[2] = (line[2] + 90)
#        line[3] = (line[3] + 180)
#    return data_road_map
#
#
#def visualise(road_map):
#    road_map = change_visualise_data(road_map)
#    print(road_map)
#    main_win = Tk()
#    canv = Canvas(main_win, width=360, height=360, background='white')
#    canv.pack(fill=BOTH)
#    ln = len(road_map)
#    ind = 0
#    for i in range(ln):
#        canv.create_line(road_map[ind - 1][2], road_map[ind - 1][3],
#                         road_map[ind][2], road_map[ind][3])
#        print(road_map[ind - 1][2], road_map[ind - 1][3],
#              road_map[ind][2], road_map[ind][3])
#        ind = (ind + 1) % ln
#    main_win.mainloop()
#
#
#print(change_visualise_data(road_map1))
#
#visualise(road_map1)
