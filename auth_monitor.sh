:#!/bin/bash

nginxNum=0
uwsgiNum=0

while true

do
    nginxNum=`ps -C nginx --no-header | wc -l`
    uwsgiNum=`ps -C uwsgi --no-header | wc -l`

    if [ $nginxNum -eq 0 ]; then
        sudo service nginx restart 
        sleep 30
        #echo "nginx"+$nginxNum
        #break
    fi

    if [ $uwsgiNum -eq 0 ]; then
        uwsgi --ini /usr/share/nignx/html/Auth/publicAuth/uwsgi.ini
        sleep 30
        #echo "uwsgi"+$uwsgiNum
    fi
    sleep 1

done
