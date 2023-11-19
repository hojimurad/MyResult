


def comment(text:str,symbols:list):
    j =0
    for i in range(len(text.split())):
        if text[i] in symbols:
            text.replace(str(text[i+1]),"")


    return text


print(comment("allps,pears # and anananas \ngrapes bababas !apple",["#","!"]))