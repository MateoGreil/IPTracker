#!/bin/bash

PUBLIC_IP_FILE=/home/mat/IPTracker/.ip
PUBLIC_IP=`wget http://ipecho.net/plain -O - -q ; echo`
NOW=date +"%m-%d-%Y %H:%M:%S"

read last_ip < $PUBLIC_IP_FILE
if [ $last_ip != $PUBLIC_IP ]
then
	echo "L'ip a change de " + $last_ip + " vers " + $PUBLIC_IP
	sendemail -l ~/email.log -f ${MAIL_FROM} -u "L'ip de l'appart a change !" -t ${MAIL_TO} -s "smtp.gmail.com:587"  -o tls=yes -xu ${MY_EMAIL} -xp ${MY_EMAIL_PASSWORD} -m "Attention ! N'utilise plus : " $last_ip ". Voici la nouvelle adresse : " $PUBLIC_IP

	echo $PUBLIC_IP > $PUBLIC_IP_FILE
else
	echo $NOW 'Pas de difference'
fi
