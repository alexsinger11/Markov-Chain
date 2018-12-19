from markov_python.cc_markov import MarkovChain
from fetch_data2 import read_lyrics


mc = MarkovChain()

mc.add_string(read_lyrics('all_lyrics.html'))

song = mc.generate_text(100)
song = [str(i) for i in song ]
song = " ".join(song)

print song