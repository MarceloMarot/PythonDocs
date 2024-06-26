

# Traducciones - python-i18n

## python-i18n

i18n es una abreviación de 'InternationalizatioN' (18 letras entre la I y la N). **python-i18n** es es una de las múltiples implementaciones de Python para las traducciones i18n.


## Instalación

i18n se instala fácilmente desde PIP:

```bash title="instalación"
pip install python-i18n
```

Si se prefiere guardar las traducciones en formato YAML el paquete requerido es el siguiente:

```bash title="instalacion (con soporte YAML)"
pip install python-i18n[YAML]
```


## Importación

El paquete debe importarse para su uso:
```python title="importación"
import i18n
```


## Traduccion desde script

Las traducciones se pueden cargar con la función `add_tranlation()` en forma de pares *campo - valor*, ambos en formato *string*:

```python title="Crear traducción"
i18n.add_translation('hello','hola')
```
en tanto que las traducciones se realizan con la función `t()`:

```python hl_lines="2" title="Leer traducción"
campo = 'hello'
traducido = i18n.t(campo)
print(traducido)
```
Para cada par campo-valor se puede asignar una abreviación de lenguaje, de modo de permitir soporte simultáneo a múltiples idiomas:
```python title="Traducciones en varios idiomas"
i18n.add_translation('hello','good morning', locale='en')   # 'en' : inglés (english) 
i18n.add_translation('hello','buenos días', locale='es')    # 'es' : español
```

Las etiquetas 'es' y 'en' son etiquetas de idioma definidas por el desarrollador. Éstas no vienen predefinidas por el paquete, aunque convencionalmente se usan las abreviaciones en inglés de los lenguajes. 


##  Set y Fallback

El lenguaje prioritario se establece on la función *set()*:
```python title="Lenguaje preferido: set"
# Lenguaje preferido
i18n.set('locale', 'es')   # español
```
en tanto que la opción alternativa se establece con la función *fallback()*:

```python title="Lenguaje de respaldo: fallback"
# alternativa : 'fallback'
i18n.set('fallback', 'en')  # inglés
```

Esto permite completar los campos para los cuales no existan traducciones en el lenguaje preestablecido. Como alternativa habitualmente se elige el inglés.


## Traduccion desde archivos YML

Las traducciones se guardan en archivos YML en una misma carpeta. El directorio se carga con el método `append()` de la función `load_path()`: 

```python title="Carpeta de traducciones"
# directorio con traducciones
i18n.load_path.append('.')        # directorio actual
i18n.load_path.append('local/')   # subdirectorio llamado 'local'
```

Los archivos YML tienen en su nombre un nombre de espacio (*namespace*), la abreviación del idioma (*locale*) y el formato del archivo (*format*):

``` title="formato de nombres de archivo"
{namespace}.{locale}.{format}
```

Ejemplo: archivo para el inglés con los campos 'hi' y 'gb'
```yml title="traduccion al inglés"
# archivo 'foo.en.yml' (inglés)
# carpeta 'local'
en: 
  hi: Hello Word!
  gb: Goodbye!
```
Ejemplo: archivo para el español con el campo único 'hi'
```yml title="traduccion al español"
# archivo 'foo.es.yml' (español)
# carpeta 'local'
es: 
  hi: Hola Mundo!
    # campo 'gb' faltante
```
Las traducciones de estos archivos se cargan con el nombre del descriptor de archivo y el nombre del campo elegido. 

   
!!! example "Ejemplo: traducción faltante"
    Si se necesita la traduccion al inglés:

    ```python title="traduccion al inglés"
    # traducción al ingles
    i18n.set('locale', 'en')    
    traducido = i18n.t('foo.hi')
    print(traducido)   
    traducido = i18n.t('foo.gb')
    print(traducido) 
    ```

    Si en cambio se necesita la traduccion al español (incompleta):

    ```python title="traduccion al español (incompleta)"
    # traducción al español
    i18n.set('locale', 'es')    
    traducido = i18n.t('foo.hi')
    print(traducido)    
    #campo faltante
    traducido = i18n.t('foo.gb')
    print(traducido)    # resultado en ingles
    ```

    en este caso la traducción incluirá los campos faltantes en inglés, por ser éste el idioma alternativo elegido.

    Y si en cambio se necesita la traducción a un lenguaje no implementado, como por ejemplo el polaco:
    
    ```python title="traduccion al polaco (faltante)"
    # traducción al polaco (faltante)
    i18n.set('locale', 'pl')    
    traducido = i18n.t('foo.hi')
    print(traducido)   # resultado en ingles
    ```

    en este caso simplemente se muestra todo en inglés.



