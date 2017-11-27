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
    #putting blanks at the beginning of list but not if we have already done this
    if(s[0] != [" ", " ", " "] and t[0] != [" ", " ", " "]):
        s.insert(0,[" ", " ", " "])
        t.insert(0,[" ", " ", " "])
    #appending blank tuples at the start of the list
    C.append([(0,"")])
    #instantiating first row all with "i" = insert
    for i in range(1,len(s)+1):
        C[0].append((i, "i"))
    #instantiating all the columns with "d" = delete
    for i in range(len(s)-1):
        C.append([(i+1,"d")])
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            #test by either song, artist, or genre in the else case
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
            #depending on which way we went we either put and "a" = replace or leave or "i" or "d"
            if(c_match <= c_ins and c_match <= c_del):
                C[i].append((c_match, "a"))
            elif(c_ins <= c_del):
                C[i].append((c_ins, "i"))
            else:
                C[i].append((c_del, "d"))
    print "{} edits it turn playlist 1 into playlist 2".format(C[i][j][0])
    pathList = []
    #going reverse order from the end to the beginning following the letters for direction
    while(i > 0 or j > 0):
        if(C[i][j][1] == "a"):
            if(C[i][j][0] == C[i-1][j-1][0]):
                pathList.append("leave {} unchanged".format(s[i]))
            else:
                pathList.append("replace {} with {}".format(s[i],t[j]))
            i-=1
            j-=1
        elif(C[i][j][1] == "i"):
            pathList.append("insert {}".format(t[j]))
            j-=1
        else:
            pathList.append("delete {}".format(s[i]))
            i-=1
    #print list in reverse since we started at the end
    for i in xrange(len(pathList)):
        print pathList.pop()


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
    playlist_transform(b1,b2)
    print "Comparing playlist similarity by genre"
    playlist_transform(b1,b2,"Genre")
    print "Comparing playlist similarity by artist"
    playlist_transform(b1,b2,"Artist")
    #include your own playlists below
    r1 = read_playlist("rock1.csv")
    r2 = read_playlist("rock2.csv")
    print "\n"
    print "Comparing playlist similarity by song"
    playlist_transform(r1,r2)
    print "Comparing playlist similarity by genre"
    playlist_transform(r1,r2,"Genre")
    print "Comparing playlist similarity by artist"
    playlist_transform(r1,r2,"Artist")