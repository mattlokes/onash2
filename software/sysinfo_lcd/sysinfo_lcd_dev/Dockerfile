FROM python:3.7-alpine

RUN apk add build-base linux-headers ethtool zlib-dev jpeg-dev freetype-dev

RUN pip3 install wheel luma.core luma.oled psutil
WORKDIR /app
COPY . /app

ENTRYPOINT exec /bin/sh -c "python3 sysinfo_lcd.py $SYSINFO_LCD_OPTS"

