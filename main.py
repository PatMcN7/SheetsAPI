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
    theempireofnewsuslandTroops = worksheetZero.cell(2, 6).value
    RhomaiontawantinsuyuTroops= worksheetZero.cell(3, 6).value
    EgyptTroops = worksheetZero.cell(4, 6).value
    CanadaLandTroops = worksheetZero.cell(5, 6).value
    FanslarviaTroops= worksheetZero.cell(6, 6).value
    yaRtheczarTroops = worksheetZero.cell(7, 6).value
    FiveStarTroops = worksheetZero.cell(8, 6).value
    AndrewdumoTroops = worksheetZero.cell(9, 6).value
    MrsFrizzleTroops = worksheetZero.cell(10, 6).value
    ThenotoriusJigglybuttgangTroops = worksheetZero.cell(11, 6).value
    BrazilTroops = worksheetZero.cell(12, 6).value
    BigboisTroops = worksheetZero.cell(13, 6).value
    PwndaTroops = worksheetZero.cell(14, 6).value
    #print(theempireofnewsuslandTroops, RhomaiontawantinsuyuTroops, EgyptTroops, CanadaLandTroops, FanslarviaTroops, yaRtheczarTroops, FiveStarTroops, AndrewdumoTroops, MrsFrizzleTroops, ThenotoriusJigglybuttgangTroops, BrazilTroops, BigboisTroops, PwndaTroops)
    theempireofnewsuslandSheet.update_cell(1,1, theempireofnewsuslandTroops)
    rhomaiontawantinsuyuSheet.update_cell(1,1, RhomaiontawantinsuyuTroops)
    egyptSheet.update_cell(1,1, EgyptTroops)
    canadalandSheet.update_cell(1,1, CanadaLandTroops)
    fanslarviaSheet.update_cell(1,1, FanslarviaTroops)
    yartheczarSheet.update_cell(1,1, yaRtheczarTroops)
    fivestarSheet.update_cell(1,1, FiveStarTroops)
    andrewdumoSheet.update_cell(1,1, AndrewdumoTroops)
    mrsfrizzleSheet.update_cell(1,1, MrsFrizzleTroops)
    thenotoriusjigglybuttgangSheet.update_cell(1,1, ThenotoriusJigglybuttgangTroops)
    brazilSheet.update_cell(1,1, BrazilTroops)
    bigboisSheet.update_cell(1,1, BigboisTroops)
    pwndaSheet.update_cell(1,1, PwndaTroops)
    print('Troop Knowledge Call Complete')


readWrite()

def Bruh():
  testRecords = worksheetThree.get_all_values()
  bruh.update('A1', testRecords)
  print('Bruh Call omplete')

Bruh()
while True:
    readWrite()
    bruh()
    time.sleep(15)
