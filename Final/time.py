t=int(input("What's your time?"))
que_3=input('''WHAT IS THE UNIT OF YOUR TIME,
CHOOSE FROM THE UNITS IN THE BRACKETS BELOW
SECONDS(S),
MINUTES(MIN)
HOURS(HRS),
MILLISECONDS(ms)
MEGASECONDS(Ms)''')
if que_3 == 's' or 'S' :
    t=t
elif que_3=='MIN' or'Min' or 'min' :
        t*=60
elif que_3== 'HRS' or 'Hrs' or 'hrs' :
    t*=3600
elif que_3== 'ms':
    t*=1000
elif que_3 == 'MS' or 'Ms' :
    t/=1000   