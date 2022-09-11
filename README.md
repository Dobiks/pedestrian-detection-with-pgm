# Tracking przechodniów z użyciem FactorGraph

## Cel
Celem projektu było stworzenie systemu pozwalającego na śledzenie przechodniów ujetych na ulicznej kamerze. Dataset złożony był z pojedynczych klatek filmu oraz z koordynatów bounding boxów, wskazujących pozycje przechodniów na obrazie kamery. 

## Działanie 

Klasa ImageLoader sortuje listę zdjęć z folderu <em>frames</em>, a następnie parsuje plik <em>bboxes.txt</em> zawierający dane o bounding boxach. Para zdjęcie-bbox zostaje zwrócona i następnie na jej podstawie zostaje utworzona lista klas Pedestrian. Liczba obiektów listy odpowiada liczbie przechodniów znajdujących się na obecnej klatce filmu. Klasa Pedestrian zawiera pola:\
<em>image</em> - zmienna zawierająca zdjecie przechodnia.\
<em>histograms</em> - lista zawierająca histogramy wykonane na kanałach r,g,b,h,s,v.\
<em>id</em> - zmienna string zawierająca numeryczne id przechodnia. Id jest unikalne dla każdej klatki filmu.\
Do każdego z powyższych pól napisane zostały gettery umożliwiające dostęp do wartości zmiennych.
Klasa zawiera również logikę wykonanywaną w poniższych metodach:\
__create_image - wycięcie obrazu przechodnia z klatki filmu.\
__create_histograms - zwraca histogramy w kanałach r,g,b,h,s,v.

Następnie do metody create klasy GraphCreator przekazana zostaje lista Pedestrians z obecnego zdjęcia oraz lista Pedestrians z poprzedniej klatki. Dla każdego przechodnia tworzony jest węzeł o nazwie zawierającej id przechodnia. Tworzony jest również wektor o rozmiarze równym liczbie przechodniów z poprzedniej klatki powiększonym o  1. Wektor ten zawiera prawdopodobieństwo pojawienia się nowej osoby oraz prawdopodobieństwa identyfikacji osób z poprzedniego zdjęcia i jest dodawany do grafu jako współczynnik połączony z węzłem przechodnia. 
Następnie z pomoca metody __get_matrix tworzona jest macierz o wymiara MxM gdzie M równe jest liczbie przechodniów z poprzedniej klatki + 1. Macierz ta zapobiega przypisaniu więcej niż jednej osoby z aktualnej klatki do osoby z klatki poprzedniej. Jeżeli występuje więcej niż jeden przechodzień powstałe węzły są ze sobą łączone, a jako współczynniki między nimi wykorzystywana jest powyższa macierz.
Następnie użyta jest funkcja BeliefPropagation, a jej wynik przekształcony zostaje w słownik. Value każdego elementu słownika zostaje pomniejszone o 1 i zwrócony zostaje wynik w postaci stringa.
