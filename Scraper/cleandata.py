from nltk.tokenize import word_tokenize
import json



dest = "C:\\Users\\Dennis.Pieruschka\\Documents\\Arrays\\Scraper\\Links\\--www.visservanbaars.nl-vacatures-cloud-solution-architect-.txt"
file = open(dest, 'r')
text = file.read()

newtext = text
thesaurus = ["communicatie","BI Architect",".net","access","analist","analyst","architect","azure","banking","bedrijfsproces","bi","bi developer","big data","business analist","business analyst","business intelligence","business objects","c#","cognos","cosmos","crm","crystal","data analist","data analyst","data model","data modeling","data modeller","data science","data scientist","data warehouse","datavault","dax","dba","Debian","designer","developer","dqs","dwh","etl","etl testing","excel","financiële dienstverlening","functionele analyse","Google analytics","Hadoop","Hdfs","Hive","HP-UX","Hue","informatie analist","informatie analyse","insurance","java","javascript","jira","kanban","linux","machine learning","Machine learning","marklogic","matlab","mds","modelleren","mysql","Node.js","nosql","ontwikkelaar","Oozie","oracle","overheid","Pentaho","php","pl/sql","powerbi","powercenter","powerdesigner","ProcSQL","project manager","python","qliksense","qlikview","r","RedHat","requirements analysis","sap","sas","sas va","scrum","semantics","specialist","spl","spotfire","spss","sql","sql developer","ssas","ssis","ssrs","tableau","Talend","technische analyse","telecom","teradata","Ubuntu","uml","vba","verzekeringen","visual analytics","visualisatie","watson","xpath","xquery"]
Skills = []
words = word_tokenize(newtext)


for j in words:
    if j in thesaurus:
        Skills.append(j)


print(Skills)

def writeToJSON(path, fileName, data):
    filePath = path + fileName + '.json'
    with open(filePath, 'w') as fp:
        json.dump(data, fp)

fileName = '--www.visservanbaars.nl-vacatures-cloud-solution-architect-'

path = "C:\\Users\\Dennis.Pieruschka\\Documents\\Scraper\\Links\\"
data = {}
data['skills'] = Skills


writeToJSON(path, fileName, data)

