#! /bin/bash
#archivo del que leo las IP a controlar
N_Hosts=$(wc hostsOK.txt | awk {'print $1'})

#defino el array con las IP
typeset Nodos[$N_Hosts]

#llenamos el array
i=0;
while read line
do
 Nodos[$i]=$(echo $line | awk {'print $1'})
 i=$i+1
done < hostsOK.txt

#construyo el comando a ejecutar
comando="fping "
comandoCompleto=$comando${Nodos[*]}

#ejecución del comando
$comandoCompleto | sed 's/is alive/está respondiendo/g' | sed 's/is unreachable/está caído/g' > output.txt
awk 'NR==FNR{a[$1]=$2;next}{$1=a[$1]}1' hostsOK.txt output.txt > resultados.txt
rm output.txt
