class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song (["Happy birthday to you",
                   "I don't want to get swed",
                   "So I' ll stop right there"])

bulls_on_parade = Song(["They rally the family",
                        "With pockets full od shells"])

human = Song(["I'm only human, I'm only, I'm only",
"I'm only human, human",
"Maybe I'm foolish, maybe I'm blind",
"Thinking I can see through this and see what's behind",
"Got no way to prove it so maybe I'm lying",
    ])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
human.sing_me_a_song()