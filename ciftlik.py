from python_imagesearch.imagesearch import imagesearch,imagesearcharea
import pyautogui
import time
import keyboard
from PIL import Image

#legend online brov client içindir 1920 1080p'de çalışır!

xarti = 1310
yarti = 342
xarticollectall = 1155
yarticollectall = 680
xartipage = 1160
yartipage = 657
xartibarn = 500
yartibarn = 250

beklemesuresi = 0.50

tiklama = 0
kontrol = 0
# sol üst : 1236 663
# sol alt : 1236 680
# sağ üst : 1274 663
# sağ alt : 1274 680
# yazının yeri : 1254 673
# ilk sayfaya gitme : x=1174, y=668
# son sayfaya gitme : x=1325, y=670
# container sol üst : x=1310, y=336
# container sağ alt : x=1351, y=657
# collectall sol üst : x=1155, y=689
# collectall sağ alt : x=1354, y=795
# full sol üst : x=497, y=246
# full sağ alt : x=1376, y=819

while True:
    if keyboard.is_pressed("esc"):
        break

    energy = imagesearcharea("energy.png",1310,336,1351,657,precision=0.8)
    collect = imagesearcharea("collect.png",1310,336,1351,657,precision=0.8)
    grass = imagesearcharea("grass.png",1310,336,1351,657,precision=0.8)
    revive = imagesearcharea("revive.png",1310,336,1351,657,precision=0.8)
    wormhole = imagesearcharea("wormhole.png",1310,336,1351,657,precision=0.8)
    care = imagesearcharea("care.png",1310,336,1351,657,precision=0.8)
    pill = imagesearcharea("pill.png",1310,336,1351,657,precision=0.8)
    collectall = imagesearcharea("collectall.png",1155,680,1350,800,precision=0.8)
    nextpage = imagesearcharea("nextpage.png",1158,655,1353,685,precision=0.8)
    lastpage = imagesearcharea("lastpage.png",1158,655,1353,685,precision=0.8)
    firstpage = imagesearcharea("firstpage.png",1158,655,1353,685,precision=0.8)
    barn = imagesearcharea("barn.png",497,246,1376,819,precision=0.8)
    farm = imagesearcharea("farm.png",497,246,1376,819,precision=0.8)
    
    if collectall[0] != -1:
        #tümünü topla ekranda ise
        if energy[0] != -1:
            #energy bulunduysa
            pyautogui.click(energy[0]+xarti,energy[1]+yarti)  
            time.sleep(beklemesuresi)
            pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
            time.sleep(beklemesuresi)
        else:
            #energy bulunamadıysa
            if collect[0] != -1:
                #collect bulunduysa
                pyautogui.click(collect[0]+xarti,collect[1]+yarti)
                time.sleep(beklemesuresi)
                pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                time.sleep(beklemesuresi)
            else:
                #collect bulunamadıysa
                if grass[0] != -1:
                    #grass bulunduysa
                    pyautogui.click(grass[0]+xarti,grass[1]+yarti)
                    time.sleep(beklemesuresi)
                    pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                    time.sleep(beklemesuresi)
                else:
                    #grass bulunamadıysa
                    if revive[0] != -1:
                        #revive bulunduysa
                        pyautogui.click(revive[0]+xarti,revive[1]+yarti)
                        time.sleep(beklemesuresi)
                        pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                        time.sleep(beklemesuresi)
                    else:
                        #revive bulunamadıysa
                        if wormhole[0] != -1:
                            #wormhole bulunduysa
                            pyautogui.click(wormhole[0]+xarti,wormhole[1]+yarti)
                            time.sleep(beklemesuresi)
                            pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                            time.sleep(beklemesuresi)
                        else:
                            #wormhole bulunamadıysa
                            if care[0] != -1:
                                #care bulunduysa
                                pyautogui.click(care[0]+xarti,care[1]+yarti)
                                time.sleep(beklemesuresi)
                                pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                                time.sleep(beklemesuresi)
                            else:
                                #care bulunamadıysa
                                if pill[0] != -1:
                                    #pill bulunduysa
                                    pyautogui.click(pill[0]+xarti,pill[1]+yarti)
                                    time.sleep(beklemesuresi)
                                    pyautogui.click(collectall[0]+xarticollectall,collectall[1]+yarticollectall)
                                    time.sleep(beklemesuresi)
                                else:
                                    #hiçbirisi bulunamadıysa
                                    tiklama +=1
                                    if tiklama >=15:
                                        pyautogui.click(pyautogui.click(nextpage[0]+xartipage,nextpage[1]+yartipage))
                                    template = pyautogui.screenshot().crop((1158,655,1353,685))
                                    pixel = template.getpixel((lastpage[0],lastpage[1]))
                                    if pixel == (35,33,30):
                                        pyautogui.click(firstpage[0]+xartipage,firstpage[1]+yartipage)#first page e gidecek
                                        time.sleep(beklemesuresi)
                                        pyautogui.click(barn[0]+xartibarn,barn[1]+yartibarn)
                                        kontrol += 1
                                    else:
                                        if kontrol <= 1:
                                            pyautogui.click(nextpage[0]+xartipage,nextpage[1]+yartipage)
                                            tiklama = 0
                                            
                                        else:
                                            time.sleep(300)
                                            pyautogui.click(farm[0]+xartibarn,farm[1]+yartibarn)
                                            kontrol = 0
                                                
  
    else:
        print("bulunamadı")

    time.sleep(beklemesuresi)
        
