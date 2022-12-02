#Создаем меню и создаем месседжи для пользователя, чтобы он знал об ошибках
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb

'''
from Node import *
from DijkstraNodeDecorator import *
from BinaryTree import *
from MinHeap import *
from Graph import *
'''

en_alphabet = "abcdefghijklmnopqrstuvwxyz"
last_alphabet_index = 0


"""
Классы
"""

class Node:
    def __init__(self, data, indexloc = None):
        self.data = data
        self.index = indexloc

class DijkstraNodeDecorator:
    
    def __init__(self, node):
        self.node = node
        self.prov_dist = float('inf')
        self.hops = []
 
    def index(self):
        return self.node.index
 
    def data(self):
        return self.node.data
    
    def update_data(self, data):
        self.prov_dist = data['prov_dist']
        self.hops = data['hops']
        return self

class BinaryTree:
 
    def __init__(self, nodes = []):
        self.nodes = nodes
 
    def root(self):
        return self.nodes[0]
    
    def iparent(self, i):
        return (i - 1) // 2
    
    def ileft(self, i):
        return 2*i + 1
 
    def iright(self, i):
        return 2*i + 2
 
    def left(self, i):
        return self.node_at_index(self.ileft(i))
    
    def right(self, i):
        return self.node_at_index(self.iright(i))
 
    def parent(self, i):
        return self.node_at_index(self.iparent(i))
 
    def node_at_index(self, i):
        return self.nodes[i]
 
    def size(self):
        return len(self.nodes)

class MinHeap(BinaryTree):
 
    def __init__(self, nodes, is_less_than = lambda a,b: a < b, get_index = None, update_node = lambda node, newval: newval):
        BinaryTree.__init__(self, nodes)
        self.order_mapping = list(range(len(nodes)))
        self.is_less_than, self.get_index, self.update_node = is_less_than, get_index, update_node
        self.min_heapify()
 
    # Изменение в кучу узлов, предполагается, что все поддеревья уже кучи
    def min_heapify_subtree(self, i):
 
        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)
        imin = i
        if( ileft < size and self.is_less_than(self.nodes[ileft], self.nodes[imin])):
            imin = ileft
        if( iright < size and self.is_less_than(self.nodes[iright], self.nodes[imin])):
            imin = iright
        if( imin != i):
            self.nodes[i], self.nodes[imin] = self.nodes[imin], self.nodes[i]
            # Если есть лямбда для получения абсолютного индекса узла
            # обновляет массив order_mapping для указания, где находится индекс
            # в массиве узлов (осмотр для этого индекса будет 0(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[imin])] = imin
                self.order_mapping[self.get_index(self.nodes[i])] = i
            self.min_heapify_subtree(imin)
 
 
    # Превращает в кучу массив, который еще ей не является
    def min_heapify(self):
        for i in range(len(self.nodes), -1, -1):
            self.min_heapify_subtree(i)
 
    def min(self):
        return self.nodes[0]
 
    def pop(self):
        min = self.nodes[0]
        if self.size() > 1:
            self.nodes[0] = self.nodes[-1]
            self.nodes.pop()
            # Обновляет order_mapping, если можно
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[0])] = 0
            self.min_heapify_subtree(0)
        elif self.size() == 1: 
            self.nodes.pop()
        else:
            return None
        # Если self.get_index существует, обновляет self.order_mapping для указания, что
        # узел индекса больше не в куче
        if self.get_index is not None:
            # Устанавливает значение None для self.order_mapping для обозначения непринадлежности к куче 
            self.order_mapping[self.get_index(min)] = None
        return min
 
    # Обновляет значение узла и подстраивает его, если нужно, чтобы сохранить свойства кучи
    def decrease_key(self, i, val):
        self.nodes[i] = self.update_node(self.nodes[i], val)
        iparent = self.iparent(i)
        while( i != 0 and not self.is_less_than(self.nodes[iparent], self.nodes[i])):
            self.nodes[iparent], self.nodes[i] = self.nodes[i], self.nodes[iparent]
            # Если есть лямбда для получения индекса узла 
            # обновляет массив order_mapping для указания, где именно находится индекс
            # в массиве узлов (осмотр этого индекса O(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[iparent])] = iparent
                self.order_mapping[self.get_index(self.nodes[i])] = i
            i = iparent
            iparent = self.iparent(i) if i > 0 else None
 
    def index_of_node_at(self, i):
        return self.get_index(self.nodes[i])

