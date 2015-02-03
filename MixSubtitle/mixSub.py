import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime

chsFile = '/Users/vpon/Desktop/chs.srt'
engFile = '/Users/vpon/Desktop/Eng.srt'
outFile = open('/Users/vpon/Desktop/output.srt','w');

chineseList = []
engList = []
MixItemList = []
sStr = '-->'

class Format_item():
    def __init__(self):
        self.id = 0
        self.time = ''
        self.start = ''
        self.end = ''
        self.subtitle_chs = []
        self.subtitle_eng = []

def store_id_time(line):
    line = u'%s' % line
    line = line.strip('\r\n').strip('\n')
    if line.isnumeric() == True:
        # global variable using for UnboundLocal error
        global s 
        s = Format_item()
        s.id = line
    elif line.find(sStr) > 0:
        s.time = line
    return s

def startTime(chstime,engtime):
    TIME_FORMAT = '%H:%M:%S,%f'
    ch_start = chstime.split(' --> ')[0]
    eng_start = engtime.split(' --> ')[0]
    datetime.strptime(ch_start,TIME_FORMAT)
    datetime.strptime(eng_start,TIME_FORMAT)
    if ch_start <= eng_start:
        return ch_start
    elif ch_start > eng_start:
        return eng_start

def endTime(chstime,engtime):
    TIME_FORMAT = '%H:%M:%S,%f'
    ch_end = chstime.split(' --> ')[1]
    eng_end = engtime.split(' --> ')[1]
    datetime.strptime(ch_end,TIME_FORMAT)
    datetime.strptime(eng_end,TIME_FORMAT)
    if ch_end <= eng_end:
        return eng_end
    elif ch_end > eng_end:
        return ch_end

def is_subtitle(line):
    line = u'%s' % line
    line = line.strip('\r\n').strip('\n')
    if(line.isnumeric() != True and line.find(sStr) < 0 and line.strip() != ''):
        return True
    else: 
        return False

def getChineseItemList(Filename):
    with open(Filename, 'r') as infile:
        for line in infile:
            s = store_id_time(line)
            if is_subtitle(line) == True:
                s.subtitle_chs.append(line)
            elif line.strip() == '':
                chineseList.append(s)
        return chineseList

def getEngItemList(Filename):
    with open(Filename,'r') as infile2:
        for line in infile2: 
            s = store_id_time(line)
            if is_subtitle(line) == True:
                s.subtitle_eng.append(line)
            elif line.strip() == '':
                engList.append(s)
        return engList

def getMixItemList(chs,eng):
    for a in chs:
        for b in eng:
            if a.time == b.time:
                global s 
                s = Format_item()
                s.id = a.id
                s.start = startTime(a.time,b.time)
                s.end = endTime(a.time,b.time)
                s.subtitle_chs = a.subtitle_chs
                s.subtitle_eng = b.subtitle_eng
                MixItemList.append(s)
    return MixItemList

def writeMixItemListToFile(mixItem,filename):

    for m in mixItem:
        filename.write(m.id + '\n')
        filename.write(m.start + ' --> ' + m.end + '\n')
        for schs in m.subtitle_chs:
            filename.write(schs)
        for seng in m.subtitle_eng:
            filename.write(seng)
        filename.write('\n')

chineseList = getChineseItemList(chsFile)
engList = getEngItemList(engFile)
mixList = getMixItemList(chineseList,engList)
writeMixItemListToFile(mixList,outFile)


