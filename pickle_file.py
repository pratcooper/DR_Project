import pickle
import os
import io

label_dict = {}

cwd = os.getcwd()
filename = "/label"
coherent_list = []
non_coherent_list = []
with open(cwd+filename, "r") as f:
    for line in f:
        line = line.strip()
        words = line.split(", ")
        if words[1] == "COHERENT":
            coherent_list.append(words[0])
        else:
            non_coherent_list.append(words[0])


label_dict['COHERENT'] = coherent_list
label_dict['NON_COHERENT'] = non_coherent_list


pickle.dump(label_dict, open("save.p", "wb"))


label_dict = pickle.load(open( "save.p", "rb" ))

#print(label_dict['COHERENT'])