def totalsum(listenavn):
    total = 0
    for tall in listenavn:
        if isinstance(tall, int) or isinstance(tall, float):
            total += tall
    return(total)

def gjennomsnitt(listenavn):
    total = totalsum(listenavn)
    antall = len(listenavn)
    gjennomsnitt = total/antall
    return gjennomsnitt

def størst(listenavn):
    return(max(listenavn))

def minst(listenavn):
    return(min(listenavn))