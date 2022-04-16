from bs4 import BeautifulSoup as soupParser
from urllib.request import Request, urlopen

# Function to get the page content
def get_page_content(url, head):
  """
  Function to get the page content
  """
  try:
    return urlopen(Request(url, headers=head))
  except:
    print("Error: Could not get the page content")
    return None

url = 'https://www.idealista.com/en/venta-viviendas/barcelona-barcelona/'
head = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': 'https://www.idealista.com/en/venta-viviendas/barcelona-barcelona/',
  'cookie': """atuserid={"name":"atuserid","val":"47abb3f1-4221-4d97-8507-87a8ee691cdb","options":{"end":"2023-04-03T15:11:32.276Z","path":"/"}}; atidvisitor={"name":"atidvisitor","val":{"vrn":"-582065-"},"options":{"path":"/","session":15724800,"end":15724800}}; didomi_token=eyJ1c2VyX2lkIjoiMTdmNGIyZmEtZjE0ZC02ZGVkLWEyOWQtYTM5YmUyYjQ1NTY4IiwiY3JlYXRlZCI6IjIwMjItMDMtMDJUMTU6MTE6MzMuMTMzWiIsInVwZGF0ZWQiOiIyMDIyLTAzLTAyVDE1OjExOjMzLjEzM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzptaXhwYW5lbCIsImM6YWJ0YXN0eS1MTGtFQ0NqOCIsImM6aG90amFyIiwiYzp5YW5kZXhtZXRyaWNzIiwiYzpiZWFtZXItSDd0cjdIaXgiLCJjOmFwcHNmbHllci1HVVZQTHBZWSIsImM6dGVhbGl1bWNvLURWRENkOFpQIiwiYzppZGVhbGlzdGEtTHp0QmVxRTMiLCJjOmlkZWFsaXN0YS1mZVJFamUyYyJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJhbmFseXRpY3MtSHBCSnJySzciLCJnZW9sb2NhdGlvbl9kYXRhIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFGbUFDQUZrLkFBQUEifQ==; euconsent-v2=CPVMwMAPVMwMAAHABBENCECoAP_AAAAAAAAAF5wBAAIAAtAC2AvMAAABAaADAAEESyUAGAAIIllIAMAAQRLIQAYAAgiWOgAwABBEsJABgACCJYyADAAEESxUAGAAIIlg.f_gAAAAAAAAA; _gcl_au=1.1.216176736.1646233894; _fbp=fb.1.1646233896944.398331645; userUUID=c3d8eb55-4e38-420b-ab5a-7211c9c9ff74; send2f99f802-4fcf-4978-b470-36547ff55f58="{'friendsEmail':null,'email':null,'message':null}"; contact5cb34b49-9b2a-437f-b8bd-cadcf36ecc02="{'email':null,'phone':null,'phonePrefix':null,'friendEmails':null,'name':null,'message':null,'message2Friends':null,'maxNumberContactsAllow':10,'defaultMessage':true}"; SESSION=b736c720ecc0095b~5cb34b49-9b2a-437f-b8bd-cadcf36ecc02; listingGalleryBoostEnabled=false; cookieSearch-1="/venta-viviendas/barcelona-barcelona/:1648890207852"; utag_main=v_id:017f4b2fadb3004d982ab381bfa805079001a07100bd0$_sn:4$_se:4$_ss:0$_st:1648892009607$dc_visit:4$ses_id:1648889680258;exp-session$_pn:4;exp-session$_prevVtSource:directTraffic;exp-1648893281671$_prevVtCampaignCode:;exp-1648893281671$_prevVtDomainReferrer:idealista.com;exp-1648893281671$_prevVtSubdomaninReferrer:www.idealista.com;exp-1648893281671$_prevVtUrlReferrer:https://www.idealista.com/en/venta-viviendas/barcelona-barcelona/;exp-1648893281671$_prevVtCampaignLinkName:;exp-1648893281671$_prevVtCampaignName:;exp-1648893281671$_prevVtRecommendationId:;exp-1648893281671$_prevCompletePageName:11::listing::resultList::others;exp-1648893810388$_prevLevel2:11;exp-1648893810388$dc_event:4;exp-session$dc_region:ap-east-1;exp-session; ABTasty=uid=99az7qxsgtaq8k2h&fst=1646233893912&pst=1648878476963&cst=1648889681916&ns=4&pvt=47&pvis=4&th=; datadome=.5SgCu6ufWS2s3cfGGsbL-~dwwcPh1N9mF~dvoqAZe~dxGRe5d8KQpQkUuwGva_i.e.m7L0vVV2RP8Bt9YLxw5O6Q.It5Ci8AhF.S_e36he-FPaM5Yk8n7IOGh3XywK6; ABTastySession=mrasn=&sen=3&lp=https%3A%2F%2Fwww.idealista.com%2Fen%2Fventa-viviendas%2Fbarcelona-barcelona%2F"""
}

data = get_page_content(url, head).read()
print(data)
# https://docs.google.com/spreadsheets/d/14Of9p4euyWsiHhZQercKEdSW7I0-UmH-QtXlJ6yIX48/edit#gid=0

