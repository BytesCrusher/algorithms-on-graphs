#Создаем меню и создаем месседжи для пользователя, чтобы он знал об ошибках
from random import *
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb

from math import ceil

import numpy as np
import matplotlib.pyplot as plt # Import Matplotlib tool kit 
import networkx as nx # Import NetworkX tool kit 

root = Tk()
root.geometry("+200+200")
root.title("Алгоритмы на графах")

listWayLongEntry = []
listWayCostEntry = []

listWayLong = []
listWayCost = []

arraylabelcost = []
arraylableway = []

en_alphabet = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19", "X20", "X21", "X22", "X23", "X24", "X25", "X26", "X27", "X28"]

frame = Frame(root , bg = "red")
frame.grid(row=0, column=0)
# frame.pack()#grid(row=0, column=0)

frameForMatrix = Frame(root, bg = "green")
frameForMatrix.grid(row= 1, column= 0)
# .pack()

# frameForGraph = Frame(root, bg = "blue")
# frameForGraph.grid(row= 2, column= 0)
# frameForGraph.pack() #grid(row= 3, column = 0, rowspan = 20, columnspan = 40)



frameForResult = Frame(root, bg = "cyan")
frameForResult.grid(row= 2, column= 1)



dimLabel = Label(frame, text="Размерность\n(m * n):", width=20).grid(
    row=0, column=0, sticky=W, padx=40)

dim = Entry(frame)
dim.grid(row=1, column=0, columnspan=3, pady=10, sticky=W+E, padx=10)

Button(frame, text="Вывести\nматрицу", width=20, command = lambda: showMatrix())\
    .grid(row=2, column=0, padx=40)

Button(frame, text="Справка", width=20)\
    .grid(row=3, column=0)

Button(frame, text="Рассчитать", width=20, command = lambda: drawPath())\
    .grid(row=4, column=0)

Button(frame, text="Очистить", width=20, command = lambda: destroy())\
    .grid(row=5, column=0)


def showMatrix():
  global dim, listWayLongEntry, listWayCostEntry, listWayLong, listWayCost, dimension, en_alphabet, arraylableway, arraylabelcost

  destroy()
  dimension = dim.get()
  dimension = int(dimension)

  count = 0
  rowLevel = 1

  Label(frameForMatrix, text="Ω Пропускная способность")\
    .grid(row = dimension + 2, column = rowLevel+1, columnspan = dimension, sticky=N)

  Label(frameForMatrix, text="D стоимость")\
    .grid(row = dimension + 2, column = dimension + 4, columnspan = dimension, sticky=N)

  
  columnLevel = dimension + 1

  stdDim = 4

  #дороги
  for i in range (dimension):
    listWayLongEntry.append([])
    label = Label(frameForMatrix, text=f"{en_alphabet[i]}")
    
    arraylableway.append(label)

    arraylableway[i].grid(row= rowLevel, column = i + 2, sticky=N, padx = stdDim)

    for j in range (dimension):
      if i == 0:
        label = Label(frameForMatrix, text=f"{en_alphabet[j]}")\
          .grid(row= j + rowLevel + 1, column = i + 1, sticky=N, padx = stdDim)
      # Label(text=f"{en_alphabet[i]}")\
      #   .grid(row= j, column = i + 1, sticky=E)

      if i == j:
        color = "cyan"
      else:
        color = "white"

      button = Entry(frameForMatrix, width = stdDim, background = color)
      button.grid(row = j + rowLevel + 1, column = i + 2, sticky=N, padx = stdDim)

      listWayLongEntry[i].append(button)
      listWayLongEntry[i][j].insert(0, "0")
  
  #пути
  for i in range (dimension):
    listWayCostEntry.append([])
    label = Label(frameForMatrix, text=f"{en_alphabet[i]}")
    
    arraylabelcost.append(label)
    print(f"arraylabelcost = {arraylabelcost}")

    arraylabelcost[i].grid(row= rowLevel, column = columnLevel + i + 3, sticky=N, padx = stdDim)

    for j in range (dimension):
      if i == 0:
        Label(frameForMatrix, text=f"{en_alphabet[j]}")\
          .grid(row= j + rowLevel + 1, column = columnLevel + i + 2, sticky=N, padx = stdDim)
      
      if i == j:
        color = "cyan"
      else:
        color = "white"

      # Label(text=f"{en_alphabet[i]}")\
      #   .grid(row= j, column = i + 1, sticky=E)
      button = Entry(frameForMatrix, width = stdDim, background = color)
      button.grid(row = j + rowLevel + 1, column = columnLevel + i + 3, sticky=N, padx = stdDim)

      listWayCostEntry[i].append(button)
      listWayCostEntry[i][j].insert(0, "0")

