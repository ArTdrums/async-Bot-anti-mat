# async-Bot-anti-mat
Бот для цензурной лексики и политики.
    Используемые библиотеки: aiogram, time.
    1.Бот написан на ассинхронной библиотеке aiogram, используются асинхронные функции.
    2.Реализовано чтение файлов с помощью менеджера контекста with, содержавших не цензурную
    и политическую лексику.                          
    3. Бот получает сообщение, сравнивает содержание слов в словарях и если данные слова 
    содержаться в словарях, заменяет их на ***. Как именно происходит проверка опишу ниже.
a.	Бот принимает сообщение в сороковом виде, далее с помощью метода split() разбиваем на элементы списка, далее запускаем проверку на содержание данного слова в нашем словаре и если содержится заменяем его, далее склеиваем все назад в строку методом join()
b.	Проверка на политику проходит аналогичным образом, только в результате проверки появляется фраза “Тут не место политике.
