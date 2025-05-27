import time
import os

#MENSAJE DE BIENVENIDA
print('''
!Bienvenido/a a NotFeik!
      ''')
time.sleep(1)
os.system('cls')
try:
    c1=int(input("¿Quieres ver las noticias en la app o en una red social? 1.-RRSS 2.-APP: "))
except ValueError:
    print("Ingresa solamente 1 o 2")

while True:
    try:
        if c1==1:
            #Redes sociales
            op=int(input('''
                    ¿A qué red social quiere ir?
                    1.-Facebook
                    2.-Instagram
                    3.-Tiktok
                    4.-Twitter/X
                    5.-Salir
                    '''))
            match op:
                case 1:
                    print("Será redirigido/a a nuestro perfil de facebook: https://www.facebook.com/?locale=es_LA")
                case 2:
                    print("Será redirigido/a a nuestro perfil de Instagram: https://www.instagram.com/")    
                case 3:
                    print("Será redirigido/a a nuestro perfil de Tiktok: https://www.tiktok.com/es/")   
                case 4:
                    print("Será redirigido/a a nuestro perfil de Twitter/X: https://x.com/")   
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Ingrese una opción válida")
                    op=int(input())
        elif c1==2:
            #Noticias desde la app
            op2=int(input("¿Quieres ver noticias 1.-nacionales o 2.-internacionales? "))
            match op2: 
                case 1:
                    print("Quieres ver noticias 1.-positivas o 2.-negativas?")
                    op3 = int(input())
                    match op3:
                        case 1:
                            print('''
                        Noticias Positivas del pais!
                        1.- Estudiante destacado: https://www.biobiochile.cl/noticias/ciencia-y-tecnologia/ciencia/2025/05/23/estudiante-chileno-logro-1-lugar-en-feria-cientifica-internacional-creo-filtro-purificador-de-aire.shtml
                        2.- Animales: https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2025/04/23/condor-nace-en-zoologico-de-quilpue-especie-esta-en-peligro-de-extincion.shtml
                        3.- Chilena historica WWE: https://www.biobiochile.cl/noticias/deportes/mas-deportes/2025/02/15/no-se-cansa-de-hacer-historia-stephanie-vaquer-gana-titulo-y-es-la-primera-chilena-campeona-en-wwe.shtml
                        ''')
                            break
                        case 2:
                            print('''
                        Noticias Negativas del pais!
                        1.- Medicina: https://www.elmostrador.cl/noticias/pais/2025/05/26/removido-director-del-h-san-jose-denuncio-670-funcionarios-que-suman-hasta-14-anos-de-licencias/
                        2.- Accidente: https://www.elmostrador.cl/noticias/pais/2025/05/26/al-menos-dos-muertos-deja-volcamiento-de-bus-en-la-ruta-5-sur-a-la-altura-de-san-fernando/
                        3.- MedioAmbiente: https://www.24horas.cl/regiones/zona-sur/los-lagos/video-dron-destruccion-tornado-puerto-varas
                        ''')
                            break
                        case _:
                            print("Ingrese una opción válida")
                    op=int(input())
                case 2:
                    print("Quieres ver noticias 1.-positivas o 2.-negativas?")
                    op3 = int(input())
                    match op3:
                        case 1:
                            print('''
                            Noticias Positivas del mundo:
                        1.- Nuevo Papa: https://www.france24.com/es/europa/20250525-el-papa-le%C3%B3n-xiv-toma-posesi%C3%B3n-de-san-juan-de-letr%C3%A1n-como-obispo-de-roma
                        2.- Deportes: https://as.com/futbol/champions/psg-inter-tv-horario-donde-y-como-ver-la-final-de-la-champions-league-online-n/
                        3.- Salud: https://lacarabuenadelmundo.com/dos-adolescentes-ganan-el-premio-de-la-tierra-2025-por-su-innovador-purificador-de-agua/
                        ''')
                            break
                        case 2:
                            print('''
                        Noticias Negativas del mundo!
                        1.- Crisis Venezuela: https://www.bbc.com/mundo/articles/c0m9jw3kej7o 
                        2.- Muertes en Gaza https://elpais.com/expres/2025-05-24/israel-mata-al-menos-a-60-personas-en-las-ultimas-24-horas-en-gaza.html
                        3.- Guerra: https://elpais.com/internacional/2025-05-26/rusia-recrudece-los-bombardeos-para-desmoralizar-a-ucrania-y-debilitar-sus-defensas-antiaereas.html
                        ''')
                            break
                        case _:
                            print("Ingrese una opción válida")
                case 3:
                    print("Salir")
                    break
        else:
            print("Ingrese una opción válida") 
    except ValueError:
        print("Ingrese una opción válida: 1 - 2")


