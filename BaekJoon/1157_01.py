word = input().upper()

alphabet_Map = {}

for i in range(len(word)):    
    if word[i] not in alphabet_Map:
        alphabet_Map[word[i]] = 0
    
    alphabet_Map[word[i]] += 1

max_count = max(alphabet_Map.values())
frequency = []

for char, cnt in alphabet_Map.items():
    if cnt == max_count:
        frequency.append(char)
    
if len(frequency) > 1:
    print("?")
else:
    print(frequency[0])