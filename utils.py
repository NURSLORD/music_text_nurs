# https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html
# return dance_monkey
def give_music_name(name):
    d = name.split('/')
    for i in d:
        if i.endswith('.html'):
            return ''.join(i[: -5])


