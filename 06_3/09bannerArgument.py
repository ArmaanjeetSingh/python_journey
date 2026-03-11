def banner_text(text = " ",screen_width = 100):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified widh {1}".format(text,screen_width))
    if text == "*":
        print("*"*screen_width)
    else:
        centered_text = text.center(screen_width-4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)
        
banner_text("*",30)
banner_text("Always look on the brighter side of life",66)
banner_text("If life seems jolly rotten",66)
banner_text("And that's to laugh and smile dance and sing,")
banner_text(screen_width=70)
banner_text("When you are feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("*")