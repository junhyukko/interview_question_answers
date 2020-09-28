import os 
from pikepdf import Pdf

curr_dir = os.getcwd() + "\\interview_questions_answers"
output_dir = curr_dir + "\\Cracking the Coding Interview Solutions"
chapter1 = output_dir + "\\Chapter 1 Arrays and Strings"
chapter2 = output_dir + "\\Chapter 2 Linked Lists"
chapter3 = output_dir + "\\Chapter 3 Stacks and Queues"
chapter4 = output_dir + "\\Chapter 4 Trees and Graphs"
chapter5 = output_dir + "\\Chapter 5 Bit Manipulation"
chapter6 = output_dir + "\\Chapter 6 Brain Teasers"
chapter7 = output_dir + "\\Chapter 7 Object Oriented Design"
chapter8 = output_dir + "\\Chapter 8 Recursion"
chapter9 = output_dir + "\\Chapter 9 Sorting and Searching"
chapter10 = output_dir + "\\Chapter 10 Mathematical"
chapter11 = output_dir + "\\Chapter 11 Testing"
chapter12 = output_dir + "\\Chapter 12 System Design and Memory Limits"
chapter13 = output_dir + "\\Chapter 13 C++"
chapter14 = output_dir + "\\Chapter 14 Java"
chapter15 = output_dir + "\\Chapter 15 Databases"
chapter16 = output_dir + "\\Chapter 16 Low Level"
chapter17 = output_dir + "\\Chapter 17 Networking"
chapter18 = output_dir + "\\Chapter 18 Threads and Locks"
chapter19 = output_dir + "\\Chapter 19 Moderate"
chapter20 = output_dir + "\\Chapter 20 Hard"

pdf = Pdf.open(curr_dir + "\\Interview_Q_A.pdf")

for n, page in enumerate(pdf.pages):
    dst = Pdf.new()
    dst.pages.append(page)
    dst.save('{:02d}.pdf'.format(n))