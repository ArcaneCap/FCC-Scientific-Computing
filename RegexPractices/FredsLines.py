#Identify each line spoken by Fred. Then put them in a list. (Note that quotes is a multi-line string
#Expected result:
#lines = ['Fred Weasley: Honestly, woman. You call yourself our mother.', Fred Weasley: I’m only joking, I am Fred!]

import re

quotes = """
Molly Weasley: Fred, you next.
George Weasley: He’s not Fred, I am!
Fred Weasley: Honestly, woman. You call yourself our mother.
Molly Weasley: Oh, I’m sorry, George.
Fred Weasley: I’m only joking, I am Fred!"""

match = re.findall(r"(Fred Weasley: .+)", quotes)

lines = []
for i in match:
    lines.append(i)

print(lines)
