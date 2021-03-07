import os
import re

# settings
subSuffix = ('ass')
audioSuffix = ('mkv', 'mp4')
###
subCount = {"normal" : 1}  # sc,tc for chinese
audioCount = 1

name = input('please input name:')

for i in os.listdir() :
    suffix = i.split('.')[-1]
    if suffix.lower().endswith(audioSuffix) :
        os.rename(i, name + ' - %02d.%s'%(audioCount, suffix))
        audioCount += 1
    elif suffix.lower().endswith(subSuffix) :
        if '.sc.' in i.lower() or '.jpsc.' in i.lower() :
            sc = subCount.get('sc')
            if sc is None :
                sc = 1
                subCount['sc'] = sc
            os.rename(i, name + ' - %02d.sc.%s'%(sc, suffix))
            subCount['sc'] += 1
        elif '.tc.' in i.lower() or '.jptc.' in i.lower() :
            tc = subCount.get('tc')
            if tc is None :
                tc = 1
                subCount['tc'] = sc
            os.rename(i, name + ' - %02d.tc.%s'%(tc, suffix))
            subCount['tc'] += 1
        else :
            os.rename(i, name + ' - %02d.%s'%(subCount['normal'], suffix))
            subCount['normal'] += 1
