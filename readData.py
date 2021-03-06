import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pylab, random, string, copy, math

import csv
from collections import defaultdict
import operator
from datetime import datetime, date, time
from datetime import timedelta


def mapHeader():
    header = ['user.bi_followers_count', 'user.domain', 'user.avatar_large', 'user.statuses_count', 'user.allow_all_comment', 'user.id', 'user.city', 'user.province', 'user.follow_me', 'user.verified_reason', 'user.followers_count', 'user.location', 'user.mbtype', 'user.profile_url', 'user.block_word', 'user.star', 'user.description', 'user.friends_count', 'user.online_status', 'user.mbrank', 'user.idstr', 'user.profile_image_url', 'user.allow_all_act_msg', 'user.verified', 'user.geo_enabled', 'user.screen_name', 'user.lang', 'user.weihao', 'user.remark', 'user.favourites_count', 'user.name', 'user.url', 'user.gender', 'user.created_at', 'user.verified_type', 'user.following', 'reposts_count', 'favorited', 'truncated', 'text', 'created_at', 'mlevel', 'idstr', 'mid', 'visible', 'attitudes_count', 'in_reply_to_screen_name', 'source', 'in_reply_to_status_id', 'comments_count', 'geo', 'id', 'in_reply_to_user_id']
    dicth = {}
    m = 0
    for h in header:
        dicth[h] = m
        m = m + 1
    return dicth

def readBrandIntoDict():
   
    reader = open('brandNames.csv', 'r')
    result = {}
    for line in reader:
        brands_list = line.split(',')
    for i in brands_list:
        j = i.decode('utf-8')
        result[j] = [0]*31
    return result

def readCSV(fName):
    
    reader = csv.reader(open(fName))

    brandsDict=readBrandIntoDict()
    for line in reader:
        if len(line) < 53:
            continue
        #uid = line[mapHeader()['user.id']]
        #uidList.append(uid)
        
        text = line[mapHeader()['text']]
        text_decoded = text.decode('utf-8')
        #textList.append(text_decoded)
        #loc = line[mapHeader()['user.location']]
        #loc_decoded = loc.decode('utf-8')
        #locList.append(loc_decoded)
        #gender = line[mapHeader()['user.gender']]
        #genderList.append(gender)
        time = line[mapHeader()['created_at']]
        
        #Sat Feb 09 21:29:29 +0800 2013
        try:
            time_notimezone = time[0:20] + time[26:]
            dtime = datetime.strptime(time_notimezone, '%a %b %d %H:%M:%S %Y')
                
        except ValueError:
            continue
        
        for b in brandsDict.keys():
            if b in text_decoded:
                brandsDict[b][dtime.day -1] = brandsDict[b][dtime.day -1]+1

    return brandsDict


def exportBrandsDict(fName):
    writer = csv.writer(open('BrandsMonthlyTrends.csv', 'wb'))
    brandsDict = readCSV(fName)
    for key,value in brandsDict.items():
        key_encode = key.encode('utf-8')