def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

if __name__=='__main__':
	print(song_decoder("AWUBBWUBC"))
