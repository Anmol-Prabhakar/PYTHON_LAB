sequence = 'helloworld'
uniquel = set(sequence)
upper = list(map(lambda x: (x.upper(),x.lower()),uniquel))
print(uniquel)