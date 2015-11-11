from pymetamap import MetaMap
import csv


def setupStuff():
    mm = MetaMap.get_instance('/Users/nwams/Documents/MetaMap/public_mm/bin/metamap12')

    # make input lowercase?
    searchTopic = raw_input('what topic are you searching for? ')
    searchTopic = [searchTopic]
    concepts, error = mm.extract_concepts(searchTopic, [1])

    conceptArray = []
    for concept in concepts:
        conceptArray.append(concept.preferred_name)
    print "conceptArray", conceptArray
    return conceptArray, len(conceptArray)

def getCPT():
    with open('../codes/CPT.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        codeDict = {rows[0]:rows[1] for rows in reader}
        print "Code Dictionary =", codeDict
        return codeDict

def searchCode(codeDict, searchTerms, lengthOfArray):
    searchTerms[2] = 'Kidney' # delete later
    watevs = []

    """ find a way to append all key, value pair mappings
    consider storing in dict, not tuples
    """
    for i in range(lengthOfArray):
        watevs = [(k, v) for (k, v) in codeDict.iteritems() if searchTerms[i] in v]
    print watevs

codeDict = getCPT()

conceptArray, length = setupStuff()

searchCode(codeDict, conceptArray, length)