!!! info "subdirectorios y *namespaces*"

    Si los archivos de traducción se guardan en *subdirectorios* entonces los nombres de éstos también cuentan como *nombre de espacio*


## Placeholders

Se pueden implementar parámetros (campos variables) dentro de las traducciones, éstos son llamados ***placeholders*** o *marcadores*:
```python title="placeholders: formato"
# campo 'name' variable 
i18n.add_translation('hi', 'Hola %{name} !')
```

Los parámetros variables se asignan como argumento para la función *t()* en el momento de traducir:
```python title="placeholders: asignación"
traducido = i18n.t('hi', name='Bob')    # 'Hola Bob!'
```

## Pluralizacion

El ***placeholder***, si éste tiene valor numérico, puede usarse para elegir entre varias traducciones posibles.

El valor numérico se pasa con la propiedad `count`. Las opciones de traducción se enmarcan entre llaves y hay cuatro opciones:

|  Opcion |   Valor   |
|:------:|:-----:|
| `zero` |     0     |
| `one`  | 1         |
| `few`  | 2 a 5     |
| `many` | 6 o mayor |

Ejemplo: conteo de emails

```python title="pluralización: formato"
i18n.add_translation('numero', {
    'zero': 'No tienes ningún correo.',
    'one': 'Tienes un nuevo correo.',
    'few': 'Sólo tienes %{count} correos.',
    'many': 'Tienes %{count} correos nuevos.'
})
```
La lectura de la traducción se hace asignándole el valor a la propiedad *count*:

```python title="pluralización: uso"
print( i18n.t('numero', count=0) )  # caso 'zero'(0)
print( i18n.t('numero', count=1) )  # caso 'one' (1)
print( i18n.t('numero', count=5) )  # caso 'few' (2 a 5)
print( i18n.t('numero', count=6) )  # caso 'many' (6 o mayor)
```



## Traduccion desde archivos JSON

Los archivos JSON deben ser habilitados para ser leidos por el paquete:
```python title="habilitación archivos JSON"
# habilitar JSON
i18n.set('file_format', 'json')
```

<!-- ## 'skip locale from root' -->

Los archivos de traducciones no siempre traen internamente indicado el campo *locale* (idioma).
Para estos casos se habilita la opción *'skip_locale_root_data'*:

```python title='skip locale from root'
i18n.set('skip_locale_root_data', True)
```
## Ejemplo aplicado - Lectura JSON

Archivo JSON de traducciones al inglés, carpeta 'local':
```JSON title="archivo de traducción al inglés"
// archivo inglés: 'foo.en.json'
// carpeta 'local'
{
   "key-1": "Welcome %{firstname} %{lastname}!",
   "key-2": "Good morning!",
   "key-3": "Bye!"
}
```
Archivo JSON de traducciones al español, carpeta 'local':
```JSON title="archivo de traducción al español"
// archivo español: 'foo.es.json'
// carpeta 'local'
{
    "key-1": "Bienvenido %{firstname} %{lastname}!",
    "key-2": "Buenos días!",
    "key-3": "Adiós!"
}
```
Código de aplicación:

```python title="rutina de traducción"
i18n.set('file_format', 'json')

i18n.load_path.append('local/')

i18n.set('fallback', 'en')  # Ultima opcion
i18n.set('skip_locale_root_data', True)


# prueba español
i18n.set('locale', 'es')  
print( i18n.t('foo.key-1',firstname='Aitor', lastname='Tilla'))
print( i18n.t('foo.key-2'))
print( i18n.t('foo.key-3'))

# prueba español
i18n.set('locale', 'en')  
print( i18n.t('foo.key-1',firstname='Aquiles', lastname='Brinco'))
print( i18n.t('foo.key-2'))
print( i18n.t('foo.key-3'))
```

## Referencias

[Documentación oficial](https://pypi.org/project/python-i18n/)




