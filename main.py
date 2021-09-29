import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

scatterdSheet = client.open('scattered logistics').sheet1


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
'''
def bruh():
    bruhData = bruhSheet.get_all_records()
    print(bruhData)
bruh()
'''
def readWrite():
    theempireofnewsuslandTroops = scatterdSheet.cell(2, 6).value
    RhomaiontawantinsuyuTroops= scatterdSheet.cell(3, 6).value
    EgyptTroops = scatterdSheet.cell(4, 6).value
    CanadaLandTroops = scatterdSheet.cell(5, 6).value
    FanslarviaTroops= scatterdSheet.cell(6, 6).value
    yaRtheczarTroops = scatterdSheet.cell(7, 6).value
    FiveStarTroops = scatterdSheet.cell(8, 6).value
    AndrewdumoTroops = scatterdSheet.cell(9, 6).value
    MrsFrizzleTroops = scatterdSheet.cell(10, 6).value
    ThenotoriusJigglybuttgangTroops = scatterdSheet.cell(11, 6).value
    BrazilTroops = scatterdSheet.cell(12, 6).value
    BigboisTroops = scatterdSheet.cell(13, 6).value
    PwndaTroops = scatterdSheet.cell(14, 6).value
    print(theempireofnewsuslandTroops, RhomaiontawantinsuyuTroops, EgyptTroops, CanadaLandTroops, FanslarviaTroops, yaRtheczarTroops, FiveStarTroops, AndrewdumoTroops, MrsFrizzleTroops, ThenotoriusJigglybuttgangTroops, BrazilTroops, BigboisTroops, PwndaTroops)
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
    print('done')


readWrite()
while True:
    readWrite()
    print('called')
    time.sleep(7200)

