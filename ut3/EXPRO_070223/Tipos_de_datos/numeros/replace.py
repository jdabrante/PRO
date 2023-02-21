song = '''You look so beautiful in this light

Your silhouette over me

The way it brings out the blue in your eyes

Is the Tenerife sea

And all of the voices surrounding us here

They just fade out when you take a breath

Just say the word and I will disappear

Into the wilderness'''

new_word  = "sounds"

first_part = song[:song.index("voices")]
second_part = song[song.index("voices")+len("voices"):]

new_song = first_part + new_word + second_part
new_song
