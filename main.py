from random import randrange
from sys import exit as sys_exit
from webbrowser import open as browser_open


def get_season():
    se = randrange(1, 12, 1)
    return se


def get_episode(season_num):
    if season_num == 1:
        ep = randrange(1, 17, 1)
    elif 1 < season_num < 4:
        ep = randrange(1, 23, 1)
    else:
        ep = randrange(1, 24, 1)
    return ep


def get_url(season_num, episode_num):
    url = f'https://hd.kinopoisk.ru/film/4c96bc227a377c8aa98da3789416c811?episode={episode_num}&from_block=kp-button-online&season={season_num}&watch='
    return url


if __name__ == '__main__':
    season = get_season()
    episode = get_episode(season)
    browser_open(get_url(season, episode))
    sys_exit()


# pyinstaller --onefile --nowindowed --icon "ico/TBBT.ico" --name "TheBigBangTheory_Randomizer" main.py
