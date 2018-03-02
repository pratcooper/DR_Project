import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import *
from nltk.corpus import wordnet as wn
import re
import csv
import gensim
import numpy as np
import pickle
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
from textstat.textstat import textstat


#nltk.download('wordnet')
#nltk.download('punkt') # if necessary...
document1 = "This code prints hello world to the console"
document2 = "int helloWorld(){ (\" hi world \"); "
java_keyword = ['abstract','assert','boolean','break','byte','case','catch','char','class','const','continue','default','double','else','enum','extends','final','finally','float','for','if','implements','import','instanceof','int','interface','long','new','package','private','protected','public','return','short','static','super','switch','synchronized','this','throw','throws','transient','try','void','volatile','while']
label_dict = pickle.load(open( "save.p", "rb" ))

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower().split()


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


'''remove punctuation, lowercase, stem'''
################ Normalize function for TFVectorizer ####################
def normalize(text):
    #list_of_tok = stem_tokens(nltk.word_tokenize(text.translate(remove_punctuation_map)))
    list_of_tok = nltk.word_tokenize(text.translate(remove_punctuation_map))

    result_list_tokens = []
    for item in list_of_tok:
        if item not in java_keyword:
            res = convert(item)
            for i in res:
                result_list_tokens.append(i)

    return result_list_tokens
##########################################################################


