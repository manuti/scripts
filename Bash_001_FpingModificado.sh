#! /bin/bash
echo -n “Pon las direcciones a continuación, separadas por una coma:”
read direcciones

IFS=”,” read -ra arr <<< “$direcciones”

#ejecución del comando
fping ${arr[*]} 2> /dev/null | sed -e ‘s/is alive/está respondiendo/g’ -e ‘s/is unreachable/no está respondiendo/g’
