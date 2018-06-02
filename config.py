timeInterval = 1 #Pick the time interval from trends24 e.g. ( 0 current hour, 1 past one hour and so on)
countryName = "united-states" #choose the country e.g. (united-kingdom, netherlands) or keep it empty for world wild
userName = "delgado_ahmed"
#searchQueries = ""

#List of commands
commandsList = {1 : 'echo \'This IP address (<IP-ADDRESS>) getting DOS for REAL!\' | telegram-send --stdin',
 				2 : 'ping -c 4 <IP-ADDRESS> | telegram-send --stdin',
                3 : 'nslookup <IP-ADDRESS> | telegram-send --stdin'}
