import gobject
import time

def process_a():
    print("[process_a]:", time.time(), "\n")
    return True

def process_b():
    print("[process_b]:", time.time(), "\n")
    return True

if __name__ == '__main__':
    try:
        loop = gobject.MainLoop()
        gobject.timeout_add(500, process_a)    # toutes les 500 ms
        gobject.timeout_add(1000, process_b)   # toutes les 1000 ms
        loop.run()
    except KeyboardInterrupt:
        print("Fin du programme\n")
