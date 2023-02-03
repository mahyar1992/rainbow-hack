import hashlib
import csv
with open('output file directory here', 'w') as fout: #csv format
    with open('input file directory here') as fin: #csv format
        reader = csv.reader(fin)
        dict_password = {}
        list_javab = []
        for each_ramz in range (0, 10000):
            if each_ramz < 10:
                each_ramz_string = '000'+ str(each_ramz)
            elif 10 <= each_ramz < 100:
                each_ramz_string = '00' + str(each_ramz)
            elif 100 <= each_ramz< 1000:
                each_ramz_string = '0' + str(each_ramz)
            else:
                each_ramz_string = str(each_ramz)
            hashed_ramz = hashlib.sha256(each_ramz_string.encode('utf-8')).hexdigest()
            dict_password[hashed_ramz] = each_ramz_string
        for row in reader:
            name = row[0]+','
            hashed_pass = row[1]
            for items in list(dict_password.keys()):
                javab = ''
                if items == hashed_pass:
                    javab = name+str(dict_password[items])
                list_javab = list_javab + javab.split()
        fout.write('/n'.join(list_javab))