

# Psutil - Monitoreo del sistema

Psutil ayuda a monitorear los parámetros de funcionamiento del sistema operativo y de sus procesos, tales como el uso de memoria, frecuencia de trabajo, uso de redes, sensores internos, etc. 

## Primeros pasos

El paquete se instala desde el gestor PIP.

```bash title="Instalación"
pip install psutil
```

El nombre de módulo coincide con el del paquete , por ello se lo importa directamente:

```python title="importacion"
include psutil
```


## Parámetros de Sistema

Para consultar parámetros del sistema *psutil* incluye un juego de *funciones*


### CPU

#### frecuencias

```py title="frecuencia procesadores"
frecuencia_procesadores = psutil.cpu_freq() 
```
Valores disponibles:
???+ info "Valores disponibles"

    | campo | valor |
    |:------------: | :---------------- |
    |***current***| frecuencia de trabajo actual (en MHz)|
    |***min***| frecuencia de trabajo mínima (en MHz)|
    |***max***| frecuencia de trabajo máxima (en MHz)|

Caso Linux, FreeBSD: pueden monitorearse todos los procesadores:

```py title="frecuencias- todos los procesadores"
lista_frecuencias = psutil.cpu_freq(percpu=True) 
```

#### nucleos

Cuenta cuantos núcleos (*cores*) dispone el CPU:

```py title="nº nucleos"
nucleos_logicos = psutil.cpu_count()
nucleos_fisicos = psutil.cpu_count(logical=False)
```


!!! hint "Hint: núcleos físicos y lógicos"


    La relación entre núcleos físicos y núcleos lógicos es:
    ```
    nucleos_logicos = nucleos_fisicos * threads_simultaneos 
    ```

    Ejemplo: un CPU con 2 núcleos físicos e *'HiperThreading'* de 2 hilos simultáneos por *core* da 4 núcleos lógicos.


#### cpu_percent()

Permite calcular el porcentaje de uso promedio de todos los núcleos del CPU :

```py title="porcentaje CPU"
# porcentaje de exigencia del CPU
porcentaje_total = psutil.cpu_percent(
    interval=None,                      # tiempo de referencia
    percpu=False                        #  resultado en lista de porcentajes , uno por *core* 
)  

```

<!-- Parámetros:

 - *interval:* tiempo de referencia
 - *percpu:* resultado en lista de porcentajes , uno por *core*  -->


Si no se indica un valor numérico para *interval* se toma de referencia la anterior llamada del método o en su defecto la importación del módulo. Es conveniente que entre ambas llamadas hayan pasado al menos 0.1 segundos para mejor precisión.

!!! example "Ejemplo: demanda de CPU de una rutina completa"

    ```py title="Porcentaje de CPU"
    #punto de referencia
    psutil.cpu_percent()  # retorna '0.0'-> IGNORAR
    # espera
    import time
    time.sleep(1)
    # medicion
    porcentaje = psutil.cpu_percent()               # promedio
    porcentajes = psutil.cpu_percent(percpu=True)   # por unidad
    ```



#### cpu_times()

Calcula los tiempos acumulados de procesamiento de cada núcleo lógico.

```py title="Tiempo procesamiento"
data_tiempos = psutil.cpu_times()     # informacion de tiempo de procesamiento en segundos
```
<!-- Campos más habituales: -->


??? info "Campos más habituales"

    | campo | valor |
    |:------------: | :---------------- |
    | **user**   | tiempo usado en modo usuario (segundos)|
    | **system** | tiempo usado en modo kernel (segundos) |


