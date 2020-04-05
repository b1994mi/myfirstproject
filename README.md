This is my first website using Django and Leaflet.js. You can create a user and view a map of every user that is registered on the SQLite database.

![mymapapp screenshot](https://obs.line-scdn.net/h7tyRxip5dFpiR2dUJhFzIzg1PjhrGSdZKkovNWMsM249HXxef08mOGEpP2I8EisNe0kkPjN4NGtrGmoMKx8jbWl7MA/m800x1200)

### Features

* It extends Django's User Model with OneToOne; adding few new fields, such as longitude and latitude (decimal field).
* It can show a map of the user's longitude and latitude using Leaflet.js and OpenStreetMap.
* It comes with three users (user1, user2, user3) inside the provided SQLite for showcase purposes.

### How to Install

* Make sure you have python 3 and Django installed.
* Download the project and extract it.
* Open the terminal/command line and change the directory to that downloaded page (myfirstproject).
* Run the development server using '''bash python manage.py runserver '''.
* Open your favorite browser and go to '''bash localhost:8000 '''

### More Screenshots
![mymapapp screenshot](https://obs.line-scdn.net/hlpdWBBR2L15_QjxQOxQoJyUwaW13TXYPZ0B4bHQsaGd2HXxcYRp1OX8paT0jF3dZZht_OnwrbW9xGjEINhp4aXR9aQ/m800x1200)
![mymapapp screenshot](https://obs.line-scdn.net/hx25_gHmWOxwuSigSahw8ZXQ4KiQtETRLN0lvKyomfCgiEjNDMRU9KSUleXhyFzdNZEdreConfi8jFyVKZxJsKyV2Kg/m800x1200)
![mymapapp screenshot](https://obs.line-scdn.net/hykFGTJcCOkVdUilLGQQ9PAcgfiNfDTVHRVthJ1k6fXdUW2hFRAxvK15qcCQFBzUaQ1BqIV5rcHdXByQTFAptclZuKA/m800x1200)