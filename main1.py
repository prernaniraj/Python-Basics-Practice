def do_stuff(num):
    try:
        if num :
            num = int(num)
            return num+5
    except ValueError :
        return "Please enter number"