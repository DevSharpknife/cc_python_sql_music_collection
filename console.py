import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()

artist_1 = Artist('Dave')
artist_repository.save(artist_1)
artist_2 = Artist('Matt/Jen')
artist_repository.save(artist_2)

artists = artist_repository.select_all()

fetch_artist = artist_repository.select(1)

pdb.set_trace()