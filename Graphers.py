#Создаем меню и создаем месседжи для пользователя, чтобы он знал об ошибках
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb

root = Tk()
root.geometry("1920x1080")
root.title("Алгоритмы на графах")

listWayLongEntry = []
listWayCostEntry = []

listWayLong = []
listWayCost = []

en_alphabet = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12"]

frame = Frame(root)
frame.grid(row=0, column = 0  )

dim = Entry(frame)
dim.grid(row=0, column=1,
                columnspan=20,
                sticky=W+E, padx=10)
 
dimLabel = Label(frame, text="Размерность\n(m * n):").grid(
    row=0, column=0, sticky=W,
    pady=10, padx=10)
 
Button(frame, text="Справка")\
    .grid(row=1, column=0, pady=10, padx=10, columnspan=5)
Button(frame, text="Вывести\nматрицу", command = lambda: showMatrix())\
    .grid(row=1, column=6, columnspan=10)
Button(frame, text="Рассчитать", command = lambda: drawPath())\
    .grid(row=1, column=11, padx=10, columnspan=5)


def showMatrix():
  global dim, listWayLongEntry, listWayCostEntry, listWayLong, listWayCost, dimension, en_alphabet

  dimension = dim.get()
  dimension = int(dimension)

  count = 0
  rowLevel = 1

  frameForMatrix = Frame(root)
  frameForMatrix = Frame(root)\
    .grid(row=1, column = 0)

  Label(frameForMatrix, text="Ω дороги")\
    .grid(row= 0, column = rowLevel - 1, columnspan = dimension, sticky=N)

  Label(frameForMatrix, text="D стоимость")\
    .grid(row= 0, column = dimension + 1, columnspan = dimension, sticky=N)

  
  columnLevel = dimension + 1

  stdDim = 4

  

  #дороги
  for i in range (dimension):
    listWayLongEntry.append([])
    Label(frameForMatrix, text=f"{en_alphabet[i]}")\
    .grid(row= rowLevel, column = i + 1, sticky=N, padx = stdDim)

    for j in range (dimension):
      if i == 0:
        Label(frameForMatrix, text=f"{en_alphabet[j]}")\
          .grid(row= j + rowLevel + 1, column = i, sticky=N, padx = stdDim)
      # Label(text=f"{en_alphabet[i]}")\
      #   .grid(row= j, column = i + 1, sticky=E)

      button = Entry(frameForMatrix, width = stdDim)
      button.grid(row = j + rowLevel + 1, column = i + 1, sticky=N, padx = stdDim)

      listWayLongEntry[i].append(button)
      listWayLongEntry[i][j].insert(0, "0")
  
  #пути
  for i in range (dimension):
    listWayCostEntry.append([])
    Label(frameForMatrix, text=f"{en_alphabet[i]}")\
    .grid(row= rowLevel, column = columnLevel + i + 1, sticky=N, padx = stdDim)

    for j in range (dimension):
      if i == 0:
        Label(frameForMatrix, text=f"{en_alphabet[j]}")\
          .grid(row= j + rowLevel + 1, column = columnLevel + i, sticky=N, padx = stdDim)
      # Label(text=f"{en_alphabet[i]}")\
      #   .grid(row= j, column = i + 1, sticky=E)
      button = Entry(frameForMatrix, width = stdDim)
      button.grid(row = j + rowLevel + 1, column = columnLevel + i + 1, sticky=N, padx = stdDim)

      listWayCostEntry[i].append(button)
      listWayCostEntry[i][j].insert(0, "0")

def drawPath():
  frameForGraph = Frame(root)
  frameForGraph.grid(row= dimension + 5, column = 1, rowspan = 20, columnspan = 40)

  canva = Canvas(frameForGraph, width = 800, height = 600, bg = "white")
  canva.pack()#grid(row = 0, column = 0, sticky=N, padx = 25, pady = 25)

  baseX = 100
  baseY = 300

  defoltSize = 20


  listConnections = []
  
  for row in range(len(listWayLongEntry)):
    for col in range(len(listWayLongEntry[row])):
      pathLengh = int(listWayLongEntry[row][col].get())
      pathCost = int(listWayCostEntry[row][col].get())
      print(f"pathLengh = {pathLengh}, pathCost = {pathCost}")

      if pathLengh != 0:
        listConnections.append([col, row, pathLengh, pathCost])
  
  # print(f"listConnections = {listConnections}")
  # for i in listConnections:
    # nullP  =  canva.create_text((x1 + x2)/2, (y1 + y2)/2, text =  str(ves), fill = "black", font = 16)

  for i in range(dimension):

    if i % 3 == 0:
      baseX += 100
      baseY = 300
    nullP = canva.create_text(baseX , baseY , text = f"{en_alphabet[i]}", fill = "black")
    krug = canva.create_oval(baseX - defoltSize, baseY - defoltSize, baseX + defoltSize, baseY + defoltSize, outline = 'black')

    # for key in listConnections:
      # if key[0] == i:
        # nullP  =  canva.create_text((x1 + x2)/2, (y1 + y2)/2, text =  str(ves), fill = "black", font = 16)
        # newLine = canva.create_line(lx[0], ly[0], lx[1], ly[1]) 

    baseY += 100
  
  

# def getXAndYByIterator(i: int):
#   baseX = 100
#   baseY = 300

#   if i % 3 == 0:
#       baseX += 100
#       baseY = 300

#   baseY += 100








# canva.bind('<Control - Button - 1>', sozdanie_kruga)
# canva.bind('<Button - 3>', napravlenie)

root.mainloop()

