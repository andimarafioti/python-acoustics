import A5Part1TRUE

x = []
freq = []
a = []
fErr = []

for f in range(100,2020,2):
    x.append([44100,A5Part1TRUE.genSine(f)])
    freq.append(f)
    
    
for i in range(len(freq)):
    a.append(A5Part1TRUE.minFreqEstErr(x[i],freq[i]))
    fErr.append(freq[i]-a[i][0])
    if abs(fErr[i]) > 0.05:
        print 'Error!' 
        break

