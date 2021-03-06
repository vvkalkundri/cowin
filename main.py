import json ,os ,time
from datetime import date, datetime
from urllib.request import urlopen, Request

from cowin_api import CoWinAPI
from json2table import convert

if __name__ == '__main__':
    try:
        os.remove('index.html')
    except:
        pass
    cowin = CoWinAPI()
    # Code to get state ids
    # states = cowin.get_states()
    # print(states)
    state_ids = [16]
    district_ids = []
    for state_id in state_ids:
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
  <title>Covin Vaccine List</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  
</head><body>
<div class="container">
<h2>Last Updated on """ + dt_string + """</h2>
<h2>States covered are ::: Karnataka <h2>
<h2>Updated every few hours between ( 9AM -6PM )  <h2>
 <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search by pincode.." title="Type in the pincode ">
    """


    table_data  = ''
    counter = 1
    final_dict = dict()
    final_dict['session'] = []
    for district_id in district_ids:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        reg_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
            district_id, todays_date)
        req = Request(url=reg_url, headers=headers)
        data = json.loads(urlopen(req).read())
        for items in data['sessions']:
            final_dict['session'].append(items)
            counter +=1

    build_direction = "LEFT_TO_RIGHT"

    table_attributes = {"style": "width:100%", "align": "center", "style": "vertical-align:bottom",
                        "table border": "2", "th bgcolor": "FED8B1" ,"table id":"myTable"}
    html = html + convert(final_dict, build_direction=build_direction, table_attributes=table_attributes)
    html = html + """
    <script>
function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value;
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[6];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>
    
    
    
    </body></html>
    """
    f = open('index.html', 'a+')
    f.write(html)
    f.close()
