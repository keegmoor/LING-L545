import sys
para = sys.stdin.read()
trades = ['.',',', '(', ')', ':', ';']
for t in trades:
    para = para.replace(t, " " + t + " ")

para = para.replace("  ", " ")
para = para.replace(" ", "\n")
print(para)
