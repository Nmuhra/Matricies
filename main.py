import math

choice = input("A for : [2*2]*[2*2],B for : [3*3]*[3*3] \n").lower()

if choice == "a":
  M1C1R1 = int(input("matricie1-column1-row1:\n"))
  M1C1R2 = int(input("matricie1-column1-row2:\n"))
  M1C2R1 = int(input("matricie1-column2-row1:\n"))
  M1C2R2 = int(input("matricie1-column2-row2:\n"))
  
  M2C1R1 = int(input("matricie2-column1-row1:\n"))
  M2C1R2 = int(input("matricie2-column1-row2:\n"))
  M2C2R1 = int(input("matricie2-column2-row1:\n"))
  M2C2R2 = int(input("matricie2-column2-row2:\n"))
  print(f"R1,C1 = ({M1C1R1}*{M2C1R1})+({M1C2R1}*{M2C1R2})")
  print(f"R1,C2 = ({M1C1R1}*{M2C2R1})+({M1C2R1}*{M2C2R2})")
  print(f"R2,C1 = ({M1C1R2}*{M2C1R1})+({M1C2R2}*{M2C1R2})")
  print(f"R2,C2 = ({M1C1R2}*{M2C2R1})+({M1C2R2}*{M2C2R2})")
if choice == "b":
  M1C1R1 = int(input("matricie1-column1-row1:\n"))
  M1C1R2 = int(input("matricie1-column1-row2:\n"))
  M1C1R3 = int(input("matricie1-column1-row3:\n"))
  M1C2R1 = int(input("matricie1-column2-row1:\n"))
  M1C2R2 = int(input("matricie1-column2-row2:\n"))
  M1C2R3 = int(input("matricie1-column2-row3:\n"))
  M1C3R1 = int(input("matricie1-column3-row1:\n"))
  M1C3R2 = int(input("matricie1-column3-row2:\n"))
  M1C3R3 = int(input("matricie1-column3-row3:\n"))
  
  M2C1R1 = int(input("matricie1-column1-row1:\n"))
  M2C1R2 = int(input("matricie1-column1-row2:\n"))
  M2C1R3 = int(input("matricie1-column1-row3:\n"))
  M2C2R1 = int(input("matricie1-column2-row1:\n"))
  M2C2R2 = int(input("matricie1-column2-row2:\n"))
  M2C2R3 = int(input("matricie1-column2-row3:\n"))
  M2C3R1 = int(input("matricie1-column3-row1:\n"))
  M2C3R2 = int(input("matricie1-column3-row2:\n"))
  M2C3R3 = int(input("matricie1-column3-row3:\n"))
