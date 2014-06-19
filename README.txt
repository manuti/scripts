Puedes consultar la licencia en el blog:

http://raspberryando.wordpress.com/about/


Para el teclado español en XRDP

Solucionar la desconfiguración del teclado con xrdp
Deja un comentario
Como habréis visto los últimos días he estado tocando el tema de conectar de manera remota, ya sea mediante VNC o RDP, con otros equipos.

Quedaba pendiente un fleco, la configuración de la distribución del teclado, ya que con xrdp no se mapea bien y nos quedamos sin “ñ” y sin la mayoría de teclas que introducen símbolos.

Buscando en Internet el mapa de caracteres encontré un blog en el que ya tenían preparado el fichero del mapeo de teclado para un teclado español. El fichero (y el blog) es:

http://c-nergy.be/downloads/km-040a.ini

Para que funcione únicamente hay que ir a la carpeta con xrdp (/etc/xrdp/) y copiar allí el archivo “km-040a.ini“.
