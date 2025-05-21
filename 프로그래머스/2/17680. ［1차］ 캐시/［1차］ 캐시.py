def solution(cacheSize, cities):
    cache = []
    time = 0
    
    if cacheSize > 0:
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.remove(city)
                cache.append(city)
                cache = cache[-cacheSize:]
                time += 1
            else:
                cache.append(city)
                cache = cache[-cacheSize:]
                time += 5        
        return time
    
    else:
        return len(cities) * 5