--------------
English
--------------

*easy_install django-online-counter*

or

*pip install django-online-counter*

command to install the application.

settings.py dosyasını aşağıdaki gibi düzenleyin.

MIDDLEWARE_CLASSES = (
    ...
    'onlinecounter.middleware.OnlineCounterMiddleware',
    ...
)


INSTALLED_APPS = (
    ...
    'onlinecounter',
    ...
)

Next, *python manage.py syncdb* command to add the application.

--------------
Türkçe
--------------

*easy_install django-online-counter*

ya da

*pip install django-online-counter*

komutuyla uygulamayı yükleyebilirsiniz.

settings.py dosyasını aşağıdaki gibi düzenleyin.

MIDDLEWARE_CLASSES = (
    ...
    'onlinecounter.middleware.OnlineCounterMiddleware',
    ...
)


INSTALLED_APPS = (
    ...
    'onlinecounter',
    ...
)

Sonra, *python manage.py syncdb* komutu ile uygulamayı ekleyin.

Kullanım
--------

Misafir, kullanıcı ve toplam ziyaretçi olmak üzere üç farklı sonuç verir.

Sayfanızın uygun yerini seçtikten sonra;

*{{ request.online.total }}* - Toplam Ziyaretçi
*{{ request.online.guest }}* - Toplam Misafir
*{{ request.online.users }}* - Toplam Kullanıcı

yazarak çevirim içi ziyaretçileri öğrenebilirsiniz.