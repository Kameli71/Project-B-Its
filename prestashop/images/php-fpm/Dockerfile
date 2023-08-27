FROM php:fpm

RUN apt-get update

RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev
RUN apt-get install -y docker-php-ext-install -j$(nproc) iconv mcrypt pdo pdo_mysql zip
RUN apt-get install -y docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN apt-get install -y docker-php-ext-install -j$(nproc) gd

RUN apt-get install -y libicu-dev && docker-php-ext-install -j$(nproc) intl