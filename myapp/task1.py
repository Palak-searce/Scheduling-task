from datetime import date, timedelta
import json
import copy

def prev_date(init_date):
    year, month, day = map(int,init_date.split("-"))
    temp_date = date(year, month, day)
    new_date = temp_date - timedelta(days = 1)
    return str(new_date)

def next_date(init_date):
    year, month, day = map(int,init_date.split("-"))
    temp_date = date(year, month, day)
    new_date = temp_date + timedelta(days = 1)
    return str(new_date)


def update(users,uName,profile,s,e):
    cnt = -1
    temp = copy.deepcopy(users[uName])
    collide = False
    index = 0
    for u in users[uName]:
        cnt += 1
        profile1 = u["profile"]
        s1 = u["sDate"]
        e1 = u["eDate"]
        
        if e < s1:
            break

        # first test case
        # |_______|
        #     |_________|
        if s1 < s < e1 < e:
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                s = s1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                temp[cnt]["eDate"] = prev_date(s)

        # second test case
        #         |___________|
        # |_________|
        elif s < s1 < e < e1:
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                e = e1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                temp[cnt]["sDate"] = next_date(e)

        # third test case
        # |_________|
        # |_________|
        elif (s1 == s) and (e1 == e):
            if not collide:
                collide = True
                index += 1
            # delete
            temp.remove(u)
            cnt -= 1

        # forth test case
        # |___________________|
        #      |_______|
        elif s1 < s <= e< e1:
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                s = s1
                e = e1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                #create new with s_new = e and e_new = e1
                temp[cnt]["eDate"] = prev_date(s)
                temp.insert(cnt+1,{"profile":profile1,"sDate":next_date(e),"eDate":e1})
                # temp[cnt]["eDate"] = prev_date(s)
                cnt += 1

        # fifth test case
        # |__________|
        # |_______|
        elif ((s1 == s) and (e < e1)) or ((s1 == s) and (s == e)):
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                e = e1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                temp[cnt]["sDate"] = next_date(e)

        # sixth test case
        # |___________|
        #    |________|
        elif ((s1 < s) and (e1 == e)) or ((e1 == e) and (s == e)):
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                s = s1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                temp[cnt]["eDate"] = prev_date(s)

        # seventh test case
        # |______|
        # |___________|
        elif ((s1 == s) and (e1 < e)) or ((s1 == s) and (s1 == e1)):
            if not collide:
                collide = True
                index += 1
            # delete
            temp.remove(u)
            cnt -= 1

        #eigth test case
        #     |____|
        # |________|
        elif ((e == e1) and (s < s1)) or ((e == e1) and (e1 == s1)):
            if not collide:
                collide = True
                index += 1
            # delete
            temp.remove(u)
            cnt -= 1

        # nineth test case
        # |_________|
        #           |_______|
        elif (e1 == s) and (s1 < s < e):
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                s = s1
                # delete
                temp.remove(u)
                cnt =- 1
            else:
                temp[cnt]["eDate"] = prev_date(s)

        # tenth test case
        #           |_________|
        # |_________|
        elif (e == s1) and (s < e < e1):
            if not collide:
                collide = True
                index += 1
            if profile == profile1:
                e = e1
                # delete
                temp.remove(u)
                cnt -= 1
            else:
                temp[cnt]["sDate"] = next_date(e)
            
        # eleventh test case
        #      |______|
        # |________________|
        elif s < s1 <= e1 < e:
            if not collide:
                collide = True
                index += 1
            # delete
            temp.remove(u)
            cnt -= 1
        
        # no overlaping
        else:
            index += 1
            #do nothing

    temp.insert(index,{"profile":profile,"sDate":s,"eDate":e})
    users[uName] = temp[:]
    f_write = open("./data.json","w")
    json.dump(users,f_write)
    f_write.close()



def insert_profile(uName,profile,sDate,eDate): 
    f_read = open("./data.json","r")
    users = json.load(f_read)
    if uName in users.keys():
        update(users,uName,profile,sDate,eDate)      
    else:
        users[uName] = [{"profile":profile,"sDate":sDate,"eDate":eDate}]
        f_write = open("./data.json","w")
        json.dump(users,f_write)
        f_write.close()

    f_read.close()
    print("Data entered and updated successfully !!!")

def show_all_profile():
    f_read = open("data.json","r")
    users = json.load(f_read)
    return users

def get_single_user(uName):
    f_read = open("data.json","r")
    users = json.load(f_read)
    return users[uName]
