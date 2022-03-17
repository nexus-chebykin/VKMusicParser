#coding="UTF-8"
import bs4
raw_input = open('SavedPage.htm').read()
page = bs4.BeautifulSoup(raw_input, features="lxml")
for el in page.find_all(class_ = 'audio_row__performers'):
    performer = ''
    for ch in list(el.children):
        performer += ch.string
    song_name_start = el.find_next(class_ = 'audio_row__title_inner')
    song_name_end = song_name_start.find_next('span')
    performer = performer.strip()
    song_name_start = song_name_start.string.strip()
    song_name_end = song_name_end.string.strip() if song_name_end.string else ''
    print(f'{performer}: {song_name_start} {song_name_end}' )
