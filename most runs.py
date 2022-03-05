from bs4 import BeautifulSoup
import openpyxl
import requests

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Most runs'
headers = ['Player', 'Matches', 'Innings', 'Not Out', 'Runs', 'High Score', 'Average', 'Balls Faced', 'Strike Rate', 'Hundreds', 'Fiftys', 'Ducks', 'Fours', 'Sixes','Team']
sheet.append(headers)

source = requests.get('https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=13840;type=tournament')
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
table = soup.find_all('table',class_="engineTable")[0]
head = table.find('tbody')
for plyr in head.find_all("tr",class_="data2"):
        Player = plyr.find_all("td")[0].text
        Mat = plyr.find_all("td")[1].text
        Inns = plyr.find_all("td")[2].text
        NO = plyr.find_all("td")[3].text
        Runs = plyr.find_all("td")[4].text
        HS = plyr.find_all("td")[5].text.strip("*")
        Ave = plyr.find_all("td")[6].text
        BF = plyr.find_all("td")[7].text
        SR = plyr.find_all("td")[8].text
        Hundreds = plyr.find_all("td")[9].text
        Fiftys = plyr.find_all("td")[10].text
        Ducks = plyr.find_all("td")[11].text
        Fours = plyr.find_all("td")[12].text
        Sixes = plyr.find_all("td")[13].text
        stats = [Player,Mat,Inns,NO,Runs,HS,Ave,BF,SR,Hundreds,Fiftys,Ducks,Fours,Sixes]
        print(stats)
        sheet.append(stats)
for team in head.find_all("tr",class_="note"):
        t = team.find("td").text.strip("()")
        tm = [t]
        print(tm)
        sheet.append(tm)

excel.save('IPL 2021 analysis.xlsx')

