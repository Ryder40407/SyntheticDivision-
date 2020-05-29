# --------------------------------------
# --- Imports --------------------------
# --------------------------------------
import os
import math


# --------------------------------------
# --- Pre-Variables --------------------
# --------------------------------------
ProgramRunning = True

# --------------------------------------
# --- All System Functions -------------
# --------------------------------------
# --- Clear
def clearSYS():
    set1a = 0
    set2a = 0
    set3a = 0
    set4a = 0

    set1b = 0
    set2b = 0

    set1aPW = 0
    set2aPW = 0
    set3aPW = 0
    set4aPW = 0

    set1bPW = 0
    set2bPW = 0


# --- System 2x2
def sys2x2():
    # Set A
    set1a = float(input("\nSet A, 1 Val: "))
    set2a = float(input("Set A, 2 Val: "))
    set1aPW = float(input("Set A, 1st Power: "))
    set2aPW = "0"

    # Set B
    set1b = float(input("\nSet B, 1 Val: "))
    set2b = float(input("Set B, 2 Val: "))
    set1bPW = float(input("Set B, 1st Power: "))
    set2bPW = "0"

    # Zero Set B
    setBzero = (set2b / set1b) * -1

    # Set
    finalNum1 = set1a * setBzero
    finalNum2 = set2a + finalNum1

    # Conversion
    finalNum1 = str(finalNum1)
    finalNum2 = str(finalNum2)

    set1aPW = str(set1aPW - 1)

    set1a = str(set1a)

    set1b = str(set1b)
    set2b = str(set2b)
    set1bPW = str(set1bPW)

    print("")
    print(finalNum1)
    print(finalNum2)

    # String-afy
    print("")
    finalSTR = (set1a + "x^" + set1aPW + " + " + finalNum1)
    finalREM = (finalNum2 + "/" + set1b + "x^" + set1bPW + " + " + set2b)
    print(finalSTR)
    if finalNum2 != "0.0":
        print(finalREM)

# --- System 3x2
def sys3x2():
    # Set A
    set1a = float(input("\nSet A, 1 Val: "))
    set2a = float(input("Set A, 2 Val: "))
    set3a = float(input("Set A, 3 Val: "))
    set1aPW = float(input("Set A, 1st Power: "))
    set2aPW = float(input("Set A, 2nd Power: "))
    set3aPW = "0"

    # Set B
    set1b = float(input("\nSet B, 1 Val: "))
    set2b = float(input("Set B, 2 Val: "))
    set1bPW = float(input("Set B, 1st Power: "))
    set2bPW = "0"

    # Zero Set B
    setBzero = (set2b / set1b) * -1

    # Set
    finalNum1 = set1a * setBzero
    finalNum2 = set2a + finalNum1
    finalNum3 = set3a + (finalNum2 * setBzero)

    # Conversion
    finalNum1 = str(finalNum1)
    finalNum2 = str(finalNum2)
    finalNum3 = str(finalNum3)

    set1aPW = str(set1aPW)
    set2aPW = str(set2aPW)

    set1a = str(set1a)

    set1b = str(set1b)
    set2b = str(set2b)
    set1bPW = str(set1bPW)

    print("")
    print(finalNum1)
    print(finalNum2)
    print(finalNum3)

    # String-afy
    print("")
    finalSTR = (set1a + "x^" + set1aPW + " + " + finalNum2 + "x^" + set2aPW)
    finalREM = (finalNum3 + "/" + set1b + "x^" + set1bPW + " + " + set2b)
    print(finalSTR)
    if finalNum3 != "0.0":
        print(finalREM)


