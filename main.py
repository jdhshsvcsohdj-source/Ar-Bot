import requests,time,os
TOKEN=os.getenv("TOKEN")
URL=f"https://api.telegram.org/bot{TOKEN}/"
s=requests.Session()
off=0
while True:
 try:
  r=s.get(URL+"getUpdates",params={"offset":off,"timeout":10},timeout=15).json()
  for u in r.get("result",[]):
   off=u["update_id"]+1
   if "message" in u:
    cid=u["message"]["chat"]["id"]
    if "/start" in u["message"].get("text",""):
     s.get(URL+"sendMessage",params={"chat_id":cid,"text":"البوت شغال @p_x_i_y"})
 except:time.sleep(1)
