# import logic.process as pro
import logic.search as indexsearch

def main():
    
    tweets=indexsearch.search("Ejercicio de educacion eficiente eficiente",10)
    print(tweets)

if __name__ == "__main__":
    main()
