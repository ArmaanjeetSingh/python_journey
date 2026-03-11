def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("HALT!!")
        print("THIS TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        
    if text == "*":
        print("*"*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)
        
banner_text("*")
banner_text("Always look on the brighter side of life")
banner_text("If life seems jolly rotten")
banner_text("And that's to laugh and smile dance and sing,")
banner_text(" ")
banner_text("When you are feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("*")