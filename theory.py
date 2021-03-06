# Словарь, содержащий теорию по основам синтаксиса python, поясняющий текст для дополнительной клавиатуры.
theory_dict = {
    "KEYBOARD_2": """Также вы можете:
1) Преобразовать своё текстовое сообщение в голосовое. Отправьте боту текстовое сообщение, а он запишет его для вас в формате аудио. 
2) Познакомиться с определённой философией программирования, называемой «The Zen of Python» («Дзен Питона», или «Дзен Пайтона»). Её текст выдаётся интерпретатором Python по команде import this.
3) Перейти на официальный сайт Python и продолжить погружение в этот невероятно интересный язык программирования.""",
    "HISTORY": """Задумка по реализации языка появилась в конце 1980-х годов, а разработка его реализации началась в 1989 году сотрудником голландского института CWI Гвидо ван Россумом. Для распределённой операционной системы Amoeba требовался расширяемый скриптовый язык, и Гвидо начал разрабатывать Python на досуге, позаимствовав некоторые наработки для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. С самого начала Python проектировался как объектно-ориентированный язык.""",
    "GENERAL": """Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н или па́йтон) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным — всё является объектами. Необычной особенностью языка является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как Си или C++.""",
    "TYPES": """Python поддерживает динамическую типизацию, то есть тип переменной определяется только во время исполнения. Поэтому вместо «присваивания значения переменной» лучше говорить о «связывании значения с некоторым именем». К примитивным типам в Python относятся булевый, целое число произвольной точности, число с плавающей запятой и комплексное число. Из контейнерных типов в Python встроены: строка, список, кортеж, словарь и множество. Все значения являются объектами, в том числе функции, методы, модули, классы. Добавить новый тип можно либо написав класс (class), либо определив новый тип в модуле расширения (например, написанном на языке C). Система классов поддерживает наследование (одиночное и множественное) и метапрограммирование. Возможно наследование от большинства встроенных типов и типов расширений.""",
    "SYNTAX_1": """Выполнение кода Python\n
Python — интерпретируемый язык программирования, что означает, что в разработке вы создаете файлы Python (.py) в текстовом редакторе, а затем помещаете эти файлы в интерпретатор python для выполнения кода.
Способ запуска файла python аналогичен командной строке:
C:\\Users\\Yourname>python helloworld
где “helloworld” — это название вашего файла python с расширением .py""",
    "SYNTAX_2": """Отступы в Python\n
В то время как в других языках программирования отступ в коде предназначен только для чтения, в Python отступ очень важен. Python использует отступ для указания блока кода:\n
if 5 > 2:  
    print("Пять больше двух!")\n
Python заявит вам об ошибке, если вы пропустите отступ:\n
if 5 > 2:  
print("Пять больше двух!")\n
Результат:\n
File "demo_indentation_test", line 2  
    print("Пять больше двух!")  
        ^  
IndentationError: expected an indented block""",
    "SYNTAX_3": """Комментарии\n
Python предоставляет возможность комментирования документации внутри кода. Комментарии следует начинать с символа #, а интерпретатор отобразит остальную часть строки в виде комментария:\n
# Это комментарий.  
print("Привет, Мир!")""",
    "SYNTAX_4": """Строки документации\n
В Python также имеются расширенные возможности документации, называемые docstrings. Строки документации могут быть однострочными или многострочными. Python использует тройные кавычки в начале и конце docstring.\n
\"\"\"Это многострочная
строка документации\"\"\"  
print("Привет, Мир!")""",
    "ZEN": """Красивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибка никогда не должна замалчиваться.
Если только вы сами этого не захотите.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать что-то.
Хотя он поначалу может быть и не очевиден, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить — идея плоха.
Если реализацию легко объяснить — идея, возможно, хороша.
Пространства имён — отличная штука! Будем делать их больше!"""
}