# --- System 4x2
def sys4x2():
    # Set A
    set1a = float(input("\nSet A, 1 Val: "))
    set2a = float(input("Set A, 2 Val: "))
    set3a = float(input("Set A, 3 Val: "))
    set4a = float(input("Set A, 4 Val: "))
    set1aPW = float(input("Set A, 1st Power: "))
    set2aPW = float(input("Set A, 2nd Power: "))
    set3aPW = float(input("Set A, 3rd Power: "))
    set4aPW = "0"

    # Set B
    set1b = float(input("\nSet B, 1 Val: "))
    set2b = float(input("Set B, 2 Val: "))
    set1bPW = float(input("Set B, 1st Power: "))
    set2bPW = "0"

    # Zero Set B
    setBzero = (set2b / set1b) * -1

    # Set
    finalNum1 = set1a * setBzero
    finalNum2 = set2a + finalNum1
    finalNum3 = set3a + (finalNum2 * setBzero)
    finalNum4 = set4a + (finalNum3 * setBzero)

    # Conversion
    finalNum1 = str(finalNum1)
    finalNum2 = str(finalNum2)
    finalNum3 = str(finalNum3)
    finalNum4 = str(finalNum4)

    set1aPW = str(set1aPW)
    set2aPW = str(set2aPW)
    set3aPW = str(set3aPW)

    set1a = str(set1a)

    set1b = str(set1b)
    set2b = str(set2b)
    set1bPW = str(set1bPW)

    print("")
    print(finalNum1)
    print(finalNum2)
    print(finalNum3)
    print(finalNum4)

    #String-afy
    print("")
    finalSTR = (set1a + "x^" + set1aPW + " + " + finalNum2 + "x^" + set2aPW + " + " + finalNum3 + "x^" + set3aPW)
    finalREM = (finalNum4 + "/" + set1b + "x^" + set1bPW + " + " + set2b)
    print(finalSTR)
    if finalNum4 != "0.0":
        print(finalREM)

# --- System 5x2
def sys5x2():
    # Set A
    set1a = float(input("\nSet A, 1 Val: "))
    set2a = float(input("Set A, 2 Val: "))
    set3a = float(input("Set A, 3 Val: "))
    set4a = float(input("Set A, 4 Val: "))
    set5a = float(input("Set A, 5 Val: "))
    set1aPW = float(input("Set A, 1st Power: "))
    set2aPW = float(input("Set A, 2nd Power: "))
    set3aPW = float(input("Set A, 3rd Power: "))
    set4aPW = float(input("Set A, 4th Power: "))
    set5aPW = "0"

    # Set B
    set1b = float(input("\nSet B, 1 Val: "))
    set2b = float(input("Set B, 2 Val: "))
    set1bPW = float(input("Set B, 1st Power: "))
    set2bPW = "0"

    # Zero Set B
    setBzero = (set2b / set1b) * -1

    # Set
    finalNum1 = set1a * setBzero
    finalNum2 = set2a + finalNum1
    finalNum3 = set3a + (finalNum2 * setBzero)
    finalNum4 = set4a + (finalNum3 * setBzero)
    finalNum5 = set4a + (finalNum4 * setBzero)

    # Conversion
    finalNum1 = str(finalNum1)
    finalNum2 = str(finalNum2)
    finalNum3 = str(finalNum3)
    finalNum4 = str(finalNum4)
    finalNum5 = str(finalNum5)

    set1aPW = str(set1aPW)
    set2aPW = str(set2aPW)
    set3aPW = str(set3aPW)
    set4aPW = str(set4aPW)

    set1a = str(set1a)

    set1b = str(set1b)
    set2b = str(set2b)
    set1bPW = str(set1bPW)

    print("")
    print(finalNum1)
    print(finalNum2)
    print(finalNum3)
    print(finalNum4)
    print(finalNum5)

    #String-afy
    print("")
    finalSTR = (set1a + "x^" + set1aPW + " + " + finalNum2 + "x^" + set2aPW + " + " + finalNum3 + "x^" + set3aPW + " + " + finalNum4 + "x^" + set4aPW)
    finalREM = (finalNum5 + "/" + set1b + "x^" + set1bPW + " + " + set2b)
    print(finalSTR)
    if finalNum5 != "0.0":
        print(finalREM)


# --------------------------------------
# --------------------------------------
# --------------------------------------
def mainPrgRUN():
    systemQst = input("\nWhat size of system do you want? ")
    print(" ")

    if systemQst == "2x2":
        sys2x2()
        clearSYS()
    elif systemQst == "3x2":
        sys3x2()
        clearSYS()
    elif systemQst == "4x2":
        sys4x2()
        clearSYS()
    elif systemQst == "5x2":
        sys5x2()
        clearSYS()


# --------------------------------------
# --------------------------------------
# --------------------------------------
while ProgramRunning:
    mainPrgRUN()