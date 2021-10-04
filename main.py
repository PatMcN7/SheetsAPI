import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)
scatteredSheet = client.open('scattered logistics')
worksheetZero = scatteredSheet.get_worksheet(0)
worksheetThree = scatteredSheet.get_worksheet(3)
bruh = client.open('BRUHHHHHHHHHHHHHHHHHHHH').sheet1


theempireofnewsuslandSheet = client.open('theempireofnewsusland').sheet1
rhomaiontawantinsuyuSheet = client.open('Rhomaiontawantinsuyu').sheet1
egyptSheet = client.open('Egypt').sheet1
canadalandSheet = client.open('CanadaLand').sheet1
fanslarviaSheet = client.open('Fanslarvia').sheet1
yartheczarSheet = client.open('yaRtheczar').sheet1
fivestarSheet = client.open('FiveStar').sheet1
andrewdumoSheet = client.open('Andrewdumo').sheet1
mrsfrizzleSheet = client.open('MrsFrizzle').sheet1
thenotoriusjigglybuttgangSheet = client.open('Thenotoriusjgglybuttgang').sheet1
brazilSheet = client.open('Brazil').sheet1
bigboisSheet = client.open('Bigbois').sheet1
pwndaSheet = client.open('Pwnda').sheet1

def readWrite():
    theempireofnewsuslandTroops = worksheetZero.get('J2:K2')
    RhomaiontawantinsuyuTroops= worksheetZero.get('J3:K4')
    EgyptTroops = worksheetZero.get('J4:K4')
    CanadaLandTroops = worksheetZero.get('J5:K5')
    FanslarviaTroops= worksheetZero.get('J6:K6')
    yaRtheczarTroops = worksheetZero.get('J7:K7')
    FiveStarTroops = worksheetZero.get('J8:K8')
    AndrewdumoTroops = worksheetZero.get('J9:K9')
    MrsFrizzleTroops = worksheetZero.get('J10:K10')
    ThenotoriusJigglybuttgangTroops = worksheetZero.get('J11:K11')
    BrazilTroops = worksheetZero.get('J12:K12')
    BigboisTroops = worksheetZero.get('J13:K13')
    PwndaTroops = worksheetZero.get('J14:K14')
    #print(theempireofnewsuslandTroops, RhomaiontawantinsuyuTroops, EgyptTroops, CanadaLandTroops, FanslarviaTroops, yaRtheczarTroops, FiveStarTroops, AndrewdumoTroops, MrsFrizzleTroops, ThenotoriusJigglybuttgangTroops, BrazilTroops, BigboisTroops, PwndaTroops)
    theempireofnewsuslandSheet.update('A1', theempireofnewsuslandTroops)
    rhomaiontawantinsuyuSheet.update('A1', RhomaiontawantinsuyuTroops)
    egyptSheet.update('A1', EgyptTroops)
    canadalandSheet.update('A1', CanadaLandTroops)
    fanslarviaSheet.update('A1', FanslarviaTroops)
    yartheczarSheet.update('A1', yaRtheczarTroops)
    fivestarSheet.update('A1', FiveStarTroops)
    andrewdumoSheet.update('A1', AndrewdumoTroops)
    mrsfrizzleSheet.update('A1', MrsFrizzleTroops)
    thenotoriusjigglybuttgangSheet.update('A1', ThenotoriusJigglybuttgangTroops)
    brazilSheet.update('A1', BrazilTroops)
    bigboisSheet.update('A1', BigboisTroops)
    pwndaSheet.update('A1', PwndaTroops)
    print('Troop and Knowledge Call Complete')



def Bruh():
  bruhRecords = worksheetThree.get_all_values()
  bruh.update('A1', bruhRecords)
  print('Bruh Call complete')

Bruh()
while True:
    readWrite()
    Bruh()
