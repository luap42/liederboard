SCORES = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]

def get_tally(preferences):
    songs = {}
    
    for juror in preferences:
        score_index = 0

        for song, band in juror:
            nsong = normalize(song)

            if nsong in songs:
                songs[nsong]['score'] += SCORES[score_index]
            
            else:
                for other_nsong in songs.keys():
                    if (nsong in other_nsong or other_nsong in nsong) and songs[other_nsong]['band'] == band:
                        songs[other_nsong]['score'] += SCORES[score_index]
                        break
                else:
                    songs[nsong] = {
                        'score': SCORES[score_index],
                        'title': song,
                        'band': band
                    }
            
            score_index += 1
        
    song_list = songs.values()
    song_list = sorted(song_list, key=lambda s: s['score'])[::-1]

    return song_list




def normalize(string):
    string = string.upper()

    new_string = ""

    for char in string:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            continue

        new_string += char
    
    return new_string