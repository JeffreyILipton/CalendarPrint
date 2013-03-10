
timeMin='2013-03-08T00:00:00Z'
def duration(start, end):
        [sdate, stime] = start.split('T')
        [edate,etime] = end.split('T')
        
        startList = stime.split('-')[0].split(':')
        smin = float(startList[0])*60.0+float(startList[1])
        
        
        endList = etime.split('-')[0].split(':')
        
        emin = float(endList[0])*60.0+float(endList[1])
        
        delta = emin-smin
        return delta
        
    