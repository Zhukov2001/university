# Задание 1
## Часть 1
Установка Grav в Docker

### Установка Docker Desktop на компьютер

1.  С официального сайта **Docker** скачиваем установочный файл

![screenshot](images/screenshot_1.png)

2. После скачивания - запускаем установочный файл и следуем инструкциям

![screenshot](images/screenshot_2.png)

3. После завершения установки - откроется Docker Desktop

![screenshot](images/screenshot_3.png)

### Запуск Grav в Docker

1.  Создаём папку для проекта

```powershell
mkdir C:\Users\Danila\grav
cd C:\Users\Danila\grav
```
![screenshot](images/screenshot_4.png)

2. Создаём файл _docker-compose.yml_ и копируем в него содержимое того же файла из официального репозитория

```powershell
notepad docker-compose.yml
```

```yaml
services:
  grav:
    image: getgrav/grav
    container_name: grav
    ports:
      - "8080:80"
    volumes:
      - grav_site:/var/www/html
    restart: unless-stopped

volumes:
  grav_site:
```

![screenshot](images/screenshot_5.png)

3. Запуск контейнера

```powershell
docker compose up -d
```
![screenshot](images/screenshot_6.png)

![screenshot](images/screenshot_7.png)

4. После запуска контейнера ждём несколько минут (для того чтобы grav установился). Для проверки можно использовать команду:

```powershell
docker logs grav -f
```
5. После вывода в терминал "Grav installation complete!" можем выйти **Ctrl+C** из терминала, а после открыть в браузере _http://localhost:8080_

![screenshot](images/screenshot_8.png)

6. После того как в браузере мы открыли _http://localhost:8080_, мы должны увидеть следующие:

![screenshot](images/screenshot_9.png)

7. Заполняем информацию

![screenshot](images/screenshot_10.png)

8. После заполнения информации, мы войдём в панель администратора

![screenshot](images/screenshot_11.png)

9. Рекомендуется обновить

![screenshot](images/screenshot_12.png)

10. Далее мы можем начать создание страниц, для этого переходим в вкладку **Pages**

![screenshot](images/screenshot_13.png)   

11. И создадим новую страницу

![screenshot](images/screenshot_14.png)  

12. Указываем параметры страницы

![screenshot](images/screenshot_15.png)

13. Пишем информацию, которая будет отображаться на странице и сохраняем

![screenshot](images/screenshot_16.png)

14. Переходим по ссылке _http://localhost:8080_ (без _admin/pages/test_) где мы можем посмотеть на нашу страницу без привилегий админа

![screenshot](images/screenshot_17.png)

15. После того как мы выполнили все наши действия, мы можем завершить работу контеёнера Docker, выполнив в терминале команду:

```powershell
docker compous down
```
![screenshot](images/screenshot_18.png)

После этого наши страницы будут недоступны 

![screenshot](images/screenshot_19.png)
