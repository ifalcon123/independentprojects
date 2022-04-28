import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account




SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)




SAMPLE_SPREADSHEET_ID = '1IVfVfHE68MtkjUvZtGI5LXpLCLsorKsQYeB_ibL1kNU'




data_range = "Sheet1!A1:Q272"


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=data_range).execute()


values = result.get('values', [])

df = pd.DataFrame(values[1:], columns = values[0])

df = df.astype({"Sq Ft":"int","Proximity (blocks)":"int", 
                "Light":"int", "View":"int", "Score":"float", 
                "Ranking":"int"})


dorms = ["Watt", "Harmony", "Broadway", "Carlton", "600 West 113", 
          "Schapiro", "Wien", "Ruggles"]

dorm_totals = [0,0,0,0,0,0,0,0]
size_totals = [0,0,0,0,0,0,0,0]
size_averages = []



for i in range(df.shape[0]):
    if df.loc[i,"Type"] == "Single" and df.loc[i,"Taken"] == "No":
        dorm_totals[dorms.index(df.loc[i,"Building"])] += 1
        size = df.loc[i,"Sq Ft"]
        size_totals[dorms.index(df.loc[i,"Building"])] += size
    elif (df.loc[i,"Type"] in ["Double", "Studio Double", "Double (male)"]) and df.loc[i,"Taken"] == "No":
        dorm_totals[dorms.index(df.loc[i,"Building"])] += 2
        size = df.loc[i,"Sq Ft"]
        size_totals[dorms.index(df.loc[i,"Building"])] += size*2






    
# for i in range(len(dorm_totals)):
#     size_averages += [size_totals[i] / dorm_totals[i]]


# with open("nuss.txt", "r") as nuss:
#     for line in nuss:
#         line = line.split("\t")
#         if line[5] != "" and line[5] != "UNI":
#             for i in range(df.shape[0]):
#                 if df.loc[i, "Room Code"] == line[3]:
#                     df.at[i, "Taken"] = "Yes"

def update(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.split("\t")
            if line[5] != "" and line[5] != "UNI":
                for i in range(df.shape[0]):
                    if df.loc[i, "Room Code"] == line[3]:
                        df.at[i, "Taken"] = "Yes"


test = df.copy(deep=True)

with open("mcbain.txt", "r") as file:
    for line in file:
        line = line.split("\t")
        if line[5] == "":
            df2 = pd.DataFrame({'Ranking': [0],
                    'Score' : [0],
                    'Taken' : ['No'],
                    'Room Code' : [line[2]],
                    'Building': ["McBain"],
                    'Room Number': [line[2][4:]],
                    'Starred': [''],
                    'Type': ["Double"],
                    'Sq Ft': [''],
                    'Proximity (blocks)': [1],
                    'Light': [''],
                    'View': [''],
                    'Bathroom': ['Corridor'],
                    'Kitchen': ['Floor'],
                    'Lounge': ['Floor'],
                    'Dorm Availability': [0],
                    'Notes': ['']})
            test = test.append(df2, ignore_index = True)
                



update("nuss.txt")
update("broadway.txt")
update("carlton.txt")
update("schapiro.txt")
update("wien.txt")
update("harmony.txt")



#duplicates
templist = []
for i in range(df.shape[0]):
    code = df.loc[i, "Room Code"]
    if code not in templist:
        templist += code
    else:
        print(code)




    
    
# ALGORITHM for ranking options:

for i in range(df.shape[0]):
    score = 0
    
    #Number of rooms available in building
    #score is total number of spots available divided by 10
    #with a max score of 10
    
    dorm_index = dorms.index(df.loc[i,"Building"])
    df.at[i, "Dorm Availability"] = dorm_totals[dorm_index]
    
    if df.loc[i,"Dorm Availability"] > 100:
        score += 10
    else:
        score += df.loc[i,"Dorm Availability"] / 10
    
    
    
    #Square footage:
        
    #score is square footage divided by 12 minus 15 for doubles
    #multiply this by 2 for singles
    if df.loc[i,"Type"] == "Single":
        score += df.loc[i,"Sq Ft"] / 6 - 15
    else:
        score += df.loc[i,"Sq Ft"] / 12 - 15
    
    
    #Proximity:
        
    #score is 10 minus number of blocks away
    score += (10 - df.loc[i, "Proximity (blocks)"])
    
    
    #Kitchen:
    # private = +3, suite = +2, floor = +1
    
    if df.loc[i,"Kitchen"] == "Private":
        score += 3
    elif df.loc[i,"Kitchen"] == "Suite":
        score += 2
    
    #Personal space:
    
    # single = +20, studio double = +15
    
    if df.loc[i,"Type"] == "Single":
        score += 20
    elif df.loc[i,"Type"] == "Studio Double":
        score += 15
    
    #Light/view:
    
    # weighted average out of 10 with light being 75%
    
    score += 0.75*(df.loc[i,"Light"]) + 0.25*(df.loc[i,"View"])
    
    #Bathroom:
    
    #private = +5, suite = +4
    
    if df.loc[i,"Bathroom"] == "Private":
        score += 5
    elif df.loc[i,"Bathroom"] == "Suite":
        score += 4
    
    
    #Starred:
        
    #+5 for starred rooms
    
    if df.loc[i, "Starred"] == "*":
        score += 5
    
    #Lounge:
    
    #suite = +3, floor = +1
    
    if df.loc[i, "Lounge"] == "Suite":
        score += 3
    elif df.loc[i, "Lounge"] == "Floor":
        score += 1
    
    
    
    if df.loc[i,"Taken"] == "No":
        df.at[i, "Score"] = score
    else:
        df.at[i, "Score"] = 0


df.sort_values("Score")

score_values = []
for i in df["Score"]:
    score_values += [i]

score_values.sort(reverse=True)


for i in range(len(score_values)):
    df.at[i, "Ranking"] = score_values.index(df.loc[i,"Score"]) + 1
    
    
# df.to_csv('housinginfo.csv', index=False)





df = df.sort_values(by="Score", ascending = False)

data_list = df.values.tolist()



output_range = "Sheet1!A2"
    
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                                 range=output_range, 
                                                 valueInputOption="USER_ENTERED", 
                                                 body={"values":data_list})
request.execute()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





