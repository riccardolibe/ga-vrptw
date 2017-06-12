from roadmap import RoadMap
from vehicle import Vehicle

roadmap = RoadMap(10)

vehicle1 = Vehicle()
time = 0
while roadmap.total_demand != 0:
    time += vehicle1.visit_next(roadmap)
    time = time % 24
    customer = roadmap.map.node[vehicle1.position]['customer']
    if vehicle1.unload(customer, time):
        customer.receive_goods(roadmap)

    print('demand', roadmap.total_demand, 'pos', vehicle1.position, 'time', time)
print(vehicle1.past_path)
print('total time:', vehicle1.tot_time, 'total cost:', vehicle1.tot_cost)
roadmap.show_map()


