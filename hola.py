import os

def main():
    nombre = os.getenv("USERNAME")
    print("Hola mundo, no se baña: {}".format(nombre))
    
if __name__ == "__main__":
    main()