'''
    >>> Програє звуки і музику
    >>> Зупиняє звук і музику
'''
# імпортуємо модулі 
import pygame, os 
import modules.data as m_data
# ініцілізуємо звук
pygame.mixer.init()
# встановлємо гучність для відтворення музики
# pygame.mixer.music.set_volume(0.5)
# створення класу для роботи з аудіо
class Audio():
    '''
        >>> Додає фонову музику
        >>> Встановлює гучність для звуку
    '''
    # ініцілізуємо клас аудіо 
    def __init__(self, name: str, loops: int = -1,volume = 0.5,max_time = "any"): 
        # створюємо змінні
        self.audio = None 
        self.name = name 
        self.loops = loops
        self.stoped = True
        # додаємо фонову музику
        self.audio = pygame.mixer.Sound(os.path.abspath(f"{__file__}/../../audio/{self.name}.mp3"))
        # встановлюємо гучність звуку
        self.audio.set_volume(volume)
        # перевіряємо чи дорівнює максимальний час будь-якому
        if max_time == 'any':
            # додаємо довжину звуку
            max_time = self.audio.get_length()
    # метод для відтворення аудіо
    def play(self, volume = 0.5):
        '''
            >>> Починає музику
            
        '''
        try:
            # зупиняємо музику
            self.stoped = False
            # відтворюємо музику
            self.audio.set_volume(volume)
            self.audio.play(loops= self.loops)
        except:
            # якщо буде помилка при завантаженні, виводимо повідомлення про помилку
            pass
    # метод для зупинки звуку

    def stop(self):
        '''
            >>> Зупиняє звук
            >>> Задає зупинки між звуками
            >>> Додає звук до досягнень
            >>> Додає звук для вибуху
            >>> Зупиняє музику
        '''
        # зупинка звуку
        self.audio.stop()
        # задаємо для зуптнки звуку значення True 
        self.stoped = True
# додаємо звук для досягнення
achievement = Audio('achievement',max_time=2, loops=0)
# додаємо звук для радару
radar = Audio('radar', loops=0)
name = '1'
try:
    with open(m_data.path+m_data.type+'music.txt', "r") as file:
        text = file.read()
        if 0 < int(text) < 5:
            name = int(text)
except Exception as error:
    print(error)
    with open(m_data.path+m_data.type+'music.txt', "w") as file:
        file.write('1')

# задаємо саундтрек для доріжки звуку
track = Audio(f'Soundtracks/{name}')
# задаємо саундтрек для доріжки звуку
# track_war = Audio('Soundtrack_war')
# додаємо звук покупки
buying = Audio('buying',0)
# перевіряємо чи не дорівнює звук значенню False
if m_data.read_data["sound"] != "False":
    # граємо звукову доріжку
    track.play()
# додаємо звук для вибуху
explosion = Audio('blas',0)