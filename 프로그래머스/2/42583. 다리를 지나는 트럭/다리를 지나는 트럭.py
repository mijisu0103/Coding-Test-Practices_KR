def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    currentWeight = 0
    
    while len(truck_weights) > 0:
        time += 1
        currentWeight = currentWeight - bridge.pop(0)
    
        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time