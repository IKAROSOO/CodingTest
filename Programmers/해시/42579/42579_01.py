def solution(genres, plays):
    answer = list()
    genre_dict = dict()
    
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [0]
        genre_dict[genres[i]][0] += plays[i]
        genre_dict[genres[i]].append([i, plays[i]])
    
    genre_dict = dict(sorted(genre_dict.items(), key=lambda item: item[1][0], reverse=True))
    
    for key in genre_dict.keys():
        if len(genre_dict[key]) == 2:
            answer.append(genre_dict[key][1][0])
            continue
            
        songs = genre_dict[key][1:]
        songs = sorted(songs, key=lambda item: (-item[1], item[0]))
        
        answer.append(songs[0][0])
        answer.append(songs[1][0])
    
    return answer