# dyyoutube-2
Este proyecto permite descargar videos individuales y listas, desde youtube, además puede convertir los videos de youtube de formato mp4 a formato mp3

Si se quiere instalar el proyecto, hay que considerar que la librería pytube puede presentar un error del tipo "AttributeError: 'NoneType' object has no attribute 'span"

1.-La solución encontrada a esto es la siguiente:

En el archivo cipher.py se debe realizar el siguiente cambio al código: def get_throttling_function_name(js: str) -> str: """Extract the name of the function that computes the throttling parameter.

:param str js: The contents of the base.js asset file. :rtype: str :returns: The name of the function used to compute the throttling parameter. """ function_patterns = [ # ytdl-org/youtube-dl#29326 (comment) # a.C&&(b=a.get("n"))&&(b=Dea(b),a.set("n",b))}}; # In above case, Dea is the relevant function name r'a.[A-Z]&&(b=a.get("n"))&&(b=([^(]+)(b)', ] logger.debug('Finding throttling function name') for pattern in function_patterns: regex = re.compile(pattern) function_match = regex.search(js) if function_match: logger.debug("finished regex search, matched: %s", pattern) function_name = function_match.group(1) is_Array = True if '[' or ']' in function_name else False if is_Array: index = int(re.findall(r'\d+', function_name)[0]) name = function_name.split('[')[0] pattern = r"var %s=[(.*?)];" % name regex = re.compile(pattern) return regex.search(js).group(1).split(',')[index] else: return function_name

raise RegexMatchError( caller="get_throttling_function_name", pattern="multiple"

La referencia a esta solucion la encontrara en https://stackoverflow.com/questions/70976489/pytube-nonetype-object-has-no-attribute-span

2.-Además se debe cambiar el siguiente código en el archivo de la librería pytube parser.py

cambiar estas líneas

152: func_regex = re.compile(r"function([^)]+)")

por esta

152: func_regex = re.compile(r"function([^)]?)")

La referencia a este cambio lo encontrará en https://stackoverflow.com/questions/70060263/pytube-attributeerror-nonetype-object-has-no-attribute-span

Además es importante destacar, que dentro del proyecto se debe cambiar la ruta de descargas por su propia ruta.
