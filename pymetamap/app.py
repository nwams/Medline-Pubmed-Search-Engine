from pymetamap import MetaMap
import csv
from flask import Flask, render_template, request, session, send_from_directory, g, redirect, url_for, abort, flash
import os
import json

# create the application object
app = Flask(__name__)

#when the user comes to the main page, send them to the home template
@app.route('/')
def main():
    return render_template('home.html')

def getCPTcodes():
    """
    get CPT codes, put in dictionary
    :return: the dictionary of codes
    """
    with open('../codes/CPT.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {"t"+str(rows[0]):rows[1] for rows in reader}
        return codeDict

def getICDcodes():
    """
    get ICD codes, put in dictionary
    :return: the dictionary of codes
    """
    with open('../codes/ICD.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {"t"+str(rows[0]):rows[1] for rows in reader}
        return codeDict

cptCodeDict = getCPTcodes()
icdCodeDict = getICDcodes()

def searchThroughCodes(searchTerms, numOfSearches):
    """
    search through the list of IPT/CPT codes.
    if the users topic matches, via UMLS terms, assign it to a dictionary
    :param codeDict: dictionary of all IPT/CPT codes
    :param searchTerms: array of UMLS Concept preferred_names
    :param numOfSearches: number of names in Concept the array
    :return: matchingTopicsDict
    """
    matchingCPTDict = {}
    matchingICDDict = {}
    for i in range(numOfSearches):
        for k,v in cptCodeDict.iteritems():
            if searchTerms[i].lower() in v.lower(): # case insensitive search required
                matchingCPTDict[k] = v

    for i in range(numOfSearches):
        for k,v in icdCodeDict.iteritems():
            if searchTerms[i].lower() in v.lower(): # case insensitive search required
                matchingICDDict[k] = v

    print "================== CPT codes ================"
    print matchingCPTDict
    print "================== ICD codes ================"
    print matchingICDDict
    return matchingCPTDict, matchingICDDict

def searchMetaMap(search):
    """
    setup MetaMap and search UMLS for user desired topic
    :return: The preferred name for the UMLS concept identified in the text. And the number of different preferred names output
    """
    # mm = MetaMap.get_instance('/Users/nwams/Documents/MetaMap/public_mm/bin/metamap12')
    mm = MetaMap.get_instance('/Users/nwams/Documents/MetaMap/public_mm/bin/metamap12')
    
    #searchTopic = raw_input('What topic are you searching for? ')
    searchTopic = [search]

    # [1] only allow user to search for one topic at a time
    concepts, error = mm.extract_concepts(searchTopic, [1])

    conceptArray = []
    for concept in concepts:
        conceptArray.append(concept.preferred_name)
    #print "UMLS terms = ", conceptArray

    return conceptArray, len(conceptArray)


@app.route('/search')
def search():
    # We receive the parameter called search from GET (Ajax) request
    search = request.args.get('search')

    conceptArray, lengthOfConceptArray = searchMetaMap(search)
    result1, result2 = searchThroughCodes(conceptArray, lengthOfConceptArray)
    results = {}
    results["procedures"] = result1
    results["symptoms"] = result2

    # Return the results as a json object
    return json.dumps(results, encoding="ISO-8859-1")


""" start the development server using the run method"""
if __name__ == "__main__":
    app.debug = True
    #app.run(debug=True)
    #app.run(debug=True, port=5001)
    #app.run(host='0.0.0.0')   #turn this on later when you go to another server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


def getPubMedArticleID():
    """

    :return: a dictionary key: term, value: set of pubmedID(s)
    """
    with open('../pubmed_data/MH_items.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        dict = {}
        for row in reader:
            term = row[0].lower() # case insensitive
            pubmedID = row[3]
            if dict.has_key(term) == False:
                dict[term] = set()
            dict[term].add(pubmedID)
        return dict

def searchPubMedArticleByConcept(conceptArray):
    dict = {}
    for concept in conceptArray:
        concept = concept.strip().lower()
        if pubmedDict.has_key(concept) == True:
            dict[concept] = pubmedDict[concept]
            print "Found " + str(len(pubmedDict[concept])) + " articles on PubMed for [" + concept + "]."
        else:
            print "No keyword matches [" + concept + "] in database."
    return dict

def getCPTcodes():
    """
    get CPT codes, put in dictionary
    :return: the dictionary of codes
    """
    with open('../codes/CPT.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {rows[0]:rows[1] for rows in reader}
        return codeDict

def getICDcodes():
    """
    get ICD codes, put in dictionary
    :return: the dictionary of codes
    """
    with open('../codes/ICD.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {rows[0]:rows[1] for rows in reader}
        return codeDict

"""
# return a dictionary with key as CPT or ICD code and value as text description
cptCodeDict = getCPTcodes()
icdCodeDict = getICDcodes()
# pubmedDict = getPubMedArticleID()
conceptArray, lengthOfConceptArray = setupStuff()
# conceptWithPubmedArticle = searchPubMedArticleByConcept(conceptArray)
searchThroughCodes(conceptArray, lengthOfConceptArray)
"""