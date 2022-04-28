import math

dimensions = input("A for : [2*2]*[2*2],B for : [3*3]*[3*3]").upper

if dimensions == "A":
  M1C1R1 = int(input("matricie1-column1-row1:\n"))
  M1C1R2 = int(input("matricie1-column1-row2:\n"))
  M1C2R1 = int(input("matricie1-column2-row1:\n"))
  M1C2R2 = int(input("matricie1-column2-row2:\n"))
  
  M2C1R1 = int(input("matricie2-column1-row1:\n"))
  M2C1R2 = int(input("matricie2-column1-row2:\n"))
  M2C2R1 = int(input("matricie2-column2-row1:\n"))
  M2C2R2 = int(input("matricie2-column2-row2:\n"))
  print(f"[({M1C1R1}*{M2C1R1})+({M1C2R1}*{M2C1R2})]")
