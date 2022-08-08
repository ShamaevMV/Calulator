x = open("calulator.py", "w")

calc_range = 20
wt = x.write

wt("def main():\n")
wt("\twhile True:\n")
wt("\t\tstr_to_calulate = input(\"enter numbers to calulate: \")\n")
wt("\t\tif str_to_calulate ==\"\": break\n")
wt("\t\tprint(calulator(str_to_calulate))\n\n")


wt("def calulator(stc):\n")
for i in range(calc_range):
    for ii in range (calc_range):
        x.write(f"\tif stc == \"{i}*{ii}\": return {i*ii}\n")

wt("\nif __name__ == \"__main__\":\n\tmain()")
x.close()
