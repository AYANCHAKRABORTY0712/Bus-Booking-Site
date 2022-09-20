#my own functions

import random
import string
from time import gmtime, strftime, localtime
from datetime import time, date, datetime, timedelta
from booking.models import USER,BUS

start=datetime(year=2020,month=1,day=1,hour=6,minute=00,second=00)
agencies=['Nanda Travels','SBSTC','Singh Travels','Chakraborty Tourism','Pal Travels Agency','Bengal Tourism','Rainbow Travels','Day & Night Tour & Travels']
bustypes=['AC Type','Non AC Type']
stations=[
    'Shyambazar',
    'Bakkhali',
    'Mandarmani',
    'Bandel',
    'Murshidabad',
    'Howrah',
    'Purulia',
    'Asansol',
    'Siliguri',
    'Kharagpur'
]
routes={
     'Shyambazar-Bakkhali': ['96S/U', '97Q/Y', '74O/Q'], 
     'Shyambazar-Mandarmani': ['57W/Z'], 
     'Shyambazar-Bandel': ['64V/I', '24H/L', '80T/C'], 
     'Shyambazar-Murshidabad': ['56N/K', '83R/B', '78F/S'], 
     'Shyambazar-Howrah': ['31C/R', '74E/V', '85Z/L'], 
     'Shyambazar-Purulia': ['82Z/X', '93D/G'], 
     'Shyambazar-Asansol': ['24G/D', '15O/P'], 
     'Shyambazar-Siliguri': ['22Y/Z', '45F/M', '21O/I'], 
     'Shyambazar-Kharagpur': ['97V/Z', '85H/X'], 
     'Bakkhali-Shyambazar': ['98L/Z'], 
     'Bakkhali-Mandarmani': ['74R/U'], 
     'Bakkhali-Bandel': ['14V/R', '50O/J', '39R/J'], 
     'Bakkhali-Murshidabad': ['86J/J', '9N/P'], 
     'Bakkhali-Howrah': ['90D/D'], 
     'Bakkhali-Purulia': ['26F/F', '20T/Y', '89Z/A'], 
     'Bakkhali-Asansol': ['25F/U', '43T/C'], 
     'Bakkhali-Siliguri': ['35V/R'], 
     'Bakkhali-Kharagpur': ['52U/E', '48G/A'], 
     'Mandarmani-Shyambazar': ['94Y/P'], 
     'Mandarmani-Bakkhali': ['1R/Z', '49F/O'], 
     'Mandarmani-Bandel': ['55U/N'], 
     'Mandarmani-Murshidabad': ['40H/X', '66B/Q'], 
     'Mandarmani-Howrah': ['8J/T', '71U/J'], 
     'Mandarmani-Purulia': ['42M/A', '59P/C'], 
     'Mandarmani-Asansol': ['82P/V', '86A/V', '53P/N'], 
     'Mandarmani-Siliguri': ['69V/I'], 
     'Mandarmani-Kharagpur': ['3Q/D', '92G/S', '14Y/A'], 
     'Bandel-Shyambazar': ['74E/D', '13G/E'], 
     'Bandel-Bakkhali': ['89X/S'], 
     'Bandel-Mandarmani': ['82H/K', '22O/V'], 
     'Bandel-Murshidabad': ['9J/P'], 
     'Bandel-Howrah': ['29G/Q'], 
     'Bandel-Purulia': ['38G/B'], 
     'Bandel-Asansol': ['7X/X', '84M/I'], 
     'Bandel-Siliguri': ['4I/D', '45Q/G'], 
     'Bandel-Kharagpur': ['13E/D'], 
     'Murshidabad-Shyambazar': ['20O/P'], 
     'Murshidabad-Bakkhali': ['34R/U'], 
     'Murshidabad-Mandarmani': ['94V/E', '24N/H', '89U/C'], 
     'Murshidabad-Bandel': ['67M/S'], 
     'Murshidabad-Howrah': ['63W/Q'], 
     'Murshidabad-Purulia': ['17Q/U', '88L/G', '8M/S'], 
     'Murshidabad-Asansol': ['85Q/W', '55Z/Q', '12O/W'], 
     'Murshidabad-Siliguri': ['29B/N', '99T/N', '64Y/B'], 
     'Murshidabad-Kharagpur': ['90U/E', '92M/V'], 
     'Howrah-Shyambazar': ['89V/E'], 
     'Howrah-Bakkhali': ['22R/G', '48B/R'], 
     'Howrah-Mandarmani': ['99R/I', '68F/R'], 
     'Howrah-Bandel': ['12A/H'], 
     'Howrah-Murshidabad': ['60W/N'], 
     'Howrah-Purulia': ['17B/H'], 
     'Howrah-Asansol': ['71E/Z', '86Z/U', '14S/A'], 
     'Howrah-Siliguri': ['19J/O', '65N/I'], 
     'Howrah-Kharagpur': ['55X/L'], 
     'Purulia-Shyambazar': ['21V/U'], 
     'Purulia-Bakkhali': ['87V/V', '22Y/A'], 
     'Purulia-Mandarmani': ['71R/W'], 
     'Purulia-Bandel': ['67Z/E'], 
     'Purulia-Murshidabad': ['72L/M'], 
     'Purulia-Howrah': ['3P/H', '88K/A'], 
     'Purulia-Asansol': ['72T/H', '96M/E'], 
     'Purulia-Siliguri': ['84G/M', '59F/S', '12D/C'], 
     'Purulia-Kharagpur': ['6I/L', '86H/E', '90J/D'], 
     'Asansol-Shyambazar': ['7J/A'], 
     'Asansol-Bakkhali': ['12D/D', '61N/U', '49Z/I'], 
     'Asansol-Mandarmani': ['98N/B', '5B/C'], 
     'Asansol-Bandel': ['80O/C', '44U/L', '62C/K'], 
     'Asansol-Murshidabad': ['20C/W', '79T/X', '98S/O'], 
     'Asansol-Howrah': ['93P/N'], 
     'Asansol-Purulia': ['99P/P'], 
     'Asansol-Siliguri': ['11P/Z', '73T/H', '92U/W'], 
     'Asansol-Kharagpur': ['2E/O', '76X/Z', '60S/Q'], 
     'Siliguri-Shyambazar': ['95Z/Z', '61F/H'], 
     'Siliguri-Bakkhali': ['38Y/Z', '59P/Q'], 
     'Siliguri-Mandarmani': ['61P/D', '52V/A', '86I/L'], 
     'Siliguri-Bandel': ['8C/P', '91G/I', '31O/Z'], 
     'Siliguri-Murshidabad': ['73M/B', '85R/C'], 
     'Siliguri-Howrah': ['23S/A'], 
     'Siliguri-Purulia': ['5E/X', '81O/V', '64A/L'], 
     'Siliguri-Asansol': ['7V/M', '94A/L', '8D/Q'], 
     'Siliguri-Kharagpur': ['9L/T', '72Q/N', '84V/P'], 
     'Kharagpur-Shyambazar': ['2D/H'], 
     'Kharagpur-Bakkhali': ['78W/P', '30C/H'], 
     'Kharagpur-Mandarmani': ['22R/J', '95L/Y'], 
     'Kharagpur-Bandel': ['37Z/F', '38F/B', '63B/E'], 
     'Kharagpur-Murshidabad': ['87R/U', '37N/Q'], 
     'Kharagpur-Howrah': ['57G/N', '57H/O', '7W/R'], 
     'Kharagpur-Purulia': ['53M/A'], 
     'Kharagpur-Asansol': ['27T/Z', '93W/G', '37J/W'], 
     'Kharagpur-Siliguri': ['18A/Q', '27F/N']
}
Point={
    'Shyambazar': ['Shyambazar 5 Point','Manindra College','Hatibagan'],
    'Bakkhali': ['Bakkhali Bus Stand'],
    'Mandarmani': ['Mandarmani Bus Stand','Mandarmani Chowlkhola Bus Stand','Chaulkhola'],
    'Bandel': ['Bandel Mini Bus Terminal','Rajhat More Bus Stop'],
    'Murshidabad': ['Berhampore Bus Stand','Lalbagh Bus Stand','Jiaganj Bus Station'],
    'Howrah': ['Howrah Bus Stand','54 Bus Stand','Shibpur Tram Depo Bus Stand'],
    'Purulia':['Purulia Bus Stand'],
    'Asansol': ['Asansol Station Bus Terminus','Burnpur Bus Stand'],
    'Siliguri': ['Tenzing Norgay Central Bus Terminus','Sikkim National Transport (SNT) Bus Terminus'],
    'Kharagpur': ['Kharagpur Bus Station','Jhapetapur Bus Stand','Prembazar Bus Stop']
}
Position={
    'Shyambazar':1,
    'Bakkhali':0,
    'Mandarmani':3,
    'Bandel':5,
    'Murshidabad':11,
    'Howrah':2,
    'Purulia':7,
    'Asansol':6,
    'Siliguri':16,
    'Kharagpur':5
}
def CreateBus(From,To,Date):
    global start
    agency=random.choice(agencies)
    bustype=random.choice(bustypes)
    id1=random.randint(1,99)
    id2=random.choice(string.ascii_uppercase)
    id3=random.randint(1000,9999)
    bus_ID='WB-'+str(id1)+id2+' '+str(id3)
    route=random.choice(routes[From+'-'+To])
    BoardPoint=random.choice(Point[From])
    DropPoint=random.choice(Point[To])
    AvS=45
    seats={
        "seniors":4,
        "ladies":4,
        "PwD":2,
        "transgender":1,
        "general":34
    }
    seatno=['S'+str(i) for i in range(1,46)]
    BkS=0
    hours=random.randint(0,16)
    minutes=random.choice([0,15,30,45])
    BTime=start+timedelta(hours=hours,minutes=minutes)
    Dist=abs(Position[From]-Position[To])
    TravelTime=Dist*0.8
    DTime=BTime+timedelta(hours=int(TravelTime),minutes=int((TravelTime-int(TravelTime))*60))
    BTime=BTime.strftime("%H:%M:%S")
    DTime=DTime.strftime("%H:%M:%S")
    TravelTime=str(int(TravelTime))+'h'+' '+str(int((TravelTime-int(TravelTime))*60))+'m'
    Rate=abs(Position[From]-Position[To])*40
    bus=BUS(agency=agency,bustype=bustype,bus_ID=bus_ID,route=route,From=From,To=To,BoardPoint=BoardPoint,DropPoint=DropPoint,AvS=AvS,BkS=BkS,BTime=BTime,DTime=DTime,TravelTime=TravelTime, Date=Date,Rate=Rate)
    bus.save()
    