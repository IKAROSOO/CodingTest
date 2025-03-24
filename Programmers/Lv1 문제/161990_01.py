def solution(wallpaper):
    answer = []
    data = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            icon = wallpaper[i][j]
            
            if icon == "#":
                data.append([i, j])
    
    rows = [point[0] for point in data]
    cols = [point[1] for point in data]

    return [min(rows), min(cols), max(rows) + 1, max(cols) + 1]