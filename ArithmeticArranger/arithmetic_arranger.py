def arithmetic_arranger(problems, display_result=False):
    

    topOperand = []
    bottomOperand = []
    dividers = []
    results = []


    #Ensure a maximum of 5 problems can be passed into function
    if len(problems) >= 6:
        return "Error: Too many problems."

    for equation in problems:


        #Split inputted problems into n1 (1st number), sign(+/-) and n2 (2nd number)
        n1, sign, n2 = equation.split()


        #Check inputs are digits, max length of 4 and only uses + or -
        if not (n1.isdigit() and n2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if sign not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."
        

        #Calculate result of sum
        result = int(n1) + int(n2) if sign == "+" else int(n1) - int(n2)


        #Format lines correctly 
        topLine = len(n1)
        bottomLine = len(f"{sign} {n2}")

        if len(n1) > len(n2):
            n1 = f"  {n1}"
            n2 = f"{n2:>{topLine}}"
            result = f"{result:>{len(n1)}}"
        else:
            n1 = f"{n1:>{bottomLine}}"
            n2 = f"{n2}"
            result = f"{result:>{bottomLine}}"


        #Make sure dashes run the length of the sum 
        dash = "-" * len(str(n1))
        

        #Append lists of formatted outputs
        topOperand.append(f"{n1}")
        bottomOperand.append(f"{sign} {n2}")
        dividers.append(dash)
        results.append(result) 


    #Arrnage so all formatted outputs are spaces 4 apart
    arranged_problems = "    ".join(topOperand) + "\n"
    arranged_problems += "    ".join(bottomOperand) + "\n"
    arranged_problems += "    ".join(dividers)


    #Only print results when 'True' is passed into the function
    if display_result:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems