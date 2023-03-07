"""
Basic Password Generator created in python. 
By: Yael Brown
Date: 3/7/2023
"""

import string
import random

# constants
lower = string.ascii_letters[:26]
upper = string.ascii_letters[26:]
special = "~!@#$%^&*()-+=[]:><?/"
number = "0123456789"

def promptForLength():
  length = input("Enter the length of the password you want: ")
  try:
    return int(length)
  except: 
    print(f"{length} is not a number... please try again.\n")
    promptForLength()
     
def promptForCharacters(q):
  print(q)
  res = input("Enter yes/y or no/n: ")
  if res == "yes" or res == "y":
    return True
  elif res == "no" or res == "n":
    return False
  else:
    print("Invalid response... please try again\n")
    promptForCharacters(q)

def generatePassword(l, ch):
  out = ""
  for i in range(l):
    out += random.choice(ch)
  return out

def promptNewPass(l, ch):
  newPass = promptForCharacters("Do you want generate another password?: ")
  print("\n")
  if newPass:
    print(generatePassword(l, ch))
    print("\n")
    promptNewPass(l, ch)

def main():
  print("Welcome to the password generator!\n")
  length = promptForLength()

  availChars = ""

  wantLower = promptForCharacters("Do you want lowercase characters?")
  if wantLower: availChars += lower
  wantUpper = promptForCharacters("Do you want uppercase characters?")
  if wantUpper: availChars += upper
  wantSpecial = promptForCharacters("Do you want special characters?")
  if wantSpecial: availChars += special
  wantNumbers = promptForCharacters("Do you want numbers characters?")
  if wantNumbers: availChars += number

  print({"a": availChars, "l": length})

  if len(availChars) == 0:
    print("You need to have some characters to generate a password with... \n Goodbye...")
    exit(1)

  print("\n")
  print(generatePassword(length, availChars))
  print("\n")
  promptNewPass(length, availChars)
  print("Goodbye :)\n")
  
  exit(0)

if __name__ == "__main__":
  main()