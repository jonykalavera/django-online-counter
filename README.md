--------------
English
--------------

**easy_install django-online-counter**

or

**pip install django-online-counter**

command to install the application.

settings.py editing.

<pre>
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
</pre>

Next, **python manage.py syncdb** command to add the application.

Manual
--------

guest, users and total visitors is the three different results.

After selecting the appropriate location of your page;

**{{ request.online.total }}** - Total visitors

**{{ request.online.guest }}** - Total guests

**{{ request.online.users }}** - Total users


online visitors can see the writing.

--------------
Türkçe
--------------

**easy_install django-online-counter**

ya da

**pip install django-online-counter**

komutuyla uygulamayı yükleyebilirsiniz.

settings.py dosyasını aşağıdaki gibi düzenleyin.

<pre>
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
</pre>

Sonra, **python manage.py syncdb** komutu ile uygulamayı ekleyin.

Kullanım
--------

Misafir, kullanıcı ve toplam ziyaretçi olmak üzere üç farklı sonuç verir.

Sayfanızın uygun yerini seçtikten sonra;

**{{ request.online.total }}** - Toplam ziyaretçi

**{{ request.online.guest }}** - Toplam misafir

**{{ request.online.users }}** - Toplam kullanıcı

yazarak çevirimiçi ziyaretçileri öğrenebilirsiniz.