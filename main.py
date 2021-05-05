import json
import requests
from json2table import convert
from cowin_api import CoWinAPI
from datetime import date, datetime



if __name__ == '__main__':
    try:
        os.remove('index.html')
    except:
        pass
    cowin = CoWinAPI()
    state_id = 16
    district_ids = []
    districts = cowin.get_districts(state_id)
    for district_id in districts['districts']:
        district_ids.append(district_id['district_id'])

    today = date.today()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    todays_date = today.strftime("%d-%m-%Y")
    html = """
    <html>
    <head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  
</head><body>
<div class="container">
<h2>Last Updated on """ + dt_string + """</h2>
<h2>States covered are Karnataka <h2>
    """

    for district_id in district_ids:
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
                district_id, todays_date))
        data = json.loads(response.text)
        print(data)
        build_direction = "LEFT_TO_RIGHT"

        table_attributes = {"style": "width:100%", "align": "center", "style": "vertical-align:bottom",
                            "table border": "2", "th bgcolor": "FED8B1"}
        html = html + convert(data, build_direction=build_direction, table_attributes=table_attributes)
    html = html + """
    </body></html>
    """
    f = open('index.html', 'a+')
    f.write(html)
    f.close()