def drawPath():
  global nodesCoord, frameForResult, allNodesInThisGraph #frameForGraph, canva
  # canva = Canvas(frameForGraph, width = 800, height = 500, bg = "white")
  # canva.pack()

  baseX = 100
  baseY = 300

  defoltSize = 20


  listConnections = []
  
  for row in range(len(listWayLongEntry)):
    for col in range(len(listWayLongEntry[row])):
      pathLengh = int(listWayLongEntry[row][col].get())
      pathCost = int(listWayCostEntry[row][col].get())
      # print(f"pathLengh = {pathLengh}, pathCost = {pathCost}")

      if pathLengh != 0:
        #столбец, строка, длина пути, стоимость пути, 
        listConnections.append([col, row, pathLengh, pathCost])
  
  # print(f"listConnections = {listConnections}")
  # for i in listConnections:
    # nullP  =  canva.create_text((x1 + x2)/2, (y1 + y2)/2, text =  str(ves), fill = "black", font = 16)

  allNodesInThisGraph = []

  nodesCoord = []
  for i in range(dimension):

    # if i % 3 == 0:
    #   baseX += 150
    #   baseY = 100
    

    # lx = baseX - defoltSize
    # ly = baseY - defoltSize

    # rx = baseX + defoltSize
    # ry = baseY + defoltSize

    # centerXCoord = rx - ((rx - lx) / 2)
    # centerYCoord = ry - ((ry - ly) / 2)
    # nodesCoord.append([centerXCoord, centerYCoord])

    allNodesInThisGraph.append(en_alphabet[i])

    # nullP = canva.create_text(baseX , baseY , text = f"{en_alphabet[i]}", fill = "black")
    # krug = canva.create_oval(lx, ly, rx, ry, outline = 'black')
    baseY += 100
  
  # print(f"listConnections = {listConnections}")
  # for line in listConnections:
  #   firstNode = line[0]
  #   secondNode = line[1]

  #   nodesCoord

  #   centerXLabelCoord = nodesCoord[secondNode][0] - ((nodesCoord[secondNode][0] - nodesCoord[firstNode][0]) / 2)
  #   centerYLabelCoord = nodesCoord[secondNode][1] - ((nodesCoord[secondNode][1] - nodesCoord[firstNode][1]) / 2) - 10

  #   label = canva.create_text(centerXLabelCoord , centerYLabelCoord , text = f"{line[3]} ({line[2]})", fill = "black")
  #   color = '#{:06x}'.format(random_color())
  #   line = canva.create_line(nodesCoord[firstNode][0], nodesCoord[firstNode][1], nodesCoord[secondNode][0], nodesCoord[secondNode][1], width=3, fill=color)

  # resultTextLabel = Label(frameForResult, text=f"Посчитали такой граф")
  # resultTextLabel.grid(row= 0, column= 0)
  calculateGraph(listConnections)


