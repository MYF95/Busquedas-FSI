# Busquedas-FSI
Práctica de búsquedas de FSI

Primera tarea:

A partir del código base entregado, se deberá programar el método de ramificación y
acotación. Utilícese como problema el grafo de las ciudades de Rumanía presente en
el código.
• Comparar la cantidad de nodos expandidos por este método con relación a los
métodos de búsqueda primero en anchura y primero en profundidad.
• Realizar a mano la traza de una búsqueda.

La primera tarea está en la versión 1.0, donde se ha implementado en 'utils.py'
"SortedFIFOQueue" y en search.py "sorted_graph_search"

Segunda tarea:

A partir del código base entregado, se deberá programar el método de búsqueda
ramificación y acotación con subestimación. Utilícese como problema el grafo de las
ciudades de Rumanía presente en el código. Como heurística se utilizará la distancia
en línea recta entre cada estado y el estado final.
• Comparar la cantidad de nodos expandidos por este método con relación a los
métodos de búsqueda primero en anchura, primero en profundidad y ramificación y
acotación.
• Demostrar con un ejemplo hecho a mano que si la heurística no fuera consistente no
se aseguraría el carácter óptimo de la búsqueda 

Version 1.1:
Se han hecho modificaciones en search.py, sumando un metodo adicional a la clase base h para poder
acceder a la h desde la instancia de problema