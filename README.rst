RU-CENTER DNS-Master backup
===========================

.. image:: https://img.shields.io/pypi/v/ru-center-backup.svg?style=flat-square
    :target: https://pypi.python.org/pypi/ru-center-backup



.. image:: https://img.shields.io/pypi/dm/ru-center-backup.svg?style=flat-square
        :target: https://pypi.python.org/pypi/ru-center-backup

Скрипт для бэкапа всех файлов зон из DNS-Master Ру-Центра в локальную директорию

Установка
---------

.. code:: bash

    pip install ru-center-backup

Использование
-------------

1.   Установить переменные окружения

    .. code:: bash

        export RUC_API=$(echo -n "<api_username>:<api_password>" | base64)
        export RUC_USER="123456/NIC-D"
        export RUC_PASS="qwerty"

2.   Запустить скрипт

    .. code:: bash

        ru-center-backup <output_dir>

    Если <output_dir> не существует - программа завершится с ошибкой.
    Если параметр <output_dir> опущен - файлы зон будут выведены на консоль (разделяется ;========= )