def calculateGraph(listConnections: list):
  #listConnections : [столбец, строка, длина пути, стоимость пути]
  G2 = nx.DiGraph() # Create a directed graph DiGraph

  firstNodeStringName = allNodesInThisGraph[0]
  lastNodeStringName = allNodesInThisGraph[-1]
  print(f"firstNodeStringName = {firstNodeStringName}, lastNodeStringName = {lastNodeStringName}")
  
  connectionData = []

  for connection in listConnections:
    firstNode = connection[0]
    secondNode = connection[1]

    firstNodeName = en_alphabet[firstNode]
    secondNodeName = en_alphabet[secondNode]

    pathDataDict = {'capacity' : connection[2], 'weight' : connection[3]}

    connectionData.append((firstNodeName, secondNodeName, pathDataDict))

  print(f"connectionData = {connectionData}")

  #3.29.1 вариант 1
  G2.add_edges_from(connectionData)

  # Add edge properties 'capacity', 'weight'
  # Sort out the labels on the edges , Used for drawing display 
  edgeLabel1 = nx.get_edge_attributes(G2, 'capacity')
  edgeLabel2 = nx.get_edge_attributes(G2, 'weight')
  edgeLabel = {
  }
  for i in edgeLabel1.keys():
      edgeLabel[i] = f'({edgeLabel1[i]:},{edgeLabel2[i]:})' # The side ( Capacity , cost )

  # Calculate the shortest path --- It's not necessary , Used to compare the results with the minimum cost flow 
  lenShortestPath = nx.shortest_path_length(G2, firstNodeStringName, lastNodeStringName, weight="weight")
  shortestPath = nx.shortest_path(G2, firstNodeStringName, lastNodeStringName, weight="weight")
  print("\n Shortest path : ", shortestPath) # Output shortest path 
  print(" The shortest path length : ", lenShortestPath) # Output shortest path length 

  # Calculate the minimum cost and maximum flow --- It's not necessary , Used to compare the results with the minimum cost flow 
  minCostFlow = nx.max_flow_min_cost(G2, firstNodeStringName, lastNodeStringName) # Find the minimum cost and maximum flow 
  minCost = nx.cost_of_flow(G2, minCostFlow) # Find the value of the minimum cost
  
  maxFlow = sum(minCostFlow[firstNodeStringName][j] for j in minCostFlow[firstNodeStringName].keys()) # Find the value of the maximum flow 
  print("\n Maximum flow : {}".format(maxFlow)) # Output the value of the minimum cost 
  print(" Minimum cost of maximum flow : {}\n".format(minCost)) # Output the value of the minimum cost 
  # v = input("Input flow (v>=0):")

  v = 0
  while True:
      v += 1 # Flow of minimum cost flow 
      G2.add_node(firstNodeStringName, demand=-v) # nx.min_cost_flow() Setting requirements for 
      G2.add_node(lastNodeStringName, demand=v) # Set source point / The flow at the sink 
      try: # Youcans@XUPT
          # Find the minimum cost flow (demand=v)
          minFlowCost = nx.min_cost_flow_cost(G2) # Find the cost of the minimum cost flow 
          minFlowDict = nx.min_cost_flow(G2) # Find the minimum cost flow 
          # minFlowCost, minFlowDict = nx.network_simplex(G2) # Find the minimum cost flow -- Equivalent to uplink 
          print(" Traffic : {:2d}\t Minimum cost :{}".format(v, minFlowCost)) # Output the value of the minimum cost (demand=v)
          # print(" Path and flow of minimum cost flow : ", minFlowDict) # Output the path of the maximum flow and the flow on each path 
      except Exception as e:
          print(" Traffic : {:2d}\t The maximum capacity of the network has been exceeded , There is no feasible flow .".format(v))
          print("\n Traffic v={:2d}： Failed to calculate minimum cost flow ({}).".format(v, str(e)))
          break # end while True loop

  print(f"minFlowDict = {minFlowDict}")
  edgeLists = []
  for i in minFlowDict.keys():
      for j in minFlowDict[i].keys():
          edgeLabel[(i, j)] += ',f=' + str(minFlowDict[i][j]) # Take out the flow information of each side and store it in the side display value 
          if minFlowDict[i][j] > 0:
              edgeLists.append((i, j))

  maxFlow = sum(minFlowDict[firstNodeStringName][j] for j in minFlowDict[firstNodeStringName].keys()) # Find the value of the maximum flow 
  print("\n Maximum flow : {:2d},\t Minimum cost :{}".format(maxFlow, minFlowCost)) # Output the value of the minimum cost 
  print(f" Path and flow of minimum cost flow: {minFlowDict}") # The path to output the minimum cost flow and the traffic on each path 
  print(f" Path of minimum cost flow: {edgeLists}") # Ways to output minimum cost flow 

  # Draw a directed network diagram 
  pos = {}

  nodeRowsCount = ceil(dimension / 4)
  baseX = 0
  baseY = 10
  xOffset = 5
  yOffset = int(2 * baseY / nodeRowsCount)

  for i in range(len(allNodesInThisGraph)):
    nodeName = allNodesInThisGraph[i]

    if i == 0:
      x = baseX
      y = baseY
    elif i == len(allNodesInThisGraph) - 1:
      x = (dimension // nodeRowsCount) + 1
      y = baseY
    else:
      x = (i // nodeRowsCount) * xOffset + xOffset
      y = (i % nodeRowsCount) * yOffset

    pos[nodeName] = (x, y)

  print(f"pos = {pos}")
  # pos={
  # 's':(0,5),'X1':(4,8),'X2':(4,2),'X3':(10,8),'X4':(10,2),'t':(14,5)
  # } # Specifies the vertex drawing location

  result = Label(frameForMatrix, bg = "white", text="Минимальный поток минимальной стоимости.\n" + "Максимальный поток : {:2d},\t Минимальная стоимость :{}\n".format(maxFlow, minFlowCost) + f" Путь и стоимость потока минимальной стоимости: {minFlowDict}\n" + f" Путь минимальной стоимости потока: {edgeLists}\n")
  result.grid(row=dimension + 3, column = 0, columnspan = dimension * 2 + 4, sticky=N)

  fig, ax = plt.subplots(figsize=(8,6))
  # ax.text(6,2.5,"youcans-xupt",color='gainsboro')
  # ax.set_title("Минимальный поток минимальной стоимости.\n" + "Maximum flow : {:2d},\t Minimum cost :{}\n".format(maxFlow, minFlowCost) + f" Path and flow of minimum cost flow: {minFlowDict}\n" + f" Path of minimum cost flow: {edgeLists}\n")
  ax.set_title("Результаты")
  nx.draw(G2,pos,with_labels=True,node_color='c',node_size=300,font_size=10) # Draw a directed graph , Show vertex labels 
  nx.draw_networkx_edge_labels(G2,pos,edgeLabel,font_size=15) # Displays the label of the edge ：'capacity','weight' + minCostFlow
  nx.draw_networkx_edges(G2,pos,edgelist=edgeLists,edge_color='m',width=1) # Sets the color of the specified edge 、 Width 
  plt.axis('on')
  plt.show()

def random_color():
    return randint(0, 0x1000000)
    
def clear_frame(frame: Frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def destroy():
  clear_frame(frameForMatrix)
  listWayCostEntry.clear()
  listWayLongEntry.clear()
  listWayLong.clear()
  listWayCost.clear()
  arraylabelcost.clear()
  arraylableway.clear()




root.mainloop()