Más informacion sobre *cpu_times()*: [sitio oficial](https://psutil.readthedocs.io/en/latest/#psutil.cpu_times)





### Procesos


#### listado y verificacion
```py
lista_pids = psutil.pids()  # todos los PIDS activos encontrados
existe_proceso = psutil.pid_exists(pid) # verifica actividad
```

#### espera y eventos al cierre
```py
# Espera al cierre de procesos indicados
psutil.wait_procs(
    lista_pids,         # lista de numeros de IDs
    timeout=None,       # tiempo de espera máximo
    callback=None       # manejador asignable -> se dispara con cada cierre
    )
``` 

### Memoria RAM 


```py
data_ram = psutil.virtual_memory()
```

??? info  "Campos principales:"

    | campo | valor |
    |:------------: | :---------------- |
    |***total***| memoria RAM total (en bytes)|
    |***available***| memoria RAM actualmente disponible (en bytes)|
    |***percent***| porcentaje de memoria usado|

### Memoria SWAP

```py
data_swap = psutil.swap_memory()
```

??? info  "Campos principales:"

    | campo | valor |
    |:------------: | :---------------- |
    |***total***| memoria swap total (en bytes)|
    |***used***| memoria swap actualmente usado|
    |***free***| memoria swap libre|
    |***percent***| porcentaje de memoria swap usado|
    |***sin***| data escrita en disco (acumulativa)|
    |***sout***| data leida en disco (acumulativa)|




### Discos

#### particiones

```py
particiones_físicas = psutil.disk_partitions() # lista de particiones

for particion in particiones:
    print(particion)
```
???+ info  "Contenido de listas:"

    | campo | valor |
    |:------------: | :---------------- |
    | ***device*** | ruta del dispositivo: 'C:\\', '/dev/hda1', etc  |
    | ***mountpoint*** | ruta montada_ '/', '/home', 'D:\\', etc |
    | ***fstype*** | formato: NTFS, FAT, ext4, etc |
    | ***opt*** | informacion extra (dependiente del SO) |



#### espacio en disco

```py
uso_disco = psutil.disk_usage(ruta)
```
???+ info  "Contenido:"

    | campo | valor |
    |:------------: | :---------------- |
    | ***used***  |  espacio usado (en bytes)   |
    |  ***free*** |  espacio libre (en bytes)  |


!!! example "Ejemplo: estadísticas del disco o particion"

    ```py title="espacio en disco eb GiB"
    ruta = "/"
    uso_disco = psutil.disk_usage(ruta)
    espacio_usado = uso_disco.used    # espacio usado (en bytes)
    espacio_libre = uso_disco.free    # espacio libre (en bytes)
    print(f"Ruta: {ruta}")
    print(f"Espacio usado: {espacio_usado / (1000**3):.4} GiB") 
    print(f"Espacio libre: {espacio_libre / (1000**3):.4} GiB") 
    ```

#### estadisticas de lectura/escritura

Las estadísticas de lectura y escritura se calculan con la *función disk_io_counters()*:

```py
data_io = psutil.disk_io_counters()
```

??? info  "Campos más importantes"

    | campo | valor |
    |:------------: | :---------------- |
    | ***read_count***  |  Nº operaciones lectura   |
    |  ***write_count*** |  Nº operaciones escritura  |
    | ***read_bytes***  |  data total leida (en bytes)   |
    |  ***write_bytes*** |  data total escrita (en bytes)  |


La información puede fragmentarse por partición con ayuda del argumento ***perdisk***:

```py
lista_data_io = psutil.disk_io_counters(perdisk=True)
```

### Uso de red

#### estadisticas globales

La información se condensa con la ***función net_io_counters()***:

```py
io_global = psutil.net_io_counters()
```

Datos disponibles:


??? info "Campos disponibles"
    | campo  | valor |
    | :----  | :--- |
    | bytes_sent      | bytes enviados|
    | bytes_recv      | bytes recibidos|
    | packets_sent    | paquetes enviados|
    | packets_recv    | paquetes recibidos|
    | errin           | errores enviados|
    | errout          | errores recibidos|
    | dropin          | paquetes descartados enviados|
    | dropout         | paquetes descartados recibidos|









!!! example "Ejemplo de uso: medicion del uso de datos por red"
    ```py title="Data de red en MB"
    # Uso de red
    io_global = psutil.net_io_counters()
    enviados = io_global.bytes_sent
    recibidos = io_global.bytes_recv
    print("Uso de red")
    print(f"Datos enviados: {enviados/(1024**2):.4} MB") 
    print(f"Datos recibidos: {recibidos/(1024**2):.4} MB")
    ```


#### configuracion local


Data de direcion MAC, IP's, etc: función ***net_if_addrs()***

```py
data_equipo = psutil.net_if_addrs()   
```
#### canales

Estado de conexiones, velocidades de transmisión, tipos de transmisión, etc: función ***net_if_stats()*** 

```py
data_canales = psutil.net_if_stats()  
```

#### estadísticas (por canal)

Información de conexiones de socket local y remoto: IP's, puertos, tipo de socket, etc.

```py
lista_conexiones = psutil.net_if_stats()  
```

### Sensores y ventiladores

<!-- #### temperaturas -->

```py title="Temperaturas"
# temperaturas del sistema en grados Celsius salvo indicacion contraria
data_temperatura = psutil.sensors_temperatures(fahrenheit=False)  
```

<!-- #### ventiladores -->

```py title="Ventiladores"
# velocidad de ventiladores en RPM
data_ventiladores = psutil.sensors_fans()    # '{}' si no hay información
```


<!-- #### bateria -->
```py title="Batería"
data_bateria = psutil.sensors_battery() # 'None' si no se detecta
```


## Procesos específicos

La data de proceso se gestiona con la ***clase Process***:
```py
proceso  = psutil.Process()     # proceso actual
proceso  = psutil.Process(pid)  # PID especificado
```
Esta clase asigna una serie de métodos para obtener la inforncion relevante del proceso: uso de memoria, procesamiento de CPU, conexiones IP, etc.

### Estadisticas de memoria

El método ***memory_info()*** da información sobre el consumo de memoria del proceso actua:

```py
info_memoria = proceso.memory_info()
```

Campos más comunes:
???+ info "Campos más habituales"
    |campo| información|
    |:---:|:---|
    | **rss**    | uso de RAM en bytes    |
    | **vms**    | uso de SWAP en bytes   |


Ejemplo de uso: uso de memoria por el proceso actual

```py
proceso  = psutil.Process() 
info_memoria = proceso.memory_info()
info_memoria.rss    # uso de RAM en bytes
info_memoria.vms    # uso de SWAP en bytes
```

Estos campos son comunes para todos los sistemas operativos implementados. Los otros campos de información tienen nombres y disponibilidad que dependen del sistema operativo anfitrión. 

Ver más información sobre *memory_info()*: [sitio oficial](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info)   


### Estadisticas del procesamiento

Estado del proceso, núcleo ejecutante y núcleos habilitados para ejecutar:

```py
proceso.status()        # estado actual
proceso.cpu_num()       # Nº procesador ejecutando el proceso
proceso.cpu_affinity()  # Nº procesadores habilitados para ejecutar este proceso
```

#### Prioridad del proceso

La prioridad de los procesos son números que el sistema operativo tiene en cuenta a la hora de repartir el tiempo de ejecución de los núcleos del CPU entre los procesos activos.

La prioridad del proceso actual es accesible y modificable con el método ***nice()***:
```py
numero_prioridad = proceso.nice()    # lectura
proceso.nice(numero_prioridad)       # escritura
```
En UNIX el valor va típicamente desde -20 (prioridad máxima) a 20(prioridad mínima).


#### cpu_percent()

Permite calcular el porcentaje de uso de todos los CPUs por el programa actual (puede superar el 100%):

```py
# porcentaje de exigencia del CPU
porcentaje_total = proceso.cpu_percent(interval=None, percpu=False)  #  (desde ultimo llamado)
```
Parámetros
 - *interval:* tiempo de referencia
 - *percpu:* resultado en lista de porcentajes , uno por *core* (V6 en adelante)

Si no se indica un valor numérico para *interval* se toma de referencia la anterior llamada del método o en su defecto la importación del módulo. Es conveniente que entre ambas llamadas hayan pasado al menos 0.1 segundos para mejor precisión.

!!! example "Ejemplo uso: demanda de CPU de una rutina completa"

    ```py title="Porcentaje CPU del proceso"
    #punto de referencia
    proceso.cpu_percent()  # retorna '0.0'-> IGNORAR
    #procesamiento
    Rutina()
    # medicion
    porcentaje = proceso.cpu_percent()   
    ```

#### cpu_times()

Calcula los tiempos acumulados de procesamiento que demandó el proceso desde su inicio hasta el presente.
```py
data_tiempos = proceso.cpu_times()     # informacion de tiempo de procesamiento en segundos
```
Campos más habituales:
???+ info "Campos más habituales"
    | campo | valor |
    |:------------: | :---------------- |
    | **user**   | tiempo usado en modo usuario (segundos)|
    | **system** | tiempo usado en modo kernel (segundos) |

Más informacion sobre *cpu_times()*: [sitio oficial](https://psutil.readthedocs.io/en/latest/#psutil.cpu_times)

### Arbol de procesos

```py
# Identificador (ID)
pid  = proceso.pid             # ID del proceso 
ppid = proceso.ppid()          # ID del proceso padre 

# data 
data_padre   = proceso.parent()     # proceso padre
lista_padres = proceso.parents()    # lista de procesos "padres"/"abuelos"/etc
lista_hijos  = proceso.children(recursive=False)  # lista de procesos hijos
```

### Hilos (*threads*)

```py
# hilos
data_hilos = proceso.threads()       # informacion de los hilos 'namedtuple'
nro_hilos  = proceso.num_threads()   # numero hilos
```

### Ruta de programa

```py
ruta_programa   = proceso.cwd()           # directorio del programa
```

### Archivos

Da informacion de los archivos afectados por el proceso:
```py
# archivos abiertos
lista_archivos = proceso.open_files()    
```

???+ info "Campos habituales"
    | campo | valor |
    |:------------: | :---------------- |
    | **path** |   ruta de archivo   |
    | **fd**   | nº descriptor  (-1 en Windows)|

[Más sobre *open_files()*]()

### Variables de entorno
```py
# diccionario con variables de entorno
lista_archivos = proceso.environ()    
```


### Usuario y Grupo

```py
nombre_usuario = proceso.username()     # usuario actual
data_usuario = proceso.uids()           # informacion de usuario 
data_usuario = proceso.gids()           # informacion de grupo
```

### Conexiones IP

Da información de los ***sockets*** ("zócalos" de conexión) creados por el proceso para las conexiones:
```py
# información de sockets usados - lista de 'namedtuple'
lista_sockets = proceso.net_connections()       # V > 0.6.0
lista_sockets = proceso.connections()           # V < 0.6.0
```
El resultado es una **lista** de estadisticas de cada socket. Cada una incluye:

???+ info "Campos disponibles"
    |campo| información|
    |:---:|:---|
    |  **fd**      | descriptor del socket |
    | **ladr**      | rutas IP del sistema |
    | **radr**      | ruta IP del destinatario |
    | **family**    | versión de rutas IP ("familia"): IPv4, IPv6, etc |
    |   **type**    | tipo de dirección: TCP / UDP / etc |
    | **status**    | estado de la conexión |   

Más información sobre *net_connections()*: [sitio oficial](https://psutil.readthedocs.io/en/latest/#psutil.Process.net_connections)


### Manejo de señales


!!! info "Métodos disponibles"

    |  método | señal equivalente  | uso |
    |  :---: | :---:  |  :--- |
    | send_signal( nro_signal) | {SIG}  |  le envía una señal  al proceso     |
    | suspend() | SIGSTOP  | suspende el proceso (lo deja en espera)  |
    | resume() | SIGCONT  |  reanuda el proceso     |
    | wait(timeout=None) | ---  |  espera al cierre, tiempo de expiración en segundos     |      
    | terminate() | SIGTERM  | termina  el proceso    |
    | kill() | SIGKILL  |  mata el proceso     |




!!! example "Ejemplo: ordenar el cierre de un proceso y esperar a su cumplimiento"

    ```py title="Cerrar por PID"
    proceso = psutil.Process(nro_pid)
    proceso.terminate()
    proceso.wait()          # espera indefinidamente de ser necesario
    ```




## Referencias

[Readthedocs - Documentacion oficial](https://psutil.readthedocs.io/en/latest/#)

[Codigos Python - Monitoreo del sistema con Psutil en python](https://codigospython.com/monitoreo-del-sistema-con-psutil-en-python/)