##Data retrieval functions

import urllib2

#returns a list of strings of each stat for a given event and year
def ParseWebData(event,year):

    count=0
    totalT=[]
    gender=[]
    ageclass=[]
    swimT=[]
    t1T=[]
    bikeT=[]
    t2T=[]
    runT=[]
    
    
    urlstring="http://www.chiptimeresults.com/resultsreader.php?y=%s&r=%s.htm" % (year,event)
    data=urllib2.urlopen(urlstring)

    for line in data.readlines():
        if len(line)==153 and line[0:2]!="DQ":
            totalT.append(line[37:44])
            gender.append(line[46])
            ageclass.append(line[47:53])
            swimT.append(line[70:75])
            t1T.append(line[84:88])
            bikeT.append(line[97:102])
            t2T.append(line[110:114])
            runT.append(line[123:128])
            count+=1

##    for i in range(count):
##        print totalT[i],gender[i],ageclass[i],swimT[i],t1T[i],bikeT[i],t2T[i],runT[i]

    return[count,totalT,gender,ageclass,swimT,t1T,bikeT,t2T,runT]

ParseWebData("joesteamT",2012)

