#!/usr/bin/python3
import re, os, sys, glob;from io import StringIO
class string:
    null = ""
    get_expression = str("""
    Enter Corresponding #:
    [1] - Ip Address
    [2] - Visa Card
    [3] - Master Card
    [4] - Discover Card
    [5] - Social Security
    -------------------------------------""")
class sigs:
    ip_address = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b";Social_security = r"\b\d{3}-\d{2}-\d{4}\b";visa_card = "\b4[0-9]{12}(?:[0-9]{3})?\b";master_card = "\b(?:5[1-5][0-9]{2}\b";discover_card = "\b6(?:011|5[0-9]{2})[0-9]{12}\b"
directory = input("\nEnter Directory To Scan Files Or\nHit ENTER For Working Directorty:------>")
extension = input("Enter File\n-File Extension Defaults To 'txt' If Hit ENTER:------>")
get = int(input(string.get_expression))
if get == 1: expression = sigs.ip_address
if get == 2: expression = sigs.visa_card
if get == 3: expression = sigs.master_card
if get == 4: expression = sigs.discover_card
if get == 5: expression = sigs.Social_security
if len(extension) <= 2: extension = "txt"
if len(directory) <= 4: directory = os.getcwd();os.chdir(directory);count = 0;print(f"\n--------------------------------------------------\nSearching Directory: [{directory}]\n\nUsing Expression: [{expression}]\n------------------------------------------------\n")
for file in glob.glob(f"*.{extension}"):
    Fname = str(file);file_0 = open(str(file), "r", encoding="utf8");data = str(file_0.read());file_0.close();obj = re.compile(expression, re.IGNORECASE);results = str(obj.findall(data));count += 1;Std_count = str(count)
    print(str(f"[{Std_count}] - File: {Fname}\n-------------------------------"))
    print(f"""
    Results:
    {results}
    """)
ofkjgds = input("DONE!\n\nHit ENTER To Exit.")
