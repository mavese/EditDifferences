#Matteo Mantese

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def playlist_transform(s,t,compareType="Song"):
    """
    Computes the edit distance for two playlists s and t, and prints the minimal edits
      required to transform playlist s into playlist t.
    Inputs:
    s: 1st playlist (format: list of (track name, artist, genre) triples)
    t: 2nd playlist (format: list of (track name, artist, genre) triples)
    compareType: String indicating the type of comparison to make.
       "Song" (default): songs in a playlist are considered equivalent if the
         (song name, artist, genre) triples match.
       "Genre": songs in a playlist are considered equivalent if the same genre is used.
       "Artist": songs in a playlist are considered equivalent if the same artist is used.
    Output: The minimum edit distance and the minimal edits required to transform playlist
      s into playlist t.
    """
    C=[]
    s.insert(0,[" ", " ", " "])
    t.insert(0,[" ", " ", " "])
    C.append([(0,"")])
    for i in range(1,len(s)-1):
        C[0].append((i, "s"))
    # C.append(range(len(t)))
    for i in range(len(s)-1):
        C.append([(i+1,"d")])
    for lists in C:
        print lists
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            if(compareType == "Song"):
                if s[i] == t[j]: c_match = C[i-1][j-1][0]
                else: c_match = C[i-1][j-1][0]+1
            elif(compareType == "Artist"):
                if s[i][1] == t[j][1]: c_match = C[i-1][j-1][0]
                else: c_match = C[i-1][j-1][0]+1
            else:
                if s[i][2] == t[j][2]: c_match = C[i-1][j-1][0]
                else: c_match = C[i-1][j-1][0]+1
            c_ins = C[i][j-1][0]+1
            c_del = C[i-1][j][0]+1
            if(c_match <= c_ins and c_match <= c_del):
                C[i].append((c_match, "a"))
            elif(c_ins <= c_del):
                C[i].append((c_ins, "s"))
            else:
                c[i].append((c_del, "d"))
            # c_min=min(c_match, c_ins, c_del)
            # C[i].append(c_min)
    for lists in C:
        print lists
    k = 0
    l = 0
    angle = False
    down = False
    prev = 0
    path = ""
    # while k < len(C)-1 or l < len(C[k])-1:
    #     if(k == len(C)-1 and l < len(C[k])-1):
    #         l+=1
    #     elif(k < len(C)-1 and l == len(C[k])-1):
    #         k+=1
    #         down = True
    #     elif(C[k][l+1]<=C[k+1][l] and C[k][l+1]<=C[k+1][l+1]):
    #         l+=1
    #     elif(C[k+1][l]<=C[k][l+1] and C[k+1][l]<=C[k+1][l+1]):
    #         k+=1
    #         down = True
    #     else:
    #         k+=1
    #         l+=1
    #         angle = True
    #     if(prev == C[k][l]):
    #       print "keep {}".format(s[k][0])
    #     elif(angle):
    #         print "replace {} with {}".format(s[k][0],t[l][0])
    #     elif(down):
    #         print "delete {}".format(s[k][0])
    #     else:
    #         print "insert {}".format(t[l][0])
    #     prev = C[k][l]
    #     path = path + "({},{})".format(k,l)
    #     down = False
    #     angle = False
    # print path
    print C
    return C[i][j]


if __name__=="__main__":
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues1.csv
    b1 = read_playlist("blues1.csv")
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues2.csv
    b2 = read_playlist("blues2.csv")
    print "Playlist 1"
    for song in b1:
        print song
    print "Playlist 2"
    for song in b2:
        print song
    print "Comparing playlist similarity by song"
    print playlist_transform(b1,b2)
    print "Comparing playlist similarity by genre"
    print playlist_transform(b1,b2,"Genre")
    print "Comparing playlist similarity by artist"
    print playlist_transform(b1,b2,"Artist")
    #include your own playlists below