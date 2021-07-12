"""
Как написать код для 'Программа на Python для проверки скорости набора текста'
Полный разбор.
https://pythonru.com/primery/programma-na-python-dlja-proverki-skorosti-nabora-teksta
"""
"""
Программа на Python для проверки скорости набора текста
18.07.2020

Курс «Программирование на Python»
Станьте Python-разработчиком с нуля. Гарантированная помощь в трудоустройстве
ПОДРОБНЕЕ
SKILLBOX.RU

Играли ли вы когда-нибудь в игры, где проверяется скорость набора текста? 
Это очень полезное развлечение, поскольку оно позволяет не только отслеживать 
значение, но и улучшает навык со временем. Если заинтересовались, то ее 
вполне можно создать самостоятельно.

О проекте
Программа для проверки скорости набора текста
В этом проекте создадим приложение на Python, с помощью которого 
можно будет проверять и увеличивать собственную скорость набора текста. 
Для графического интерфейса используем библиотеку pygame, которая для 
этих целей и предназначена. Также нарисуем изображения, которые будут 
отображаться на экране.

Требования
Для работы над проектом требуются базовые знания программирования 
на Python и библиотеки pygame.

Для установки библиотеки используйте в терминале следующую команду.

pip install pygame
Шаги для создания проекта
По этой ссылке можно загрузить весь исходный код проекта: typing-speed-game.rar

Для начала разберемся с файловой структурой проекта:

background.jpg — фоновое изображение для программы
icon.jpg — иконка для кнопки сброса
sentences.txt — текстовый файл со списком предложений
speed_typing.py — файл со всем кодом программы
typing-speed-open.png — иконка для отображения при запуске игры
Создадим файл sentences.txt, в котором на каждой строке добавим по предложению.

При создании проекта будем использовать принципы 
объектно-ориентированного программирования.

Импортируем библиотеки
Для этого проекта будем использовать библиотеку pygame. 
Ее нужно импортировать вместе с другими встроенными модулями Python, 
такими как time и random.

import pygame
from pygame.locals import *
import sys
import time
import random

Создадим класс игры
Дальше создаем класс игры, который будет содержать функции для старта, 
сброса и несколько дополнительных, отвечающих за вычисления.

Создадим конструктор класса, в котором будет определены все переменные проекта.

class Game:
    def __init__(self):
        self.w=750
        self.h=500
        self.reset=True
        self.active = False
        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h))
        
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500,750))
        
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Type Speed test')
        
В этом конструкторе инициализируем ширину и высоту окна, 
а также переменные, которые нужны для вычислений. 
Наконец, инициализируем саму pygame и загрузим изображения. 
Самое важное — переменная экрана, на котором будет выводиться интерфейс.

Метод draw_text()
Метод draw_text() — это вспомогательная функция для класса Game, 
которая выводит текст на экран. В качестве аргумента она принимает экран, 
выводимое сообщение, координату y экрана, где нужно нарисовать текст, 
а также размер и цвет шрифта. В этом случае все должно выводиться по центру. 
После прорисовки pygame нужно обновить экран.

def draw_text(self, screen, msg, y ,fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1,color)
    text_rect = text.get_rect(center=(self.w/2, y))
    screen.blit(text, text_rect)
    pygame.display.update()
    
Метод get_sentence()
В файле sentences.txt хранится список предложений. 
Метод get_sentence() будет открывать его и возвращать случайное 
предложение из списка. Целая строка будет разбиваться с помощью 
символа новой строки.

def get_sentence(self):
    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    return sentence
    
Метод show_results()
В методе show_results() рассчитывается скорость набора. 
Таймер запускается в тот момент, когда пользователь нажимает 
на поле ввода, а останавливается в момент нажатия Enter. 
Затем рассчитывается разница и определяется время в секундах.

Для вычисления точности используется математика. Подсчитываются 
правильно введенные символы за счет сравнения введенного текста 
с тем, который нужно было ввести.

Формула следующая:
(правильные символы) х 100 / (всего символов в предложении)

WPM (words per minute) — это количество слов в минуту. 
Типичное слово состоит приблизительно из 5 символов, поэтому 
рассчитываем показатель, разделяя общее количество слов на 5. 
Затем результат делится на общее время, которое потребовалось 
для набора. Поскольку общее время указано в секундах, его 
сначала нужно конвертировать в минуты, разделив значение на 60.

Наконец, в нижней части есть иконка, выступающая кнопкой сброса. 
Когда пользователь нажимает на нее, игра сбрасывается. Речь о методе 
reset_game() пойдет дальше.

    def show_results(self, screen):
        if(not self.end):
            # Расчет времени
            self.total_time = time.time() - self.time_start
               
            # Расчет точности
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100
           
            # Расчет количества слов в минуту
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)
                
            self.results = 'Time:'+str(round(self.total_time)) +" secs   Accuracy:"+ str(round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # Загрузка иконки
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150,150))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75,self.h-140))
            self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()
            
Метод run()
Это основной метод класса, отвечающий за обработку всех событий. 
Метод reset_game() вызывается в начале метода, который сбрасывает 
все переменные. Затем выполняется бесконечный цикл, который 
захватывает все события мыши и клавиатуры. После этого на экране 
рисуются заголовок и поле ввода.

Другой цикл ждет событий мыши и клавиатуры. Когда кнопка мыши нажимается, 
проверяется ее положение. Если она над полем ввода, то таймер запускается, 
а переменная active становится True. Если над кнопкой сброса — игра сбрасывается.

Когда значение active равняется True, а набор текста не завершен, 
ожидаются события с клавиатуры. Если пользователь нажимает любую клавишу, 
то нужно обновить сообщение поля ввода. Клавиша Enter завершает ввод, 
после чего происходят вычисления. Еще одно событие — для клавиши Backspace, 
которая удаляет последний символ введенного текста.

    def run(self):
        self.reset_game()
    
       
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            # Обновление текста пользовательского ввода
            self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # Расположение окна ввода
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time() 
                     # Расположение кнопки сброса
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
             
                
        clock.tick(60)
        
Метод reset_game()
Метод reset_game() сбрасывает все переменные, так что проверить скорость 
набора можно снова. Еще раз выбирается случайное предложение с помощью 
метода get_sentence(). В конце определение класса закрывается. 
Создаем объект класса Game и запускаем программу.

    def reset_game(self):
        self.screen.blit(self.open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self.reset=False
        self.end = False

        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Получаем случайное предложение 
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        # Загрузка окна
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg,80, 80,self.HEAD_C)  
        # Отрисовка поля ввода
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)

        # Отрисовка строки предложения
        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()



Game().run()
Вывод:
Программа для проверки скорости набора текста старт
Программа для проверки скорости набора текста результат
Выводы
В этом проекте мы создали игру на Python с использованием pygame, 
которая отслеживает скорость набора текста пользователем.
"""