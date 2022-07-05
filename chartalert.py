//STRATEGY TESTER▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Alerts
ttlongentrystring  = "{\n\"side\":\"longentry\"}"
ttshortentrystring = "{\n\"side\":\"shortentry\"}"
ttlongexitstring = "{\n\"side\":\"longexit\"}"
ttshortexitstring = "{\n\"side\":\"shortexit\"}"
//ttstopstring = "{\n\"side\":\"stop\"}"

uselongentryalert = input(defval=true, title="Use LONG ENTRY Alert", group="Alert Messages")
longentrystring  = input(title="Buy Alert Message",  defval=ttlongentrystring,  type=input.string, confirm=false, group="Alert Messages", tooltip=ttlongentrystring)

useshortentryalert = input(defval=true, title="Use SELL Alert", group="Alert Messages")
shortentrystring = input(title="Sell Alert Message", defval=ttshortentrystring, type=input.string, confirm=false, group="Alert Messages", tooltip=ttshortentrystring)

uselongexitalert = input(defval=true, title="Use SELL Alert", group="Alert Messages")
longexitstring = input(title="Sell Alert Message", defval=ttlongexitstring, type=input.string, confirm=false, group="Alert Messages", tooltip=ttlongexitstring)

useshortexitalert = input(defval=true, title="Use SELL Alert", group="Alert Messages")
shortexitstring = input(title="Sell Alert Message", defval=ttshortexitstring, type=input.string, confirm=false, group="Alert Messages", tooltip=ttshortexitstring)

// usestopalert = input(defval=true, title="Use STOP Alert", group="Alert Messages")
// stopstring = input(title="Stop Alert Message", defval=ttstopstring, type=input.string, confirm=false, group="Alert Messages", tooltip=ttstopstring)

//Long
if tradetrendoption ? alternatelong and mabuy and longpositions : alternatelong and longpositions
	strategy.entry("longposition", strategy.long, comment="Long Entry")
	alert(longentrystring, alert.freq_once_per_bar)
if (shortentry or printstoplong) and longpositions
	strategy.close("longposition", comment="Long Exit")
	alert(longexitstring, alert.freq_once_per_bar)

//Short
if tradetrendoption ? alternateshort and masell and shortpositions : alternateshort and shortpositions
	strategy.entry("shortposition", strategy.short, comment=" Short Entry")
	alert(shortentrystring, alert.freq_once_per_bar)
if (longentry or printstopshort) and shortpositions
	strategy.close("shortposition", comment="Short Exit")
	alert(shortexitstring, alert.freq_once_per_bar)
	
	
//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////