from datetime import date

def getStringDate():
    return date.today().strftime('%B %d, %Y')
    #return 'February 14, 2021'