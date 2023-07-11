def solution(cap, n, deliveries, pickups):
    end_point_for_deliveries = n - 1
    end_point_for_pickups = n - 1
    hand_deliver = 0
    hand_pickup = 0
    while True:
        distance_deliver = 0
        tmp_deliver = 0
        while hand_deliver < cap:
            if end_point_for_deliveries < 0:
                break
            if deliveries[end_point_for_deliveries] == 0:
                end_point_for_deliveries -= 1
            else:
                deliveries[end_point_for_deliveries] -= 1
                tmp_deliver = end_point_for_deliveries + 1
                hand_deliver += 1
                distance_deliver = max(tmp_deliver, distance_deliver)

        tmp_pickup = 0
        while hand_pickup < cap:
            if end_point_for_pickups < 0:
                break
            if deliveries[end_point_for_pickups] == 0:
                end_point_for_pickups -= 1
            else:
                deliveries[end_point_for_pickups] -= 1

                tmp_pickup = end_point_for_pickups + 1
                hand_pickup += 1
                distance_deliver = max(tmp_pickup, distance_deliver)
        if end_point_for_pickups < 0 and end_point_for_deliveries < 0:
            return distance_deliver * 2

    return distance_deliver

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))