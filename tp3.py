import sys
import time

from common.graph_generator import main as gen_main
from mc_karger.main import main as kg_main

USAGE = '''
Instrucciones de uso:
        *  -gen <n> <name>    Genera un grafo conexo no dirigido de <n> vertices y 2*<n> aristas. Los almacena en el archivo <name>.txt

        *  -kg <name>         Ejecuta el algoritmo de Karger para encontrar el corte minimo del grafo <name>        
        '''


def main(argc, argv):
    print("-------TDA TP3-------")
    if argc < 2:
        print(USAGE)
        return

    print(argv)
    ej, params = argv[1], argv[2:]
    if ej == "-gen":
        n, file_name = params
        print("Generando Grafo")
        return measure_time(gen_main, (int(n), file_name))

    if ej == "-kg":
        print(argv)
        file_name = params
        print("DIJKSTRA")
        return measure_time(kg_main, file_name)


def measure_time(f, n):
    start = time.perf_counter()
    f(n)
    end = time.perf_counter()
    print("Tiempo de ejecución:     {:.5f} segundos".format(end - start))
    # print("{:.5f}".format(end - start).replace('.', ','))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