class Graph: 
    def __init__(self, nodes):
        self.adj_list = [ [node, []] for node in nodes ]
        for i in range(len(nodes)):
            nodes[i].index = i

    def add_node(self, node: Node):
        lastIndex = self.adj_list.__len__
        print(f"lastIndex = {lastIndex}")

        node.index = lastIndex
        self.adj_list.append([node, []])
    
    def show_graph(self):
        for i in self.adj_list:
            print(f"{i[0].data} -> {i[1]}")

    def connect_dir(self, node1, node2, weight = 1, cost = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        # Отмечает, что нижеуказанное не предотвращает от добавления связи дважды
        self.adj_list[node1][1].append((node2, weight))
 
    def connect(self, node1, node2, lenght = 1, cost = 1):
        self.connect_dir(node1, node2, lenght, cost)
        self.connect_dir(node2, node1, lenght, cost)
 
    def connections(self, node):
        node = self.get_index_from_node(node)
        return self.adj_list[node][1]
    
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index
 
    #Реализация алгоритма Дейкстры (поиска кратчайшего пути)
    def dijkstra(self, src):
        
        src_index = self.get_index_from_node(src)
        # Указывает узлы к DijkstraNodeDecorators
        # Это инициализирует все предварительные расстояния до бесконечности
        dnodes = [ DijkstraNodeDecorator(node_edges[0]) for node_edges in self.adj_list ]
        # Устанавливает предварительное расстояние исходного узла до 0 и его массив перескоков к его узлу
        dnodes[src_index].prov_dist = 0
        dnodes[src_index].hops.append(dnodes[src_index].node)
        # Устанавливает все методы настройки кучи
        is_less_than = lambda a, b: a.prov_dist < b.prov_dist
        get_index = lambda node: node.index()
        update_node = lambda node, data: node.update_data(data)
 
        # Подтверждает работу кучи с DijkstraNodeDecorators с узлами
        heap = MinHeap(dnodes, is_less_than, get_index, update_node)
 
        min_dist_list = []
 
        while heap.size() > 0:
            # Получает узел кучи, что еще не просматривался ('seen')
            # и находится на минимальном расстоянии от исходного узла
            min_decorated_node = heap.pop()
            min_dist = min_decorated_node.prov_dist
            hops = min_decorated_node.hops
            min_dist_list.append([min_dist, hops])
            
            # Получает все следующие перескоки. Это больше не O(n^2) операция
            connections = self.connections(min_decorated_node.node)
            # Для каждой связи обновляет ее путь и полное расстояние от 
            # исходного узла, если общее расстояние меньше, чем текущее расстояние
            # в массиве dist
            for (inode, weight) in connections: 
                node = self.adj_list[inode][0]
                heap_location = heap.order_mapping[inode]
                if(heap_location is not None):
                    tot_dist = weight + min_dist
                    if tot_dist < heap.nodes[heap_location].prov_dist:
                        hops_cpy = list(hops)
                        hops_cpy.append(node)
                        data = {'prov_dist': tot_dist, 'hops': hops_cpy}
                        heap.decrease_key(heap_location, data)
        return min_dist_list


#Установка и Подключение библиотеки Networkx, с помощью которой рассчитываем критический путь
import networkx as nx
import matplotlib.pyplot as plt
def oprogramme():
  opragramme = Tk()
  opragramme.geometry("1100x300")
  okno = Label(opragramme, text = "При запуске моей программы, Вы можете увидеть большую часть занимает поля Canvas, а левая часть несет 5 кнопок.", font = ("Arial", 13))
  okno0 = Label(opragramme, text = "Нажав на каждую, вы сможете сделать такие действия: Выход - выйти из программы, об Авторе - создатель, ", font = ("Arial", 13))
  okno1 = Label(opragramme, text = "Рассчитать критический путь - нажимается, в том случаи если Вы указали смежность и вес, создали при этом создали вершины, ", font = ("Arial", 13))
  okno11 = Label(opragramme, text = "Правила ввода - правильность ввода в окне Ввод связей и ребер, первая кнопка данный пункт.", font = ("Arial", 13))
  okno2 = Label(opragramme, text = "При работе с полем Canvas вы левой кнопкой мыши + левый Control , создаете Вершины которые имеют нумерацию, ", font = ("Arial", 13))
  okno22 = Label(opragramme, text = "правой кнопкой первый раз нажав на вершину и еще раз правой кнопкой нажав на другую вершину - вы создаете дугу, ", font = ("Arial", 13))
  okno3 = Label(opragramme, text = "После создание появляется окно Вввод связей ребер и вес вершин, там будет 3 поля ввода, где в первых двух Вы обязаны указать, ", font = ("Arial", 13))
  okno33 = Label(opragramme, text = "те 2 вершины, которые вы соединили, а в 3 поле указать вес, вес если равен 0 - фиктивность, если вы пытаетесь", font = ("Arial", 13))
  okno4 = Label(opragramme, text = "создать цикл, то когда вы соединете вторую линию в первую вершину, то выдаст ошибку и удалится вторая линия, ", font = ("Arial", 13))
  okno44 = Label(opragramme, text = "после выполение процедуры Вввод связей ребер и вес вершин, вы сможете увидеть Вес на дуге, значит вы сделали  -  верно. ", font = ("Arial", 13))
  okno5 = Label(opragramme, text = "Далее после того как вы создали уже граф, вы можете нажать кнопку Критический путь, ", font = ("Arial", 13))
  okno55 = Label(opragramme, text = "тогда ниже будут написаны вершины из которого они состоят, а так же чему он будет равен, но это еще не все, он будет  - выделен красным цветом", font = ("Arial", 13))
  okno.place(x = 0, y = 0)
  okno0.place(x = 0, y = 25)
  okno1.place(x = 0, y = 50)
  okno11.place(x = 0, y = 75)
  okno2.place(x = 0, y = 100)
  okno22.place(x = 0, y = 125)
  okno3.place(x = 0, y = 150)
  okno33.place(x = 0, y = 175)
  okno4.place(x = 0, y = 200)
  okno44.place(x = 0, y = 225)
  okno5.place(x = 0, y = 250)
  okno55.place(x = 0, y = 275)
  
def instrucia():
  instucia = Tk()
  instucia.geometry("1550x55")
  okno = Label(instucia, text = "При запуске окна при вводе Веса, если Вы укажете текст будет ошибка, если вы соединили циклом, выдаст ошибку и удалит линию, Вводите те номера которые указаны на вершинах!", font = ("Arial", 13))
  okno.place(x = 0, y = 0)

def ob_aftore():
  #Создание кнопки об авторе и показание данных
  obaftore = Tk()
  obaftore.geometry("550x55")
  okno = Label(obaftore, text = "Студенты гр. 22 - ВТм", font = ("Arial", 13))
  okno.place(x = 130, y = 0)
def for_buttonall(event):
  global okno, entrynomer, entrynomer1, entryves, entryCost
  okno = Tk()
  okno.title("Аттрибуты")
  okno.wm_attributes(' - topmost', 1)
  okno.geometry("650x175")
  label2 = Label(okno, text = "Вввод связей ребер и вес вершин", font = ("Arial", 22)).place(x = 45, y = 0)
  labelnomer = Label(okno, text = "Номер для вершины:", font = ("Arial", 13)).place(x = 45, y = 50)
  labelnomer1 = Label(okno, text = "Номер для вершины:", font = ("Arial", 13)).place(x = 245, y = 50)
  labelves = Label(okno, text = "Вес ребра:", font = ("Arial", 13)).place(x = 445, y = 50)
  labelcost = Label(okno, text = "Стоимость:", font = ("Arial", 13)).place(x = 505, y = 50)
  knopka = Button(okno, text = "Прочтите перед вводом", command = chtenie, font = ("Arial", 13)).place(x = 190, y = 143)
  entrynomer = Entry(okno).place(x = 65, y = 80)
  entrynomer1 = Entry(okno).place(x = 265, y = 80)
  entryves = Entry(okno, width = 10).place(x = 455, y = 80)
  entryCost = Entry(okno, width = 10).place(x = 505, y = 80)

  otmena = Button(okno, text = "Выйти", command = quit_program, width = 8, font = ("Arial", 13))
  otmena.place(x = 470, y = 143)
  add = Button(okno, text = "Добавить", command = for_add, width = 8, font = ("Arial", 13))
  add.place(x = 390, y = 143)

def chtenie():
  OKNO = Tk()
  OKNO.geometry("1500x55")
  labelostorozno = Label(OKNO, text = "Уважаемый пользователь, вводите номера соотвествующие, тем, с которыми вы создали смежность, иначе программа будет работать не корректно.", font = ("Arial", 13))
  labelostorozno.place(x = 0, y = 0)

def sozdanie_kruga(event):
  global r1x, r2y, a, kolvo, graph, en_alphabet, last_alphabet_index
  kolvo = a
  rx  =  event.x
  ry  =  event.y
  r1x  =  event.x - 40
  r2y  =  event.y - 40
  
  
  massivkolvo.append(kolvo)
  
  node_name = en_alphabet[last_alphabet_index]
  new_node = Node(node_name)
  graph.add_node(new_node)
  last_alphabet_index += 1
  nullP = canva.create_text(r1x + 20, r2y + 20, text = f"{a} ({node_name})", fill = "black")
  krug = canva.create_oval(rx, ry, r1x, r2y, outline = 'black')
  a = a + 1

  print(f"graph = {graph.show_graph()}")
  
def napravlenie(event):
  global x1, y1, x2, y2, liniya
  
  lx.append(event.x)
  ly.append(event.y)
  print(f"lx = {lx}, ly = {ly}")

  liniya = canva.create_line(lx[0], ly[0], lx[1], ly[1]) #, arrow = LAST
  x1 = lx[0]
  y1 = ly[0]
  x2 = lx[1]
  y2 = ly[1]

  for_buttonall(event)
  lx.clear()
  ly.clear()

def for_add():
    global firstrebro, secondrebro, ves, cost, graph
    #Проверка на пустоту и буквы, и передача данных из Entry и очистка Entry
    try:      
      firstrebro = int()
      secondrebro = int()
      ves = int()
      cost = int()
      firstrebro = int(entrynomer.get())
      secondrebro = int(entrynomer1.get())
      ves = int(entryves.get())
      entrynomer.delete(0, END)
      entrynomer1.delete(0, END)
      entryves.delete(0, END)
      quit_program()
    except ValueError:
      mb.showerror("Ошибка", "Поле не должно быть пустым и содержать буквы")
      entrynomer.delete(0, END)
      entrynomer1.delete(0, END)
      entryves.delete(0, END)
      return
    if ves == 0:
      canva.itemconfig(liniya, dash = (10, 2))
      
    #Проверка первого ребра на знак
    if firstrebro <0:
      mb.showerror("Ошибка", "Не одно из полей не должно иметь отрицательные значения")
      entrynomer.delete(0, END)
      entrynomer1.delete(0, END)
      entryves.delete(0, END)
      return
    #Проверка второго ребра на знак
    if secondrebro <0:
      mb.showerror("Ошибка", "Не одно из полей не должно иметь отрицательные значения")
      entrynomer.delete(0, END)
      entrynomer1.delete(0, END)
      entryves.delete(0, END)
      return
    #Проверка веса на знак
    if ves <0:
      mb.showerror("Ошибка", "Не одно из полей не должно иметь отрицательные значения")
      entrynomer.delete(0, END)
      entrynomer1.delete(0, END)
      entryves.delete(0, END)
      return
    #Вершины не могут соединиться друг с другом
    if firstrebro  ==  secondrebro:
      mb.showerror("Ошибка", "Так нельзя задать смежность!")
      canva.delete(liniya)
      return
      
    if len(dlyapervogo)>0:
      l = 0
      for i in dlyapervogo:
        if secondrebro  ==  i:
          if dlyavtorogo[l] == firstrebro:
           l = l + 1
           mb.showerror("Ошибка", "В сетевом графе не может быть циклов!")
           canva.delete(liniya)
           canva.delete(nullP)
           return
   
    dlyalini.append(liniya)
    nullP  =  canva.create_text((x1 + x2)/2, (y1 + y2)/2, text =  str(ves), fill = "black", font = 16)
    dlyapervogo.append(firstrebro)
    dlyavtorogo.append(secondrebro)
    dlyvesa.append(ves)

    graph.connect(graph.adj_list[firstrebro - 1], graph.adj_list[secondrebro - 1], 15)
    graph.show_graph()

def way():
  global crit, s
  s = 0
  l = 1
  crit = []
  crit = critway()
    
  for i in crit:
      if(l<len(crit)):
        s = s + sumq(i, crit[l])
        l = l + 1
        resovanie()

def sumq(a, b):
  j = 0
  m = 0
  k = 0
  for i in dlyapervogo:
    
    if (a == i):
      
      if (b == dlyavtorogo[j]):

        canva.itemconfig(dlyalini[m], fill = "red")
        return dlyvesa[k]
    j = j + 1
    k = k + 1
    m = m + 1

'''
Расчет критического пути
'''
def critway():
  k = 0
  j = 0
  critical  =  0
  for i in dlyapervogo:
    dg.add_edge(i, dlyavtorogo[j], weight = dlyvesa[k])
    critical = nx.dag_longest_path(dg, weight = "weight")
    k = k + 1
    j = j + 1
  return critical  

def resovanie():
  label1 = Label(root, text = "Критический путь cостоит из:", font = ("Arial", 13))
  label15 = Label(root, text = str(crit), font = ("Arial", 11))
  label15.place(x = 0, y = 232)
  label1.place(x = 0, y = 182)
  label2 = Label(root, text = "Критический путь равен  =  "  + str(s), font = ("Arial", 13))
  label2.place(x = 0, y = 282)

def quit_program1():
  root.destroy()

def quit_program():
  okno.destroy()

#Создаем три массива, в которых будет хранится вес и смежность ребер
lx = []
ly = []
dlyapervogo  =  []
dlyavtorogo  =  []
dlyvesa  =  []
a = 1
massivkolvo = []
matrix = []
dlyalini = []

#При то что появляется первом запуске
dg = nx.DiGraph()
root = Tk()
root.geometry("1920x1080")
root.title("Алгоритмы на графах")
canva  =  Canvas(root, width = 1700, height = 1200, bg = "white")
canva.place(x = 324, y =  - 2)
canva.bind('<Control - Button - 1>', sozdanie_kruga)
canva.bind('<Button - 3>', napravlenie)

aftor = Button(root, text = "Об авторе", width = 35, command = ob_aftore, font = ("Arial", 13))
aftor.place(x = 0, y = 99)     
vvod = Button(root, text = "Рассчитать критический путь", command = way, width = 35, font = ("Arial", 13))
vvod.place(x = 0, y = 66)
vixod = Button(root, text = "Выход", width = 35, command = quit_program1, font = ("Arial", 13))
vixod.place(x = 0, y = 132)
peredvvodom = Button(root, text = "Правила ввода данных", width = 35, command = instrucia, font = ("Arial", 13))
peredvvodom.place(x = 0, y = 34)
peredvvodom = Button(root, text = "Правила работы программы", width = 35, command = oprogramme, font = ("Arial", 13))
peredvvodom.place(x = 0, y = 0)

global graph 
graph = Graph([])

'''

#Задание графа
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

g = Node('g')
j = Node('j')
h = Node('h')
k = Node('k')

graph.connect(a, b, 5, 20)
graph.connect(a, c, 10, 15)
graph.connect(a, e, 2, 22)
graph.connect(b, c, 2, 5)
graph.connect(b, d, 4, 8)
graph.connect(c, d, 7, 16)
graph.connect(c, f, 10, 18)
graph.connect(d, e, 3, 14)

print("Кратчайшие пути:")
print([(weight, [n.data for n in node]) for (weight, node) in graph.dijkstra(a)])

graph.add_node(j)
graph.add_node(g)
graph.add_node(h)
graph.add_node(k)

print(f"{graph.adj_list}")

print("\nМинимальные стоимости:")
'''

root.mainloop()

