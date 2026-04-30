# Задание 1
## Часть 1
Установка Grav в Docker

### Установка Docker Desktop на компьютер

1.  С официального сайта Docker скачиваем установочный файл

![screenshot](images/screenshot_1.png)

2. После скачивания, запускаем установочный файл и следуем инструкциям

![screenshot](images/screenshot_2.png)

3. После завершения установки, откроется Docker Desktop

![screenshot](images/screenshot_3.png)

### Запуск Grav в Docker

1. Создаём новую директорию в корне диска и переходим в новую директорию

![screenshot](images/screenshot_4.png)

2. Создаём в директории файл Dockerfile и вставляем туда содержимое Dockerfile из репозитория docker-grav  

![screenshot](images/screenshot_5.png)

3. Создаём в директории файл docker-compose.yml и вставляем туда содержимое docker-compose.yml из репозитория docker-grav

![screenshot](images/screenshot_6.png)

4. Создаём в директории директорию grav и разархивируем туда содержимое grav_admin-v1.7.52, которое мы ранее скачали с официального сайта GRAV

![screenshot](images/screenshot_7.png)

5. После всего мы с помощью команды "docker compose up -d" начинаем сборку

![screenshot](images/screenshot_8.png)
