import requests
import time
import telebot

TOKEN = "5945472384:AAEO02kSROwEMIciIaix5rdvN9I0RCdE_Qw"

bot = telebot.TeleBot(TOKEN)

ids = [426213768]
#blacklist = ["Borsch8293", "Hillichu", "RuheSucherSS", "Cholm", "KoToBaCiK", "Wettisgod", "Bakamate", "Orest58008", "OlHiLel", "Korot228", "SaNchOusi", "BLAK_9029", "Folya1488", "Tarasha", "ZenikRep", "FrozenBlueFrog"]
whitelist = ["limeqz", "ratskui", "Quodie", "shkrummy", "OBAKKABO", "Meksich", "MAKSUMUS", "luxembourq", "paketpiva", "Borsch8293"]

print("Started!")

def check():
    rbot = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    if rbot.status_code != 200:
        print(rbot.content)
        return print('Помилка при виконанні запиту')

    t = rbot.json()["result"]#[len(rbot.json()["result"])-1]["message"]["chat"]["id"]
    for t1 in t:
        t2 = int(t1["message"]["chat"]["id"])
        for id in ids:
            if ids.count(t2) <= 0:
                ids.append(t2)
                #bot.send_message(t, f"You are in list now. {t}")
                print(ids)

    r = requests.get("http://borukva.space:3405/up/world/Borukva_nether/0")
    if r.status_code != 200:
        print(r.content)
        return print('Помилка при виконанні запиту')

    for p in r.json()["players"]:
        if p["world"] == "Borukva":
            if (p["x"] >= 7315.0) and (p["x"] <= 8180.0):
                if (p["z"] >= 7315.0) and (p["z"] <= 7515.0):
                    if whitelist.count(p["name"]) <= 0:
                        data = str(p["name"]) + ", " + str(p["x"]) + ", " + str(p["z"])
                        for id in ids:
                            bot.send_message(id, data)
                        print(data)
    #invisible = [p["name"] for p in r.json()["players"] if p["world"] == "-some-other-bogus-world-"]

    #print(f"Знайдено таких гравців з ефектом невидимості: {', '.join(invisible)}")
    
#print(requests.get("http://borukva.space:3405/up/world/Borukva_nether/0").json())
while True:
    check()
    time.sleep(10)