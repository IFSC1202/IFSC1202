classroomA= int(input("classroom A: "))
classroomB= int(input("classroom B: "))
classroomC= int(input("classroom c: "))
fulldesksA= classroomA//2
partialdesksA= classroomA%2
fulldesksB= classroomB//2
partialdesksB= classroomB%2
fulldesksC= classroomC//2
partialdesksC= classroomC%2
total= fulldesksA+ partialdesksA+ fulldesksB+ partialdesksB+ fulldesksC+ partialdesksC
print(total)
