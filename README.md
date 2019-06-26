# MD->PDF конвертер

Инструмент для конвертации MD файлов в PDF.

## Принцип работы

Сначала на основе MD формируется HTML файл, к которому присоединяется файл со стилями. Далее из него формируется файл PDF.

## Запуск

Поместить необходимые файлы в директорию с исполняемым файлом и запустить:

```text
python main.py
```

В данном случае, программа будет использовать для конвертации файл `README.MD`, файл стилей `style.html`, файл шрифтов `Roboto-Regular.ttf` в текущей директории. Также сохранит результат в файле `README.pdf` в текущей каталоге.

Это аналогично вызову:

```text
python main.py -m README.MD -s style.html -p README.pdf -d ./ -f Roboto-Regular.ttf
```

### Параметры вызова

* `-m` или `--md`: файл MD, который необходимо конвертировать;

* `-s` или `--style`: файл, в котором содержится информация для оформления итогового PDF;

* `-p` или `--pdf`: название результирующего pdf файла;

* `-d` или `--directory`: каталог, в который будет помещен результирующий файл;

* `-f` или `--font`: файл со шрифтами, при помощи которых будет сформирован PDF (необходимо, если в документе присутствует кириллица).
