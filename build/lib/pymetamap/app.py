from pymetamap import MetaMap
import csv

def getCPTandICD():
    """
    get CPT and ICD codes, put in dictionary
    :return: the dictionary of codes
    """
    with open('../codes/CPTandICD.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {rows[0]:rows[1] for rows in reader}
        return codeDict

def setupStuff():
    """
    setup MetaMap and search UMLS for user desired topic
    :return: The preferred name for the UMLS concept identified in the text. And the number of different preferred names output
    """
    mm = MetaMap.get_instance('/Users/yiqingluo/IF5400/public_mm/bin/metamap12')

    searchTopic = raw_input('What topic are you searching for? ')
    print "the user is searching for:", searchTopic
    searchTopic = [searchTopic]

    # [1] only allow user to search for one topic at a time
    concepts, error = mm.extract_concepts(searchTopic, [1])

    conceptArray = []
    for concept in concepts:
        conceptArray.append(concept.preferred_name)
    print "UMLS terms = ", conceptArray

    return conceptArray, len(conceptArray)


def searchThroughCodes(codeDict, searchTerms, numOfSearches):
    """
    search through the list of IPT/CPT codes.
    if the users topic matches, via UMLS terms, assign it to a dictionary
    :param codeDict: dictionary of all IPT/CPT codes
    :param searchTerms: array of UMLS Concept preferred_names
    :param numOfSearches: number of names in Concept the array
    :return: matchingTopicsDict
    """
    matchingTopicsDict ={}
    for i in range(numOfSearches):
        for k,v in codeDict.iteritems():
            if searchTerms[i].lower() in v.lower(): # case insensitive search required
                matchingTopicsDict[k] = v
    print matchingTopicsDict
    return matchingTopicsDict

codeDict = getCPTandICD()

conceptArray, lengthOfConceptArray = setupStuff()

searchThroughCodes(codeDict, conceptArray, lengthOfConceptArray)