######################Normalize function for Raw vectorizer###########################
def raw_normalize(text):
    return stem_tokens(nltk.word_tokenize(text.translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english',lowercase = False)
raw_vectorizer = TfidfVectorizer()
##########################################################################


#########################Cosine similarity using TF-IDF Vectorizer#####################
def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    # print(tfidf)
    return ((tfidf * tfidf.T).A)[0, 1]

#######################################################################################


######################Raw Cosine Similarity######################################
def raw_cosine_sim(text1, text2):
    tfidf = raw_vectorizer.fit_transform([text1, text2])
    # print(tfidf)
    return ((tfidf * tfidf.T).A)[0, 1]
##########################################################################


##########################################################################
def getSynonyms(word):
    synonymSet = set()
    for i, j in enumerate(wn.synsets(word)):
        # print ("Meaning",i, "NLTK ID:", j.name())
        # print ("Definition:",j.definition())
        # print ("Synonyms:", ", ".join(j.lemma_names()))
        for k in j.lemma_names():
            # print(k.type)
            synonymSet.add(k)

    # print (synonymSet)
    return synonymSet
##########################################################################


##########################################################################
def replaceSynonyms(text1, text2):
    text1 = text1.split(" ")
    text2 = text2.split(" ")
    for i in text1:
        # print (i + " is i")
        synList = getSynonyms(i)
        for j in synList:
            # print (j + " " + "is j")
            for k in range(len(text2)):
                if j == text2[k] and j != i:
                    # print("Changing here" + j + " " + i)
                    text2[k] = i

    return text1, text2
##########################################################################

##########################################################################
def getPair(line):

    counter = 0
    codeList = []
    commentList = []

    while(counter<len(line)):
        methodInfo = line[counter+0]
        pathToMain = line[counter+1]
        #print(line[1])
        commentLength = int(line[counter+2])

        comment = []
        for i in range(commentLength):
            comment.append(line[counter + i + 3])
        commentString = ' '.join(comment)
        commentList.append(commentString)
        codeLength = int(line[counter+ 3 + commentLength])

        code = []
        for i in range(codeLength):
            code.append(line[counter + i+4+commentLength])
        codeString = ' '.join(code)
        codeList.append(codeString)
        end = counter + commentLength+codeLength+5
        counter = end
        #print(counter)
    return codeList,commentList
##########################################################################


##########################################################################
def operandSynonyms(document1, document2):
    # hashmap = { "+" : "sum" , "-" : "divides", "*" : "multiplication", "/" : "multiplication" }
    if ("+" in document2):
        # print("Here")
        document2 = document2.replace("+", "addition")
    if ("-" in document2):
        document2 = document2.replace("-", "subtract")
    if ("*" in document2):
        document2 = document2.replace("*", "multiplie")
    if ("/" in document2):
        document2 = document2.replace("/", "divide")

    # print (document2)
    return document1, document2
##########################################################################

##########################################################################
def runCosineSim(document1,document2):
    #print("Original text")
    #print(document1)
    #print(document2)
    cosine_before = cosine_sim(document1, document2)
    #print("cosine_before :" , cosine_before )
    text1, text2 = replaceSynonyms(document1, document2)
    #print('replaced text :', text2)
    text1 = ' '.join(text1)
    text2 = ' '.join(text2)
    #print("Preprocessed text")
    #print(text1)
    #print(text2)
    cosine_after  = cosine_sim(text1, text2)
    #print("cosine_after :", cosine_after)
    #if cosine_before != cosine_after:
        #print("Values changed")

    return cosine_after
##########################################################################


##########################################################################
def runRawCosineSim(document1,document2):
    raw_res_cosine = raw_cosine_sim(document1, document2)
    return raw_res_cosine
##########################################################################

##########################################################################
def runCosineSimWord2Vec(document1,document2,model):

    result_vec_code = np.zeros(shape=(300,))
    count_comment_zero = 0
    count_code_zero = 0
    for word in document1:
        try:
            word_vec = model[word]
        except KeyError:
            word_vec = 0
            count_code_zero = count_code_zero + 1
        result_vec_code = np.add(result_vec_code,word_vec)

    result_vec_code = np.divide(result_vec_code,(len(document1) - count_code_zero))

    result_vec_comment = np.zeros(shape=(300,))
    for word in document2:
        try:
            word_vec = model[word]
        except KeyError:
            word_vec = 0
            count_comment_zero = count_comment_zero + 1
        result_vec_comment = np.add(result_vec_comment, word_vec)

    result_vec_comment = np.divide(result_vec_comment, (len(document2) - count_comment_zero))

    numerator = np.dot(result_vec_code,result_vec_comment)
    dinominator = np.multiply(np.linalg.norm(result_vec_code),np.linalg.norm(result_vec_comment))

    #cosine_similar= float(numerator/dinominator)
    #cosine_similar = 1 - sp.spatial.distance.cosine(result_vec_code,result_vec_comment)
    #cosine_similar = cosine_similarity(result_vec_code,result_vec_comment)

    cosine_similar = numerator/float(dinominator)
    return cosine_similar
##########################################################################


##########################################################################
def create_list_var_api_returnvar(code,find_ret,find_var,find_api,find_method_name):
    lines = code.split('\n')
    list_var = []
    api_calls_list = []
    return_var_list = []
    method_name_list = []
    method_name_found = False

    for line in lines:
        ##### populate list of return variables ######
        if find_ret:
            if "return" in line:
                found_return = True
                list = re.split(' ',line)
                return_variable = list[list.index("return") + 1]
                if return_variable:
                    if return_variable.endswith(';'):
                        return_variable = return_variable[:-1]
                return_var_list.append(return_variable)

        ######## populate list of api calls variables#######
        if find_api:
            api = re.findall(r'\([^()]*\)', line)
            if api:
                if '+' not in api and '-' not in api and '*' not in api and '/' not in api:
                    #print("API :", api)
                    api_call_name_index = line.find('(')
                    api_call_name = ""
                    while (line[api_call_name_index] != ' ' and line[api_call_name_index] != '.'):
                        #print("index :", api_call_name_index)
                        api_call_name = api_call_name + line[api_call_name_index - 1]
                        api_call_name_index = api_call_name_index - 1
                    res = api_call_name[::-1]
                    if res[0] == '.' or res[0] == ' ':
                        res = res[1:]
                    api_calls_list.append(res)

        #######  populate list of variables  #######
        #print("line :" , line)
        if find_var:
            firstEqual = line.find('=')
            if firstEqual != -1:
                subStr = line[:firstEqual]
                #print(subStr)
                list_splitted = subStr.strip().split(' ')
                if list_splitted[len(list_splitted) - 1][0].isalpha():
                    var_i = list_splitted[len(list_splitted) - 1]
                else:
                    var_i = list_splitted[len(list_splitted) - 2]
                #print(var_i)

                if '.' in var_i:
                    var_i = var_i.split('.')[1]
                list_var.append(var_i)

        if find_method_name and (not method_name_found):
            api = re.findall(r'\([^()]*\)', line)
            if api:
                if '+' not in api and '-' not in api and '*' not in api and '/' not in api:
                    # print("API :", api)
                    api_call_name_index = line.find('(')
                    api_call_name = ""
                    while (line[api_call_name_index] != ' ' and line[api_call_name_index] != '.'):
                        # print("index :", api_call_name_index)
                        api_call_name = api_call_name + line[api_call_name_index - 1]
                        api_call_name_index = api_call_name_index - 1
                    res = api_call_name[::-1]
                    if res[0] == '.' or res[0] == ' ':
                        res = res[1:]
                    method_name_list.append(res)
                    method_name_found = True

    return return_var_list,list_var,api_calls_list,method_name_list
##########################################################################

if __name__=="__main__":
    resCosineValList = []
    resRawCosineValList = []
    with open("/Users/pratnaik/PycharmProjects/code_comments-master/Benchmark_Raw_Data.txt") as f:
        lines = f.readlines()

        codeList, commentList = getPair(lines)
        cnt = 1

        model = gensim.models.KeyedVectors.load_word2vec_format('/Users/pratnaik/PycharmProjects/code_comments-master/code_comments_w2v.bin', binary=True)
        f1 = open("coherent.txt", "a")
        f2 = open("non_coherent.txt", "a")
        feature_file = open('feature_file.txt', 'a')
        with open("/Users/pratnaik/PycharmProjects/code_comments-master/Points.csv", 'w') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            for i,j in zip(codeList,commentList):
                print('Data Point :' ,cnt)
                #################### similarity functions ##############
                res_cosine = runCosineSim(i, j)
                raw_res_cosine = runRawCosineSim(i,j)
                res_cosine_word2vec = runCosineSimWord2Vec(i,j,model)
                resRawCosineValList.append(raw_res_cosine)
                resCosineValList.append(res_cosine)
                #################### Print similarity functions ######################
                print("Raw Cosine Similarity value:",raw_res_cosine)
                print("Modified Cosine Similarity using features:", res_cosine)
                print("Modified Cosine Similarity using word2vec:", res_cosine_word2vec)
                print("-----------")
                ##########################get method name and comment similarity##############################
                a,b,c,method_name = create_list_var_api_returnvar(i,False,False,False,True)
                method_comment_sim_score = 0

                if len(method_name)!= 0:
                    method_string = ""
                    unCamaledMethod = convert(method_name[0])
                    for item in unCamaledMethod:
                        method_string = method_string + item
                        method_string+= " "

                    method_string = method_string.strip()
                    method_comment_sim_score = runCosineSim(method_string,j)

                ######################################################################
                dataPoint = str(cnt) + ' ' + str(res_cosine) + ' ' + str(len(j)) + '\n'
                feature_file.write(dataPoint)
                ############## calculate readability score for comment ###############
                test_data = j
                score = 0.0
                num_of_metrics = 9
                score += textstat.flesch_reading_ease(test_data)
                score += textstat.smog_index(test_data)
                score += textstat.flesch_kincaid_grade(test_data)
                score += textstat.coleman_liau_index(test_data)
                score += textstat.automated_readability_index(test_data)
                score += textstat.dale_chall_readability_score(test_data)
                score += textstat.difficult_words(test_data)
                score += textstat.linsear_write_formula(test_data)
                score += textstat.gunning_fog(test_data)

                score = score/float(num_of_metrics)
                ######################################################################
                if str(cnt) in label_dict["COHERENT"]:
                    wr.writerow([cnt, "COHERENT", float(res_cosine_word2vec), len(j),float(score),float(method_comment_sim_score)])
                else:
                    wr.writerow([cnt, "NON_COHERENT", float(res_cosine_word2vec), len(j) ,float(score),float(method_comment_sim_score)])
                cnt = cnt + 1

            feature_file.close()
    with open("/Users/pratnaik/PycharmProjects/code_comments-master/data.csv",'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i,j in zip(resCosineValList,resRawCosineValList):
            wr.writerow([float(i),float(j)])

