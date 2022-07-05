
c="███████╗ █████╗  █████╗   ██╗   ██╗ █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗███╗  ██╗"
o="╚════██║██╔══██╗██╔══██╗  ██║   ██║██╔══██╗██║   ██║██╔════╝ ██║  ██║████╗ ██║"
d="  ███╔═╝███████║██║  ╚═╝  ╚██╗ ██╔╝███████║██║   ██║██║  ██╗ ███████║██╔██╗██║"
e="██╔══╝  ██╔══██║██║  ██╗   ╚████╔╝ ██╔══██║██║   ██║██║  ╚██╗██╔══██║██║╚████║"
r="███████╗██║  ██║╚█████╔╝    ╚██╔╝  ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║ ╚███║"
s="╚══════╝╚═╝  ╚═╝ ╚════╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝"

//@version=4
strategy("Seannie Test", overlay=true, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=15)

price = plot(close, title="Close Line", color=color.blue, display=display.none)

////////////////////////////////////////////////////////////////////////////////
//TREND INDICATORS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Trend EMA
tttradetrend = "Only place BUY or SELL orders with the direction of the Trend EMA."
tradetrendoption = input(false, title="Only Trade with Trend", tooltip=tttradetrend)
len111 = input(defval=200, minval=0, maxval=2000, title="Trend EMA Length")
src111 = close
out111 = ema(src111, len111)
ma111  = plot(out111, title="EMA 200", linewidth=2, color=color.blue, offset=0)
mabuy  = out111 > out111[1]
masell = out111 < out111[1]
//5 EMAs////////////////////////////////////////////////////////////////////////
len1 = 9
src1 = close
out1 = ema(src1, len1)
ema1color = (out1 > out1[1] ? #00bcd4 : #e91e63)
ema1 = plot(out1, title="EMA 9", linewidth=3, color=color.new(ema1color, 50), offset=0, display=display.none)
fill(price, ema1, title="EMA 9 Fill", color=color.new(ema1color, 90), editable=true)
len2 = 21
src2 = close
out2 = ema(src2, len2)
ema2color = (out2 > out2[1] ? #00bcd4 : #e91e63)
ema2 = plot(out2, title="EMA 21", linewidth=3, color=color.new(ema2color, 50), offset=0, display=display.none)
fill(price, ema2, title="EMA 21 Fill", color=color.new(ema2color, 90), editable=true)
len3 = 55
src3 = close
out3 = ema(src3, len3)
ema3color = (out3 > out3[1] ? #00bcd4 : #e91e63)
ema3 = plot(out3, title="EMA 55", linewidth=3, color=color.new(ema3color, 50), offset=0, display=display.none)
fill(price, ema3, title="EMA 55 Fill", color=color.new(ema3color, 90), editable=true)
len4 = 100
src4 = close
out4 = ema(src4, len4)
ema4color = (out4 > out4[1] ? #00bcd4 : #e91e63)
ema4 = plot(out4, title="EMA 100", linewidth=3, color=color.new(ema4color, 50), offset=0, display=display.none)
fill(price, ema4, title="EMA 100 Fill", color=color.new(ema4color, 90), editable=true)
len5 = 200
src5 = close
out5 = ema(src5, len5)
ema5color = (out5 > out5[1] ? #00bcd4 : #e91e63)
ema5 = plot(out5, title="EMA 200", linewidth=3, color=color.new(ema5color, 50), offset=0, display=display.none)
fill(price, ema5, title="EMA 200 Fill", color=color.new(ema5color, 90), editable=true)

//Supertrend////////////////////////////////////////////////////////////////////
atrPeriod = 10
factor = 3
[supertrend, direction] = supertrend(factor, atrPeriod)
bodyMiddle = plot((open + close) / 2, display=display.none, title="Body Middle Line")
uptrend = direction < 0 and direction[1] > 0[1] ? supertrend : na
downtrend = direction > 0 and direction[1] < 0[1] ? supertrend : na
//fill(bodyMiddle, upTrend, color.new(color.green, 90), fillgaps=false)
//fill(bodyMiddle, downTrend, color.new(color.red, 90), fillgaps=false)
//bullishsupertrend = supertrend < close and supertrend[1] > close
//plotshape(uptrend, style=shape.labelup, color=color.green, location=location.belowbar, size=size.large)

//HMA///////////////////////////////////////////////////////////////////////////
len6 = 100
src6 = close
hma = wma(2*wma(src6, len6/2)-wma(src6, len6), floor(sqrt(len6)))
hmacolor = close > hma ? #00bcd4 : #e91e63
plot(hma, title="HMA Line", color=color.new(hmacolor, 25), linewidth=5)

//Parabolic SAR/////////////////////////////////////////////////////////////////
start = 0.02
increment = 0.01
maximum = 0.2
psar = sar(start, increment, maximum)
//plot(psar, "ParabolicSAR", style=plot.style_circles, color=#ffffff)


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//MOMENTUM INCIDATORS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//RSI Divergence////////////////////////////////////////////////////////////////
len11 = 14
src11 = close
lbR11 = 2
lbL11 = 6
rangeUpper11 = 60
rangeLower11 = 5
plotBull11 = true
plotHiddenBull11 = false
plotBear11 = true
plotHiddenBear11 = false
bearColor11 = color.red
bullColor11 = color.green
hiddenBullColor11 = color.new(color.green, 80)
hiddenBearColor11 = color.new(color.red, 80)
textColor11 = color.white
noneColor11 = color.new(color.white, 100)
osc11 = rsi(src11, len11)

//plot(osc11, title="RSI", linewidth=2, color=#2962FF)
//hline(50, title="Middle Line", color=#787B86, linestyle=hline.style_dotted)
//obLevel11 = hline(70, title="Overbought", color=#787B86, linestyle=hline.style_dotted)
//osLevel11 = hline(30, title="Oversold", color=#787B86, linestyle=hline.style_dotted)
//fill(obLevel11, osLevel11, title="Background", color=color.rgb(33, 150, 243, 90))

plFound11 = na(pivotlow(osc11, lbL11, lbR11)) ? false : true
phFound11 = na(pivothigh(osc11, lbL11, lbR11)) ? false : true
_inRange11(cond) =>
	bars11 = barssince(cond == true)
	rangeLower11 <= bars11 and bars11 <= rangeUpper11

//Regular Bullish Divergence

//Osc: Higher Low
oscHL11 = osc11[lbR11] > valuewhen(plFound11, osc11[lbR11], 1) and _inRange11(plFound11[1])
//Price: Lower Low
priceLL11 = low[lbR11] < valuewhen(plFound11, low[lbR11], 1)

bullCond11 = plotBull11 and priceLL11 and oscHL11 and plFound11
//plot(plFound11 ? osc11[lbR11] : na, offset=-lbR11, title="Regular Bullish", linewidth=2, color=(bullCond11 ? bullColor11 : noneColor11))
//plotshape(bullCond11 ? osc11[lbR11] : na, offset=-lbR11, title="Regular Bullish Label", text=" Bull ", style=shape.labelup, location=location.absolute, color=bullColor11, textcolor=textColor11)

//Hidden Bullish Divergence

//Osc: Lower Low
oscLL11 = osc11[lbR11] < valuewhen(plFound11, osc11[lbR11], 1) and _inRange11(plFound11[1])
//Price: Higher Low
priceHL11 = low[lbR11] > valuewhen(plFound11, low[lbR11], 1)

hiddenBullCond11 = plotHiddenBull11 and priceHL11 and oscLL11 and plFound11
//plot(plFound11 ? osc11[lbR11] : na, offset=-lbR11, title="Hidden Bullish", linewidth=2, color=(hiddenBullCond11 ? hiddenBullColor11 : noneColor11))
//plotshape(hiddenBullCond11 ? osc11[lbR11] : na, offset=-lbR11, title="Hidden Bullish Label", text=" H Bull ", style=shape.labelup, location=location.absolute, color=bullColor11, textcolor=textColor11)
	 
//Regular Bearish Divergence

//Osc: Lower High
oscLH11 = osc11[lbR11] < valuewhen(phFound11, osc11[lbR11], 1) and _inRange11(phFound11[1])
//Price: Higher High
priceHH11 = high[lbR11] > valuewhen(phFound11, high[lbR11], 1)

bearCond11 = plotBear11 and priceHH11 and oscLH11 and phFound11
//plot(phFound11 ? osc11[lbR11] : na, offset=-lbR11, title="Regular Bearish", linewidth=2, color=(bearCond11 ? bearColor11 : noneColor11))
//plotshape(bearCond11 ? osc11[lbR11] : na, offset=-lbR11, title="Regular Bearish Label", text=" Bear ", style=shape.labeldown, location=location.absolute, color=bearColor11, textcolor=textColor11)
	 
//Hidden Bearish Divergence

//Osc: Higher High
oscHH11 = osc11[lbR11] > valuewhen(phFound11, osc11[lbR11], 1) and _inRange11(phFound11[1])
// Price: Lower High
priceLH11 = high[lbR11] < valuewhen(phFound11, high[lbR11], 1)

hiddenBearCond11 = plotHiddenBear11 and priceLH11 and oscHH11 and phFound11
//plot(phFound11 ? osc11[lbR11] : na, offset=-lbR11, title="Hidden Bearish", linewidth=2, color=(hiddenBearCond11 ? hiddenBearColor11 : noneColor11))
//plotshape(hiddenBearCond11 ? osc11[lbR11] : na, offset=-lbR11, title="Hidden Bearish Label", text=" H Bear ", style=shape.labeldown, location=location.absolute, color=bearColor11, textcolor=textColor11)

//MACD Divergence///////////////////////////////////////////////////////////////
fast_length12 = 12
slow_length12 = 26
src12 = close
signal_length12 = 9
sma_source12 = "EMA"
sma_signal12 = "EMA"
//Plot colors
col_macd12 = #2962FF
col_signal12 = #FF6D00
col_grow_above12 = #26A69A
col_fall_above12 = #B2DFDB
col_grow_below12 = #FFCDD2
col_fall_below12 = #FF5252
//Calculating
fast_ma12 = sma_source12 == "SMA" ? sma(src12, fast_length12) : ema(src12, fast_length12)
slow_ma12 = sma_source12 == "SMA" ? sma(src12, slow_length12) : ema(src12, slow_length12)
macd = fast_ma12 - slow_ma12
signal = sma_signal12 == "SMA" ? sma(macd, signal_length12) : ema(macd, signal_length12)
hist = macd - signal
//plot(hist, title="Histogram", style=plot.style_columns, color=(hist>=0 ? (hist[1] < hist ? col_grow_above12 : col_fall_above12) : (hist[1] < hist ? col_grow_below12 : col_fall_below12)))
//plot(macd, title="MACD", color=col_macd12)
//plot(signal, title="Signal", color=col_signal12)

donttouchzero12 = true

lbR12 = 2
lbL12 = 6
rangeUpper12 = 60
rangeLower12 = 5
plotBull12 = true
plotHiddenBull12 = false
plotBear12 = true
plotHiddenBear12 = false
bearColor12 = color.red
bullColor12 = color.green
hiddenBullColor12 = color.new(color.green, 80)
hiddenBearColor12 = color.new(color.red, 80)
textColor12 = color.white
noneColor12 = color.new(color.white, 100)
osc12 = macd

plFound12 = na(pivotlow(osc12, lbL12, lbR12)) ? false : true
phFound12 = na(pivothigh(osc12, lbL12, lbR12)) ? false : true
_inRange12(cond) =>
	bars12 = barssince(cond == true)
	rangeLower12 <= bars12 and bars12 <= rangeUpper12
	
//Regular Bullish Divergence

//Osc: Higher Low
oscHL12 = osc12[lbR12] > valuewhen(plFound12, osc12[lbR12], 1) and _inRange12(plFound12[1]) and  osc12[lbR12] < 0
// Price: Lower Low
priceLL12 = low[lbR12] < valuewhen(plFound12, low[lbR12], 1)
priceHHZero12 =  highest(osc12, lbL12+lbR12+5) 
//plot(priceHHZero,title="priceHHZero",color=color.green)
blowzero12 = donttouchzero12 ? priceHHZero12 < 0 : true

bullCond12 = plotBull12 and priceLL12 and oscHL12 and plFound12 and blowzero12
//plot(plFound12 ? osc12[lbR12] : na, offset=-lbR12, title="Regular Bullish", linewidth=2, color=(bullCond12 ? bullColor12 : noneColor12))
//plotshape(bullCond12 ? osc12[lbR12] : na, offset=-lbR12, title="Regular Bullish Label", text=" Bull ", style=shape.labelup, location=location.absolute, color=bullColor12, textcolor=textColor12)
	 
//Hidden Bullish Divergence

//Osc: Lower Low
oscLL12 = osc12[lbR12] < valuewhen(plFound12, osc12[lbR12], 1) and _inRange12(plFound12[1])
//Price: Higher Low
priceHL12 = low[lbR12] > valuewhen(plFound12, low[lbR12], 1)

hiddenBullCond12 = plotHiddenBull12 and priceHL12 and oscLL12 and plFound12
//plot(plFound12 ? osc12[lbR12] : na, offset=-lbR12, title="Hidden Bullish", linewidth=2, color=(hiddenBullCond12 ? hiddenBullColor12 : noneColor12))
//plotshape(hiddenBullCond12 ? osc12[lbR12] : na, offset=-lbR12, title="Hidden Bullish Label", text=" H Bull ", style=shape.labelup, location=location.absolute, color=bullColor12, textcolor=textColor12)
	 
//Regular Bearish Divergence

//Osc: Lower High
oscLH12 = osc12[lbR12] < valuewhen(phFound12, osc12[lbR12], 1) and _inRange12(phFound12[1])  and osc12[lbR12] > 0
priceLLZero12 =  lowest(osc12, lbL12+lbR12+5) 
//plot(priceLLZero,title="priceLLZero", color=color.red)
bearzero12 = donttouchzero12 ? priceLLZero12 > 0 : true
//Price: Higher High
priceHH12 = high[lbR12] > valuewhen(phFound12, high[lbR12], 1)

bearCond12 = plotBear12 and priceHH12 and oscLH12 and phFound12 and bearzero12
//plot(phFound12 ? osc12[lbR12] : na, offset=-lbR12, title="Regular Bearish", linewidth=2, color=(bearCond12 ? bearColor12 : noneColor12))
//plotshape(bearCond12 ? osc12[lbR12] : na, offset=-lbR12, title="Regular Bearish Label", text=" Bear ", style=shape.labeldown, location=location.absolute, color=bearColor12, textcolor=textColor12)
	 
//Hidden Bearish Divergence

//Osc: Higher High
oscHH12 = osc12[lbR12] > valuewhen(phFound12, osc12[lbR12], 1) and _inRange12(phFound12[1])
//Price: Lower High
priceLH12 = high[lbR12] < valuewhen(phFound12, high[lbR12], 1)

hiddenBearCond12 = plotHiddenBear12 and priceLH12 and oscHH12 and phFound12
//plot(phFound12 ? osc12[lbR12] : na, offset=-lbR12, title="Hidden Bearish", linewidth=2, color=(hiddenBearCond12 ? hiddenBearColor12 : noneColor12))
//plotshape(hiddenBearCond12 ? osc12[lbR12] : na, offset=-lbR12, title="Hidden Bearish Label", text=" H Bear ", style=shape.labeldown, location=location.absolute, color=bearColor12, textcolor=textColor12)
	 
	 
//Wave Trend Divergence/////////////////////////////////////////////////////////
n1 = 9
n2 = 12
ap = hlc3 
esa = ema(ap, n1)
d1 = ema(abs(ap - esa), n1)
ci = (ap - esa) / (0.015 * d1)
tci = ema(ci, n2)
hline = 0
wt1 = tci
wt2 = sma(wt1, 4)

//plot(hline, color=color.gray)
//plot(wt1, color=color.white)
//plot(wt2, color=color.blue)


//Divergence
lbR13 = 2
lbL13 = 6
rangeUpper13 = 60
rangeLower13 = 5
plotBull13 = true
plotHiddenBull13 = false
plotBear13 = true
plotHiddenBear13 = false

bearColor13 = color.red
bullColor13 = color.green
hiddenBullColor13 = color.green
hiddenBearColor13 = color.red
textColor13 = color.white
noneColor13 = color.new(color.white, 100)

k13 = wt1
d13 = wt2
osc13 = k13

plFound13 = na(pivotlow(osc13, lbL13, lbR13)) ? false : true
phFound13 = na(pivothigh(osc13, lbL13, lbR13)) ? false : true

_inRange13(cond) =>
    bars13 = barssince(cond == true)
    rangeLower13 <= bars13 and bars13 <= rangeUpper13

//Regular Bullish

//Osc: Higher Low
oscHL13 = osc13[lbR13] > valuewhen(plFound13, osc13[lbR13], 1) and _inRange13(plFound13[1])

//Price: Lower Low
priceLL13 = low[lbR13] < valuewhen(plFound13, low[lbR13], 1)

bullCond13 = plotBull13 and priceLL13 and oscHL13 and plFound13
//plot(plFound13 ? osc13[lbR13] : na, offset=-lbR13, title="Regular Bullish", linewidth=2, color=(bullCond13 ? bullColor13 : noneColor13))
//plotshape(bullCond13 ? osc13[lbR13] : na, offset=-lbR13, title="Regular Bullish Label", text=" Bull ", style=shape.labelup, location=location.absolute, color=bullColor13, textcolor=textColor13)

//Hidden Bullish

//Osc: Lower Low
oscLL13 = osc13[lbR13] < valuewhen(plFound13, osc13[lbR13], 1) and _inRange13(plFound13[1])

//Price: Higher Low
priceHL13 = low[lbR13] > valuewhen(plFound13, low[lbR13], 1)

hiddenBullCond13 = plotHiddenBull13 and priceHL13 and oscLL13 and plFound13
//plot(plFound13 ? osc13[lbR13] : na, offset=-lbR13, title="Hidden Bullish", linewidth=2, color=(hiddenBullCond13 ? hiddenBullColor13 : noneColor13))
//plotshape(hiddenBullCond13 ? osc13[lbR13] : na, offset=-lbR13, title="Hidden Bullish Label", text=" H Bull ", style=shape.labelup, location=location.absolute, color=bullColor13, textcolor=textColor13)
	 
//Regular Bearish

//Osc: Lower High
oscLH13 = osc13[lbR13] < valuewhen(phFound13, osc13[lbR13], 1) and _inRange13(phFound13[1])

//Price: Higher High
priceHH13 = high[lbR13] > valuewhen(phFound13, high[lbR13], 1)

bearCond13 = plotBear13 and priceHH13 and oscLH13 and phFound13
//plot(phFound13 ? osc13[lbR13] : na, offset=-lbR13, title="Regular Bearish", linewidth=2, color=(bearCond13 ? bearColor13 : noneColor13))
//plotshape(bearCond13 ? osc13[lbR13] : na, offset=-lbR13, title="Regular Bearish Label", text=" Bear ", style=shape.labeldown, location=location.absolute, color=bearColor13, textcolor=textColor13)

//Hidden Bearish

//Osc: Higher High
oscHH13 = osc13[lbR13] > valuewhen(phFound13, osc13[lbR13], 1) and _inRange13(phFound13[1])

//Price: Lower High
priceLH13 = high[lbR13] < valuewhen(phFound13, high[lbR13], 1)

hiddenBearCond13 = plotHiddenBear13 and priceLH13 and oscHH13 and phFound13
//plot(phFound13 ? osc13[lbR13] : na, offset=-lbR13, title="Hidden Bearish", linewidth=2, color=(hiddenBearCond13 ? hiddenBearColor13 : noneColor13))
//plotshape(hiddenBearCond13 ? osc13[lbR13] : na, offset=-lbR13, title="Hidden Bearish Label", text=" H Bear ", style=shape.labeldown, location=location.absolute, color=bearColor13, textcolor=textColor13)


//Stochastic Divergence/////////////////////////////////////////////////////////
periodK14 = 14
smoothK14 = 3
periodD14 = 3
k14 = sma(stoch(close, high, low, periodK14), smoothK14)
d14 = sma(k14, periodD14)
//plot(k14, title="%K", color=#2962FF)
//plot(d14, title="%D", color=#FF6D00)
//h0 = hline(80, "Upper Band", color=#787B86)
//h1 = hline(20, "Lower Band", color=#787B86)
//fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")

//Divergence
lbR14 = 2
lbL14 = 6
rangeUpper14 = 60
rangeLower14 = 5
plotBull14 = true
plotHiddenBull14 = false
plotBear14 = true
plotHiddenBear14 = false

bearColor14 = color.red
bullColor14 = color.green
hiddenBullColor14 = color.green
hiddenBearColor14 = color.red
textColor14 = color.white
noneColor14 = color.new(color.white, 100)

osc14 = k14

plFound14 = na(pivotlow(osc14, lbL14, lbR14)) ? false : true
phFound14 = na(pivothigh(osc14, lbL14, lbR14)) ? false : true

_inRange14(cond) =>
    bars14 = barssince(cond == true)
    rangeLower14 <= bars14 and bars14 <= rangeUpper14

//Regular Bullish

//Osc: Higher Low
oscHL14 = osc14[lbR14] > valuewhen(plFound14, osc14[lbR14], 1) and _inRange14(plFound14[1])

//Price: Lower Low
priceLL14 = low[lbR14] < valuewhen(plFound14, low[lbR14], 1)

bullCond14 = plotBull14 and priceLL14 and oscHL14 and plFound14
//plot(plFound14 ? osc14[lbR14] : na, offset=-lbR14, title="Regular Bullish", linewidth=2, color=(bullCond14 ? bullColor14 : noneColor14))
//plotshape(bullCond14 ? osc14[lbR14] : na, offset=-lbR14, title="Regular Bullish Label", text=" Bull ", style=shape.labelup, location=location.absolute, color=bullColor14, textcolor=textColor14)

//Hidden Bullish

//Osc: Lower Low
oscLL14 = osc14[lbR14] < valuewhen(plFound14, osc14[lbR14], 1) and _inRange14(plFound14[1])

//Price: Higher Low
priceHL14 = low[lbR14] > valuewhen(plFound14, low[lbR14], 1)

hiddenBullCond14 = plotHiddenBull14 and priceHL14 and oscLL14 and plFound14
//plot(plFound14 ? osc14[lbR14] : na, offset=-lbR14, title="Hidden Bullish", linewidth=2, color=(hiddenBullCond14 ? hiddenBullColor14 : noneColor14))
//plotshape(hiddenBullCond14 ? osc14[lbR14] : na, offset=-lbR14, title="Hidden Bullish Label", text=" H Bull ", style=shape.labelup, location=location.absolute, color=bullColor14, textcolor=textColor14)

//Regular Bearish

//Osc: Lower High
oscLH14 = osc14[lbR14] < valuewhen(phFound14, osc14[lbR14], 1) and _inRange14(phFound14[1])

//Price: Higher High
priceHH14 = high[lbR14] > valuewhen(phFound14, high[lbR14], 1)

bearCond14 = plotBear14 and priceHH14 and oscLH14 and phFound14
//plot(phFound14 ? osc14[lbR14] : na, offset=-lbR14, title="Regular Bearish", linewidth=2, color=(bearCond14 ? bearColor14 : noneColor14))
//plotshape(bearCond14 ? osc14[lbR14] : na, offset=-lbR14, title="Regular Bearish Label", text=" Bear ", style=shape.labeldown, location=location.absolute, color=bearColor14, textcolor=textColor14)
	 
//Hidden Bearish

//Osc: Higher High
oscHH14 = osc14[lbR14] > valuewhen(phFound14, osc14[lbR14], 1) and _inRange14(phFound14[1])

//Price: Lower High
priceLH14 = high[lbR14] < valuewhen(phFound14, high[lbR14], 1)

hiddenBearCond14 = plotHiddenBear14 and priceLH14 and oscHH14 and phFound14
//plot(phFound14 ? osc14[lbR14] : na, offset=-lbR14, title="Hidden Bearish", linewidth=2, color=(hiddenBearCond14 ? hiddenBearColor14 : noneColor14))
//plotshape(hiddenBearCond14 ? osc14[lbR14] : na, offset=-lbR14, title="Hidden Bearish Label", text=" H Bear ", style=shape.labeldown, location=location.absolute, color=bearColor14, textcolor=textColor14)


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//VOLATILITY INDICATORS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Bollinger Bands///////////////////////////////////////////////////////////////
length1 = 20
src7 = close
mult1 = 2.0
basis = sma(src7, length1)
dev = mult1 * stdev(src7, length1)
upper = basis + dev
lower = basis - dev
offset = 0
//plot(basis, "Basis", color=#FF6D00, offset = offset)
//p1 = plot(upper, "Upper", color=#2962FF, offset = 0)
//p2 = plot(lower, "Lower", color=#2962FF, offset = 0)
//fill(p1, p2, title = "Background", color=color.rgb(33, 150, 243, 95))


//Average True Range /////////////////////////////////////////////////
length2 = 1
mult2 = 1.85
showLabels = true
useClose = false
highlightState = false

atr = mult2 * atr(length2)

longStop = (useClose ? highest(close, length2) : highest(length2)) - atr
longStopPrev = nz(longStop[1], longStop) 
longStop := close[1] > longStopPrev ? max(longStop, longStopPrev) : longStop

shortStop = (useClose ? lowest(close, length2) : lowest(length2)) + atr
shortStopPrev = nz(shortStop[1], shortStop)
shortStop := close[1] < shortStopPrev ? min(shortStop, shortStopPrev) : shortStop

var int dir = 1
dir := close > shortStopPrev ? 1 : close < longStopPrev ? -1 : dir

var color longColor = color.green
var color shortColor = color.red

buySignal = dir == 1 and dir[1] == -1
//plotshape(buySignal and showLabels ? longStop : na, title="Gold Buy", text="Buy", location=location.belowbar, style=shape.labelup, size=size.tiny, color=longColor, textcolor=color.new(color.white, 0))

sellSignal = dir == -1 and dir[1] == 1
//plotshape(sellSignal and showLabels ? shortStop : na, title="Gold Sell", text="Sell", location=location.abovebar, style=shape.labeldown, size=size.tiny, color=shortColor, textcolor=color.new(color.white, 0))


//Relative Volatility Index Divergence//////////////////////////////////////////
length15 = 12
src15 = close
len15 = 14
stddev15 = stdev(src15, length15)
upper15 = ema(change(src15) <= 0 ? 0 : stddev15, len15)
lower15 = ema(change(src15) > 0 ? 0 : stddev15, len15)
rvi = upper15 / (upper15 + lower15) * 100
//h0 = hline(80, "Upper Band", color=#787B86)
//h1 = hline(20, "Lower Band", color=#787B86)
//fill(h0, h1, color=color.rgb(126, 87, 194, 90), title="Background")
//plot(rvi15, title="RVI", color=#7E57C2, offset = offset)

//Divergence
lbR15 = 2
lbL15 = 6
rangeUpper15 = 60
rangeLower15 = 5
plotBull15 = true
plotHiddenBull15 = false
plotBear15 = true
plotHiddenBear15 = false

bearColor15 = color.red
bullColor15 = color.green
hiddenBullColor15 = color.green
hiddenBearColor15 = color.red
textColor15 = color.white
noneColor15 = color.new(color.white, 100)

d15 = rvi
osc15 = d15

plFound15 = na(pivotlow(osc15, lbL15, lbR15)) ? false : true
phFound15 = na(pivothigh(osc15, lbL15, lbR15)) ? false : true

_inRange15(cond) =>
    bars15 = barssince(cond == true)
    rangeLower15 <= bars15 and bars15 <= rangeUpper15

//Regular Bullish

//Osc: Higher Low
oscHL15 = osc15[lbR15] > valuewhen(plFound15, osc15[lbR15], 1) and _inRange15(plFound15[1])

//Price: Lower Low
priceLL15 = low[lbR15] < valuewhen(plFound15, low[lbR15], 1)

bullCond15 = plotBull15 and priceLL15 and oscHL15 and plFound15
//plot(plFound15 ? osc15[lbR15] : na, offset=-lbR15, title="Regular Bullish", linewidth=2, color=(bullCond15 ? bullColor15 : noneColor15))
//plotshape(bullCond15 ? osc15[lbR15] : na, offset=-lbR15, title="Regular Bullish Label", text=" Bull ", style=shape.labelup, location=location.absolute, color=bullColor15, textcolor=textColor15)

//Hidden Bullish

//Osc: Lower Low
oscLL15 = osc15[lbR15] < valuewhen(plFound15, osc15[lbR15], 1) and _inRange15(plFound15[1])

//Price: Higher Low
priceHL15 = low[lbR15] > valuewhen(plFound15, low[lbR15], 1)

hiddenBullCond15 = plotHiddenBull15 and priceHL15 and oscLL15 and plFound15
//plot(plFound15 ? osc15[lbR15] : na, offset=-lbR15, title="Hidden Bullish", linewidth=2, color=(hiddenBullCond15 ? hiddenBullColor15 : noneColor15))
//plotshape(hiddenBullCond15 ? osc15[lbR15] : na, offset=-lbR15, title="Hidden Bullish Label", text=" H Bull ", style=shape.labelup, location=location.absolute, color=bullColor15, textcolor=textColor15)
	 
//Regular Bearish

//Osc: Lower High
oscLH15 = osc15[lbR15] < valuewhen(phFound15, osc15[lbR15], 1) and _inRange15(phFound15[1])

//Price: Higher High
priceHH15 = high[lbR15] > valuewhen(phFound15, high[lbR15], 1)

bearCond15 = plotBear15 and priceHH15 and oscLH15 and phFound15
//plot(phFound15 ? osc15[lbR15] : na, offset=-lbR15, title="Regular Bearish", linewidth=2, color=(bearCond15 ? bearColor15 : noneColor15))
//plotshape(bearCond15 ? osc15[lbR15] : na, offset=-lbR15, title="Regular Bearish Label", text=" Bear ", style=shape.labeldown, location=location.absolute, color=bearColor15, textcolor=textColor15)

//Hidden Bearish

//Osc: Higher High
oscHH15 = osc15[lbR15] > valuewhen(phFound15, osc15[lbR15], 1) and _inRange15(phFound15[1])

//Price: Lower High
priceLH15 = high[lbR15] < valuewhen(phFound15, high[lbR15], 1)

hiddenBearCond15 = plotHiddenBear15 and priceLH15 and oscHH15 and phFound15
//plot(phFound15 ? osc15[lbR15] : na, offset=-lbR15, title="Hidden Bearish", linewidth=2, color=(hiddenBearCond15 ? hiddenBearColor15 : noneColor15))
//plotshape(hiddenBearCond15 ? osc15[lbR15] : na, offset=-lbR15, title="Hidden Bearish Label", text=" H Bear ", style=shape.labeldown, location=location.absolute, color=bearColor15, textcolor=textColor15)

//Support and Resistance////////////////////////////////////////////////////////
left16 = 200
right16 = 20
quick_right16 = 5
src16 = "Close"

pivot_high16 = iff(src16=="Close",pivothigh(close,left16,right16),pivothigh(high,left16,right16))
pivot_lows16 = iff(src16=="Close",pivotlow(close, left16,right16),pivotlow(low,left16,right16))

quick_pivot_high16 = iff(src16=="Close",pivothigh(close,left16,quick_right16),pivothigh(high,left16,quick_right16))
quick_pivot_lows16 = iff(src16=="Close",pivotlow(close, left16,quick_right16),pivotlow(low, left16,quick_right16))

level1 = iff(src16=="Close",valuewhen(quick_pivot_high16, close[quick_right16], 0),valuewhen(quick_pivot_high16, high[quick_right16], 0))
level2 = iff(src16=="Close",valuewhen(quick_pivot_lows16, close[quick_right16], 0),valuewhen(quick_pivot_lows16, low[quick_right16], 0))
level3 = iff(src16=="Close",valuewhen(pivot_high16, close[right16], 0),valuewhen(pivot_high16, high[right16], 0))
level4 = iff(src16=="Close",valuewhen(pivot_lows16, close[right16], 0),valuewhen(pivot_lows16, low[right16], 0))
level5 = iff(src16=="Close",valuewhen(pivot_high16, close[right16], 1),valuewhen(pivot_high16, high[right16], 1))
level6 = iff(src16=="Close",valuewhen(pivot_lows16, close[right16], 1),valuewhen(pivot_lows16, low[right16], 1))
level7 = iff(src16=="Close",valuewhen(pivot_high16, close[right16], 2),valuewhen(pivot_high16, high[right16], 2))
level8 = iff(src16=="Close",valuewhen(pivot_lows16, close[right16], 2),valuewhen(pivot_lows16, low[right16], 2))

level1_col = close >= level1 ? color.green : color.red
level2_col = close >= level2 ? color.green : color.red
level3_col = close >= level3 ? color.green : color.red
level4_col = close >= level4 ? color.green : color.red
level5_col = close >= level5 ? color.green : color.red
level6_col = close >= level6 ? color.green : color.red
level7_col = close >= level7 ? color.green : color.red
level8_col = close >= level8 ? color.green : color.red

length17 = 9
src17 = close
hma17 = wma(2*wma(src17, length17/2)-wma(src17, length17), floor(sqrt(length17)))

buy1 = hma17 > level1 and hma17[1] < level1[1] and close > close[2]
buy2 = hma17 > level2 and hma17[1] < level2[1] and close > close[2]
buy3 = hma17 > level3 and hma17[1] < level3[1] and close > close[2]
buy4 = hma17 > level4 and hma17[1] < level4[1] and close > close[2]
buy5 = hma17 > level5 and hma17[1] < level5[1] and close > close[2]
buy6 = hma17 > level6 and hma17[1] < level6[1] and close > close[2]
buy7 = hma17 > level7 and hma17[1] < level7[1] and close > close[2]
buy8 = hma17 > level8 and hma17[1] < level8[1] and close > close[2]

sell1 = hma17 < level1 and hma17[1] > level1[1] and close < close[2]
sell2 = hma17 < level2 and hma17[1] > level2[1] and close < close[2]
sell3 = hma17 < level3 and hma17[1] > level3[1] and close < close[2]
sell4 = hma17 < level4 and hma17[1] > level4[1] and close < close[2]
sell5 = hma17 < level5 and hma17[1] > level5[1] and close < close[2]
sell6 = hma17 < level6 and hma17[1] > level6[1] and close < close[2]
sell7 = hma17 < level7 and hma17[1] > level7[1] and close < close[2]
sell8 = hma17 < level8 and hma17[1] > level8[1] and close < close[2]


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//VOLUME INDICATORS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//OBV Divergence////////////////////////////////////////////////////////////////
len18 = 20
src18 = close
lbR18 = 2
lbL18 = 6
rangeUpper18 = 60
rangeLower18 = 5
plotBull18 = true
plotHiddenBull18 = false
plotBear18 = true
plotHiddenBear18 = false


bearColor18 = color.red
bullColor18 = color.green
hiddenBullColor18 = color.green
hiddenBearColor18 = color.new(color.red, 80)
textColor18 = color.white
noneColor18 = color.new(color.white, 100)

csrc = change(src18)
obv1(src18) => cum(change(src18) > 0 ? volume : csrc < 0 ? -volume : 0*volume)
os = obv1(src18)
obv_osc = (os - ema(os,len18))
obc_color=obv_osc > 0 ? color.green : color.red
//plot(obv_osc, color=obc_color, style=plot.style_line,title="OBV-Points", linewidth=2)
//plot(obv_osc, color=color.silver, transp=70, title="OBV", style=plot.style_area)
//hline(0)

plFound18 = na(pivotlow(obv_osc, lbL18, lbR18)) ? false : true
phFound18 = na(pivothigh(obv_osc, lbL18, lbR18)) ? false : true

_inRange(cond) =>
    bars = barssince(cond == true)
    rangeLower18 <= bars and bars <= rangeUpper18

// Regular Bullish

// Osc: Higher Low
oscHL18 = obv_osc[lbR18] > valuewhen(plFound18, obv_osc[lbR18], 1) and _inRange(plFound18[1])

// Price: Lower Low
priceLL18 = low[lbR18] < valuewhen(plFound18, low[lbR18], 1)
bullCond18 = plotBull18 and priceLL18 and oscHL18 and plFound18
//plot(plFound18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Regular Bullish",linewidth=2,color=(bullCond18 ? bullColor18 : noneColor18))
//plotshape(bullCond18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Regular Bullish Label",text=" Bull ",style=shape.labelup,location=location.absolute,color=bullColor18,textcolor=textColor18)

// Hidden Bullish

// Osc: Lower Low
oscLL18 = obv_osc[lbR18] < valuewhen(plFound18, obv_osc[lbR18], 1) and _inRange(plFound18[1])

// Price: Higher Low
priceHL18 = low[lbR18] > valuewhen(plFound18, low[lbR18], 1)
hiddenBullCond18 = plotHiddenBull18 and priceHL18 and oscLL18 and plFound18
//plot(plFound18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Hidden Bullish",linewidth=2,color=(hiddenBullCond18 ? hiddenBullColor18 : noneColor18))
//plotshape(hiddenBullCond18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Hidden Bullish Label",text=" H Bull ",style=shape.labelup,location=location.absolute,color=bullColor18,textcolor=textColor18)

// Regular Bearish

// Osc: Lower High
oscLH18 = obv_osc[lbR18] < valuewhen(phFound18, obv_osc[lbR18], 1) and _inRange(phFound18[1])

// Price: Higher High
priceHH18 = high[lbR18] > valuewhen(phFound18, high[lbR18], 1)
bearCond18 = plotBear18 and priceHH18 and oscLH18 and phFound18
//plot(phFound18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Regular Bearish",linewidth=2,color=(bearCond18 ? bearColor18 : noneColor18))
//plotshape(bearCond18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Regular Bearish Label",text=" Bear ",style=shape.labeldown,location=location.absolute,color=bearColor18,textcolor=textColor18)

// Hidden Bearish

// Osc: Higher High
oscHH18 = obv_osc[lbR18] > valuewhen(phFound18, obv_osc[lbR18], 1) and _inRange(phFound18[1])

// Price: Lower High
priceLH18 = high[lbR18] < valuewhen(phFound18, high[lbR18], 1)
hiddenBearCond18 = plotHiddenBear18 and priceLH18 and oscHH18 and phFound18
//plot(phFound18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Hidden Bearish",linewidth=2,color=(hiddenBearCond18 ? hiddenBearColor18 : noneColor18))
//plotshape(hiddenBearCond18 ? obv_osc[lbR18] : na,offset=-lbR18,title="Hidden Bearish Label",text=" H Bear ",style=shape.labeldown,location=location.absolute,color=bearColor18,textcolor=textColor18)


//Chaikin Money Flow////////////////////////////////////////////////////////////
length19 = 50
ad19 = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
cmf = sum(ad19, length19) / sum(volume, length19)
//plot(cmf, color=#43A047, title="MF")
//hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)

//VWAP//////////////////////////////////////////////////////////////////////////
computeVWAP(src20, isNewPeriod, stDevMultiplier) =>
	var float sumSrcVol = na
	var float sumVol = na
    var float sumSrcSrcVol = na
    
	sumSrcVol := isNewPeriod ? src20 * volume : src20 * volume + sumSrcVol[1]
	sumVol := isNewPeriod ? volume : volume + sumVol[1]
	// sumSrcSrcVol calculates the dividend of the equation that is later used to calculate the standard deviation
	sumSrcSrcVol := isNewPeriod ? volume * pow(src20, 2) : volume * pow(src20, 2) + sumSrcSrcVol[1]
	
	_vwap = sumSrcVol / sumVol
	variance = sumSrcSrcVol / sumVol - pow(_vwap, 2)
	variance := variance < 0 ? 0 : variance
	stDev = sqrt(variance)
	
	lowerBand20 = _vwap - stDev * stDevMultiplier
	upperBand20 = _vwap + stDev * stDevMultiplier
	
	[_vwap, lowerBand20, upperBand20]

hideonDWM = false
var anchor = "Session"
src20 = hlc3
offset20 = 0

showBands = true
stdevMult = 1.0

timeChange(period) =>
	change(time(period))

new_earnings = earnings(syminfo.tickerid, earnings.actual, barmerge.gaps_on, barmerge.lookahead_on)
new_dividends = dividends(syminfo.tickerid, dividends.gross, barmerge.gaps_on, barmerge.lookahead_on)
new_split = splits(syminfo.tickerid, splits.denominator, barmerge.gaps_on, barmerge.lookahead_on)

tcD = timeChange("D")
tcW = timeChange("W")
tcM = timeChange("M")
tc3M = timeChange("3M")
tc12M = timeChange("12M")

isNewPeriod = anchor == "Earnings" ? new_earnings :
 anchor == "Dividends" ? new_dividends :
 anchor == "Splits" ? new_split :
 na(src20[1]) ? true :
 anchor == "Session" ? tcD :
 anchor == "Week" ? tcW :
 anchor == "Month" ? tcM :
 anchor == "Quarter" ? tc3M :
 anchor == "Year" ? tc12M :
 anchor == "Decade" ? tc12M and year % 10 == 0 :
 anchor == "Century" ? tc12M and year % 100 == 0 :
 false
	
float vwapValue = na
float std = na
float upperBandValue = na
float lowerBandValue = na

if not (hideonDWM and timeframe.isdwm)
    [_vwap, bottom, top] = computeVWAP(src20, isNewPeriod, stdevMult)
    vwapValue := _vwap
    upperBandValue := showBands ? top : na
    lowerBandValue := showBands ? bottom : na

//plot(vwapValue, title="VWAP", color=#2962FF, offset=offset)

//upperBand20 = plot(upperBandValue, title="Upper Band", color=color.green, offset=offset)
//lowerBand20 = plot(lowerBandValue, title="Lower Band", color=color.green, offset=offset)

//fill(upperBand20, lowerBand20, title="Bands Fill", color= showBands ? color.new(color.green, 95) : na)

//Candle Patterns///////////////////////////////////////////////////////////////

//Bullish Engulfing
C_DownTrend = true
C_UpTrend = true
var trendRule1 = "SMA50"
var trendRule2 = "SMA50, SMA200"
var trendRule = trendRule1

if trendRule == trendRule1
	priceAvg = sma(close, 50)
	C_DownTrend := close < priceAvg
	C_UpTrend := close > priceAvg

if trendRule == trendRule2
	sma200 = sma(close, 200)
	sma50 = sma(close, 50)
	C_DownTrend := close < sma50 and sma50 < sma200
	C_UpTrend := close > sma50 and sma50 > sma200
C_Len = 14 // ema depth for bodyAvg
C_ShadowPercent = 5.0 // size of shadows
C_ShadowEqualsPercent = 100.0
C_DojiBodyPercent = 5.0
C_Factor = 2.0 // shows the number of times the shadow dominates the candlestick body

C_BodyHi = max(close, open)
C_BodyLo = min(close, open)
C_Body = C_BodyHi - C_BodyLo
C_BodyAvg = ema(C_Body, C_Len)
C_SmallBody = C_Body < C_BodyAvg
C_LongBody = C_Body > C_BodyAvg
C_UpShadow = high - C_BodyHi
C_DnShadow = C_BodyLo - low
C_HasUpShadow = C_UpShadow > C_ShadowPercent / 100 * C_Body
C_HasDnShadow = C_DnShadow > C_ShadowPercent / 100 * C_Body
C_WhiteBody = open < close
C_BlackBody = open > close
C_Range = high-low
C_IsInsideBar = C_BodyHi[1] > C_BodyHi and C_BodyLo[1] < C_BodyLo
C_BodyMiddle = C_Body / 2 + C_BodyLo
C_ShadowEquals = C_UpShadow == C_DnShadow or (abs(C_UpShadow - C_DnShadow) / C_DnShadow * 100) < C_ShadowEqualsPercent and (abs(C_DnShadow - C_UpShadow) / C_UpShadow * 100) < C_ShadowEqualsPercent
C_IsDojiBody = C_Range > 0 and C_Body <= C_Range * C_DojiBodyPercent / 100
C_Doji = C_IsDojiBody and C_ShadowEquals

patternLabelPosLow = low - (atr(30) * 0.6)
patternLabelPosHigh = high + (atr(30) * 0.6)

label_color_bullish = color.blue
C_EngulfingBullishNumberOfCandles = 2
C_EngulfingBullish = C_DownTrend and C_WhiteBody and C_LongBody and C_BlackBody[1] and C_SmallBody[1] and close >= open[1] and open <= close[1] and ( close > open[1] or open < close[1] )
if C_EngulfingBullish
    var ttBullishEngulfing = "Engulfing\nAt the end of a given downward trend, there will most likely be a reversal pattern. To distinguish the first day, this candlestick pattern uses a small body, followed by a day where the candle body fully overtakes the body from the day before, and closes in the trend’s opposite direction. Although similar to the outside reversal chart pattern, it is not essential for this pattern to completely overtake the range (high to low), rather only the open and the close."
    //label.new(bar_index, patternLabelPosLow, text="BE", style=label.style_label_up, color = label_color_bullish, textcolor=color.white, tooltip = ttBullishEngulfing)
//bgcolor(highest(C_EngulfingBullish?1:0, C_EngulfingBullishNumberOfCandles)!=0 ? color.blue : na, offset=-(C_EngulfingBullishNumberOfCandles-1))

//Bearish Engulfing
label_color_bearish = color.red
C_EngulfingBearishNumberOfCandles = 2
C_EngulfingBearish = C_UpTrend and C_BlackBody and C_LongBody and C_WhiteBody[1] and C_SmallBody[1] and close <= open[1] and open >= close[1] and ( close < open[1] or open > close[1] )
if C_EngulfingBearish
    var ttBearishEngulfing = "Engulfing\nAt the end of a given uptrend, a reversal pattern will most likely appear. During the first day, this candlestick pattern uses a small body. It is then followed by a day where the candle body fully overtakes the body from the day before it and closes in the trend’s opposite direction. Although similar to the outside reversal chart pattern, it is not essential for this pattern to fully overtake the range (high to low), rather only the open and the close."
    //label.new(bar_index, patternLabelPosHigh, text="BE", style=label.style_label_down, color = label_color_bearish, textcolor=color.white, tooltip = ttBearishEngulfing)
//bgcolor(highest(C_EngulfingBearish?1:0, C_EngulfingBearishNumberOfCandles)!=0 ? color.red : na, offset=-(C_EngulfingBearishNumberOfCandles-1))


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//SIGNAL SCORES▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Alternate Signals Option
alternatesignals = input(title='Alternate Signals', defval=false)

//Position Options
longpositions = input(title='Long Positions', defval=true)
shortpositions = input(title='Short Positions', defval=true)

//Stop Loss Warning Option
stoplosspercent = input(title='Stop Loss Warning (%)', defval=-0.8, minval=-50, maxval=0, step=.1) / 100

//Score Requirements
stronglongscore = input(defval=10, minval=0, maxval=1000, title='Required Strong LONG Score')
strongshortscore = input(defval=10, minval=0, maxval=1000, title='Required Strong SHORT Score')
weaklongscore = input(defval=8, minval=0, maxval=1000, title='Required Weak LONG Score')
weakshortscore = input(defval=8, minval=0, maxval=1000, title='Required Weak SHORT Score')

//Trend Indicator Signals///////////////////////////////////////////////////////

//EMA Signals
emadirectionimportance = input(defval=4, minval=0, maxval=100, title='EMA Trend Direction Importance')
emadirectionup = out5 < close ? emadirectionimportance : 0
emadirectionupstatus = emadirectionup ? 'EMA Trend Direction Up' : na
emadirectiondown = out5 > close ? emadirectionimportance : 0
emadirectiondownstatus = emadirectiondown ? 'EMA Trend Direction Down' : na

emapushpullimportance = input(defval=5, minval=0, maxval=100, title='EMA Pressure Importance')
emapushup = out2 > out2[1] and out3 < out3[1] ? emapushpullimportance : 0
emapushupstatus = emapushup ? 'EMA Pushing Up' : na
emapulldown = out2 < out2[1] and out3 > out3[1] ? emapushpullimportance : 0
emapulldownstatus = emapulldown ? 'EMA Pulling Down' : na

//Super Trend Signals
supertrenddirimportance = input(defval=0, minval=0, maxval=100, title='SuperTrend Direction Importance')
supertrendup = direction < 0 ? supertrenddirimportance : 0
supertrendupstatus = supertrendup ? 'SuperTrend Direction Up' : na
supertrenddown = direction > 0 ? supertrenddirimportance : 0
supertrenddownstatus = supertrenddown ? 'SuperTrend Direction Down' : na

supertrendrevimportance = input(defval=0, minval=0, maxval=100, title='SuperTrend Reversal Importance')
supertrendrevup = direction < 0 and direction[1] > 0[1] ? supertrendrevimportance : 0
supertrendrevupstatus = supertrendrevup ? 'SuperTrend Reversed Up' : na
supertrendrevdown = direction > 0 and direction[1] < 0[1] ? supertrendrevimportance : 0
supertrendrevdownstatus = supertrendrevdown ? 'SuperTrend Reversed Down' : na

//Parabolic SAR Signals
psardirimportance = input(defval=0, minval=0, maxval=100, title='Parabolic SAR Direction Importance')
psardirup = psar < close ? psardirimportance : 0
psardirupstatus = psardirup ? 'PSAR Direction Up' : na
psardirdown = psar > close ? psardirimportance : 0
psardirdownstatus = psardirdown ? 'PSAR Direction Down' : na

psarrevimportance = input(defval=2, minval=0, maxval=100, title='Parabolic SAR Reversal Importance')
psarrevup = psar < close and psar[1] > close[1] ? psarrevimportance : 0
psarrevupstatus = psarrevup ? 'PSAR Reversed Up' : na
psarrevdown = psar > close and psar[1] < close ? psarrevimportance : 0
psarrevdownstatus = psarrevdown ? 'PSAR Reversed Down' : na

//HMA Signals
hmacloseposimportance = input(defval=0, minval=0, maxval=100, title='HMA Trend Direction Importance')
hmacloseposup = hma < close and hma[1] ? hmacloseposimportance : 0
hmacloseposupstatus = hmacloseposup ? 'Price Crossed Over HMA' : na
hmacloseposdown = hma > close ? hmacloseposimportance : 0
hmacloseposdownstatus = hmacloseposdown ? 'Price Crossed Under HMA' : na

hmapivotimportance = input(defval=5, minval=0, maxval=100, title='HMA Pivot Importance')
hmapivotup = hma > hma[1] and hma[1] < hma[2] ? hmapivotimportance : 0
hmapivotupstatus = hmapivotup ? 'HMA Pivot Up' : na
hmapivotdown = hma < hma[1] and hma[1] > hma[2] ? hmapivotimportance : 0
hmapivotdownstatus = hmapivotdown ? 'HMA Pivot Down' : na

//Momentum Indicator Signals////////////////////////////////////////////////////

//RSI Signals
rsidivimportance = input(defval=4, minval=0, maxval=100, title='RSI Divergence Importance')
rsidivup = bullCond11 or bullCond11[1] or bullCond11[2] ? rsidivimportance : 0
rsidivupstatus = rsidivup ? 'Bullish RSI Divergence' : na
rsidivdown = bearCond11 or bearCond11[1] or bearCond11[2] ? rsidivimportance : 0
rsidivdownstatus = rsidivdown ? 'Bearish RSI Divergence' : na

rsilevelimportance = input(defval=2, minval=0, maxval=100, title='RSI Level Importance')
rsioversold = osc11 < 30 ? rsilevelimportance : 0
rsioversoldstatus = rsioversold ? 'RSI Oversold' : na
rsioverbought = osc11 > 70 ? rsilevelimportance : 0
rsioverboughtstatus = rsioverbought ? 'RSI Overbought' : na

rsidirectionimportance = input(defval=1, minval=0, maxval=100, title='RSI Cross 50-Line Importance')
rsicrossup = osc11 > 50 and osc11[1] < 50 or osc11 > 50 and osc11[2] < 50 ? rsidirectionimportance : 0
rsicrossupstatus = rsicrossup ? 'RSI Crossed 50-Line Up' : na
rsicrossdown = osc11 < 50 and osc11[1] > 50 or osc11 < 50 and osc11[2] > 50 ? rsidirectionimportance : 0
rsicrossdownstatus = rsicrossdown ? 'RSI Crossed 50-Line Down' : na

//MACD Signals
macddivimportance = input(defval=7, minval=0, maxval=100, title='MACD Divergence Importance')
macddivup = bullCond12 or bullCond12[1] or bullCond12[2] ? macddivimportance : 0
macddivupstatus = macddivup ? 'Bullish MACD Divergence' : na
macddivdown = bearCond12 or bearCond12[1] or bearCond12[2] ? macddivimportance : 0
macddivdownstatus = macddivdown ? 'Bearish MACD Divergence' : na

histpivotimportance = input(defval=0, minval=0, maxval=100, title='MACD Histogram Pivot Importance')
histpivotup = hist > hist[1] and hist[1] < hist[2] and hist < 0 ? histpivotimportance : 0
histpivotupstatus = histpivotup ? 'MACD Histogram Pivot Up' : na
histpivotdown = hist < hist[1] and hist[1] > hist[2] and hist > 0 ? histpivotimportance : 0
histpivotdownstatus = histpivotdown ? 'MACD Histogram Pivot Down' : na

macdcrosssignalimportance = input(defval=0, minval=0, maxval=100, title='MACD Cross Signal Importance')
macdcrosssignalup = macd > signal and macd[1] < signal[1] and signal < 0 ? macdcrosssignalimportance : 0
macdcrosssignalupstatus = macdcrosssignalup ? 'MACD Crossed Signal Up' : na
macdcrosssignaldown = macd < signal and macd[1] > signal[1] and signal > 0 ? macdcrosssignalimportance : 0
macdcrosssignaldownstatus = macdcrosssignaldown ? 'MACD Crossed Signal Down' : na

//WaveTrend Signals
wtdivimportance = input(defval=3, minval=0, maxval=100, title='WaveTrend Divergence Importance')
wtdivup = bullCond13 or bullCond13[1] or bullCond13[2] ? wtdivimportance : 0
wtdivupstatus = wtdivup ? 'Bullish WaveTrend Divergence' : na
wtdivdown = bearCond13 or bearCond13[1] or bearCond13[2] ? wtdivimportance : 0
wtdivdownstatus = wtdivdown ? 'Bearish WaveTrend Divergence' : na

wtcrosssignalimportance = input(defval=2, minval=0, maxval=100, title='WaveTrend Cross Signal Importance')
wtcrosssignalup = wt1 > wt2 and wt1[1] < wt2[1] and wt2 < -10 ? wtcrosssignalimportance : 0
wtcrosssignalupstatus = wtcrosssignalup ? 'WaveTrend Crossed Signal Up' : na
wtcrosssignaldown = wt1 < wt2 and wt1[1] > wt2[1] and wt2 > 10 ? wtcrosssignalimportance : 0
wtcrosssignaldownstatus = wtcrosssignaldown ? 'WaveTrend Crossed Signal Down' : na

//Stochastic Signals
sdivimportance = input(defval=2, minval=0, maxval=100, title='Stochastic Divergence Importance')
sdivup = bullCond14 or bullCond14[1] or bullCond14[2] ? sdivimportance : 0
sdivupstatus = sdivup ? 'Bullish Stoch Divergence' : na
sdivdown = bearCond14 or bearCond14[1] or bearCond14[2] ? sdivimportance : 0
sdivdownstatus = sdivdown ? 'Bearish Stoch Divergence' : na

scrosssignalimportance = input(defval=0, minval=0, maxval=100, title='Stoch Cross Signal Importance')
scrosssignalup = k14 > d14 and k14[1] < d14[1] ? scrosssignalimportance : 0
scrosssignalupstatus = scrosssignalup ? 'Stoch Crossed Signal Up' : na
scrosssignaldown = k14 < d14 and k14[1] > d14[1] ? scrosssignalimportance : 0
scrosssignaldownstatus = scrosssignaldown ? 'Stoch Crossed Signal Down' : na


//Volatility Indicators/////////////////////////////////////////////////////////

//Bollinger Bands Signals
bbcontimportance = input(defval=5, minval=0, maxval=100, title='BollingerBands Contact Importance')
bbcontup = close < lower ? bbcontimportance : 0
bbcontupstatus = bbcontup ? 'Price Contacted Lower BB' : na
bbcontdown = open > upper ? bbcontimportance : 0
bbcontdownstatus = bbcontdown ? 'Price Contacted Upper BB' : na

//Average True Range Signals
atrrevimportance = input(defval=2, minval=0, maxval=100, title='ATR Reversal Importance')
atrrevup = buySignal ? atrrevimportance : 0
atrrevupstatus = atrrevup ? 'ATR Reversed Up' : na
atrrevdown = sellSignal ? atrrevimportance : 0
atrrevdownstatus = atrrevdown ? 'ATR Reversed Down' : na

//Relative Volatility Index Signals
rviposimportance = input(defval=0, minval=0, maxval=100, title='RVI Position Importance')
rviposup = rvi > 25 and rvi[1] < 40 ? rviposimportance : 0
rviposupstatus = rviposup ? 'RVI Volatility Increasing' : na
rviposdown = rvi < 75 and rvi[1] > 60 ? rviposimportance : 0
rviposdownstatus = rviposdown ? 'RVI Volatility Decreasing' : na

rvidivimportance = input(defval=2, minval=0, maxval=100, title='RVI Divergence Importance')
rvidivup = bullCond15 or bullCond15[1] or bullCond15[2] ? rvidivimportance : 0
rvidivupstatus = rvidivup ? 'Bullish RVI Divergence' : na
rvidivdown = bearCond15 or bearCond15[1] or bearCond15[2] ? rvidivimportance : 0
rvidivdownstatus = rvidivdown ? 'Bearish RVI Divergence' : na

//Support and Resistance Signals
srcrossimportance = input(defval=0, minval=0, maxval=100, title='Support/Resistance Cross Importance')
srcrossup = buy1 or buy2 or buy3 or buy4 or buy5 or buy6 or buy7 or buy8 ? srcrossimportance : 0
srcrossupstatus = srcrossup ? 'Crossed Key Level Up' : na
srcrossdown = sell1 or sell2 or sell3 or sell4 or sell5 or sell6 or sell7 or sell8 ? srcrossimportance : 0
srcrossdownstatus = srcrossdown ? 'Crossed Key Level Down' : na

//Volume Indicator Signals//////////////////////////////////////////////////////

//On Balance Volume Divergence Signals
obvdivimportance = input(defval=7, minval=0, maxval=100, title='OBV Divergence Importance')
obvdivup = bullCond18 or bullCond18[1] or bullCond18[2] ? obvdivimportance : 0
obvdivupstatus = obvdivup ? 'Bullish OBV Divergence' : na
obvdivdown = bearCond18 or bearCond18[1] or bearCond18[2] ? obvdivimportance : 0
obvdivdownstatus = obvdivdown ? 'Bearish OBV Divergence' : na

//Chaikin Money Flow Signals
cmfcrossimportance = input(defval=2, minval=0, maxval=100, title='CMF Cross 50-Line Importance')
cmfcrossup = cmf > 0 and cmf[1] < 0 ? cmfcrossimportance : 0
cmfcrossupstatus = cmfcrossup ? 'CMF Crossed 50-Line Up' : na
cmfcrossdown = cmf < 0 and cmf[1] > 0 ? cmfcrossimportance : 0
cmfcrossdownstatus = cmfcrossdown ? 'CMF Crossed 50-Line Down' : na

cmflevimportance = input(defval=0, minval=0, maxval=100, title='CMF Level Importance')
cmflevup = cmf > 0 ? cmflevimportance : 0
cmflevupstatus = cmflevup ? 'CMF Level Up' : na
cmflevdown = cmf < 0 ? cmflevimportance : 0
cmflevdownstatus = cmflevdown ? 'CMF Level Down' : na

//VWAP Signals
vwapcrossimportance = input(defval=2, minval=0, maxval=100, title='VWAP Cross HMA Importance')
vwapcrossup = hma < vwapValue and hma[1] > vwapValue[1] ? vwapcrossimportance : 0
vwapcrossupstatus = vwapcrossup ? 'VWAP Crossed Above HMA' : na
vwapcrossdown = hma > vwapValue and hma[1] < vwapValue[1] ? vwapcrossimportance : 0
vwapcrossdownstatus = vwapcrossdown ? 'VWAP Crossed Below HMA' : na

vwaptrendimportance = input(defval=0, minval=0, maxval=100, title='VWAP Trend Importance')
vwaptrendup = out2 > vwapValue ? vwaptrendimportance : 0
vwaptrendupstatus = vwaptrendup ? 'VWAP Up Trend' : na
vwaptrenddown = out2 < vwapValue ? vwaptrendimportance : 0
vwaptrenddownstatus = vwaptrenddown ? 'VWAP Down Trend' : na

//Candle Patterns Signals
engulfingcandleimportance = input(defval=3, minval=0, maxval=100, title='Engulfing Candle Importance')
bulleng = C_EngulfingBullish ? engulfingcandleimportance : 0
bullengstatus = bulleng ? 'Bullish Engulfing Candle' : na
beareng = C_EngulfingBearish ? engulfingcandleimportance : 0
bearengstatus = beareng ? 'Bearish Engulfing Candle' : na



//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//COLLECT SIGNALS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Classify Entries
stronglongentrysignal  = emadirectionup   + emapushup   + supertrendup   + supertrendrevup   + psardirup   + psarrevup   + hmacloseposup   + hmapivotup   + rsidivup   + rsioversold   + rsicrossup   + macddivup   + histpivotup   + macdcrosssignalup   + wtdivup   + wtcrosssignalup   + sdivup   + scrosssignalup   + bbcontup   + atrrevup   + rviposup   + rvidivup   + srcrossup   + obvdivup   + cmfcrossup   + cmflevup   + vwapcrossup   + vwaptrendup   + bulleng >= stronglongscore
strongshortentrysignal = emadirectiondown + emapulldown + supertrenddown + supertrendrevdown + psardirdown + psarrevdown + hmacloseposdown + hmapivotdown + rsidivdown + rsioverbought + rsicrossdown + macddivdown + histpivotdown + macdcrosssignaldown + wtdivdown + wtcrosssignaldown + sdivdown + scrosssignaldown + bbcontdown + atrrevdown + rviposdown + rvidivdown + srcrossdown + obvdivdown + cmfcrossdown + cmflevdown + vwapcrossdown + vwaptrenddown + beareng >= strongshortscore
weaklongentrysignal    = emadirectionup   + emapushup   + supertrendup   + supertrendrevup   + psardirup   + psarrevup   + hmacloseposup   + hmapivotup   + rsidivup   + rsioversold   + rsicrossup   + macddivup   + histpivotup   + macdcrosssignalup   + wtdivup   + wtcrosssignalup   + sdivup   + scrosssignalup   + bbcontup   + atrrevup   + rviposup   + rvidivup   + srcrossup   + obvdivup   + cmfcrossup   + cmflevup   + vwapcrossup   + vwaptrendup   + bulleng >= weaklongscore
weakshortentrysignal   = emadirectiondown + emapulldown + supertrenddown + supertrendrevdown + psardirdown + psarrevdown + hmacloseposdown + hmapivotdown + rsidivdown + rsioverbought + rsicrossdown + macddivdown + histpivotdown + macdcrosssignaldown + wtdivdown + wtcrosssignaldown + sdivdown + scrosssignaldown + bbcontdown + atrrevdown + rviposdown + rvidivdown + srcrossdown + obvdivdown + cmfcrossdown + cmflevdown + vwapcrossdown + vwaptrenddown + beareng >= weakshortscore

//Alternate Entry Signals
var pos = 0
if stronglongentrysignal and pos <= 0
    pos := 1
if strongshortentrysignal and pos >= 0
    pos := -1
longentry = pos == 1 and (pos != 1)[1]
shortentry = pos == -1 and (pos != -1)[1]
alternatelong  = alternatesignals ? longentry  : stronglongentrysignal
alternateshort = alternatesignals ? shortentry : strongshortentrysignal

//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//PLOT SIGNALS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

plotshape(tradetrendoption ? alternatelong and mabuy : alternatelong, title="Strong Long Label", style=shape.labelup, location=location.belowbar, color=#00bcd4, text="𝐋𝐎𝐍𝐆", textcolor=color.white, size=size.small)
plotshape(tradetrendoption ? alternateshort and masell : alternateshort, title="Strong Short Label", style=shape.labeldown, location=location.abovebar, color=#e91e63, text="𝐒𝐇𝐎𝐑𝐓", textcolor=color.white, size=size.small)
plotshape(weaklongentrysignal, title="Weak Long Triangle", style=shape.triangleup, location=location.belowbar, color=color.new(#00bcd4, 50), size=size.tiny)
plotshape(weakshortentrysignal, title="Weak Short Triangle", style=shape.triangledown, location=location.abovebar, color=color.new(#e91e63, 50), size=size.tiny)


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//PLOT STATUS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

var table statuswindow = table.new(position.top_right, 100, 100, border_width=2)

//Trend Status//////////////////////////////////////////////////////////////////

txt1 = "🡇            TREND             🡇"
table.cell(statuswindow, 3, 0, text=txt1, bgcolor=color.new(#000000, 50), text_color=color.white, text_size=size.small)

//EMA Status
if emadirectionup
    table.cell(statuswindow, 3, 1, text=tostring(emadirectionupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if emadirectiondown
    table.cell(statuswindow, 3, 1, text=tostring(emadirectiondownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if emapushup ? 1 : na
    table.cell(statuswindow, 3, 2, text=tostring(emapushupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if emapushup ? na : 1
    table.clear(statuswindow, 3, 2)
if emapulldown ? 1 : na
    table.cell(statuswindow, 3, 3, text=tostring(emapulldownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if emapulldown ? na : 1
    table.clear(statuswindow, 3, 3)

//SuperTrend Status
if supertrendup
    table.cell(statuswindow, 3, 4, text=tostring(supertrendupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if supertrenddown
    table.cell(statuswindow, 3, 4, text=tostring(supertrenddownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if supertrendrevup ? 1 : na
    table.cell(statuswindow, 3, 5, text=tostring(supertrendrevupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if supertrendrevup ? na : 1
    table.clear(statuswindow, 3, 5)
if supertrendrevdown ? 1 : na
    table.cell(statuswindow, 3, 6, text=tostring(supertrendrevdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if supertrendrevdown ? na : 1
    table.clear(statuswindow, 3, 6)
    
//Parabolic SAR Status
if psardirup
    table.cell(statuswindow, 3, 7, text=tostring(psardirupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if psardirdown
    table.cell(statuswindow, 3, 7, text=tostring(psardirdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if psarrevup ? 1 : na
    table.cell(statuswindow, 3, 8, text=tostring(psarrevupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if psarrevup ? na : 1
    table.clear(statuswindow, 3, 8)
if psarrevdown ? 1 : na
    table.cell(statuswindow, 3, 9, text=tostring(psarrevdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if psarrevdown ? na : 1
    table.clear(statuswindow, 3, 9)

//HMA Status
if hmacloseposup
    table.cell(statuswindow, 3, 10, text=tostring(hmacloseposupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if hmacloseposdown
    table.cell(statuswindow, 3, 10, text=tostring(hmacloseposdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if hmapivotup ? 1 : na
    table.cell(statuswindow, 3, 11, text=tostring(hmapivotupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if hmapivotup ? na : 1
    table.clear(statuswindow, 3, 11)
if hmapivotdown ? 1 : na
    table.cell(statuswindow, 3, 12, text=tostring(hmapivotdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if hmapivotdown ? na : 1
    table.clear(statuswindow, 3, 12)

//Momentum Status///////////////////////////////////////////////////////////////

txt2 = "🡇         MOMENTUM         🡇"
table.cell(statuswindow, 2, 0, text=txt2, bgcolor=color.new(#000000, 50), text_color=color.white, text_size=size.small)
    
//RSI Status
if rsidivup ? 1 : na
    table.cell(statuswindow, 2, 1, text=tostring(rsidivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if rsidivup ? na : 1
    table.clear(statuswindow, 2, 1)
if rsidivdown ? 1 : na
    table.cell(statuswindow, 2, 2, text=tostring(rsidivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if rsidivdown ? na : 1
    table.clear(statuswindow, 2, 2)
if rsioversold ? 1 : na
    table.cell(statuswindow, 2, 3, text=tostring(rsioversoldstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if rsioversold ? na : 1
    table.clear(statuswindow, 2, 3)
if rsioverbought ? 1 : na
    table.cell(statuswindow, 2, 4, text=tostring(rsioverboughtstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if rsioverbought ? na : 1
    table.clear(statuswindow, 2, 4)
if rsicrossup ? 1 : na
    table.cell(statuswindow, 2, 5, text=tostring(rsicrossupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if rsicrossup ? na : 1
    table.clear(statuswindow, 2, 5)
if rsicrossdown ? 1 : na
    table.cell(statuswindow, 2, 6, text=tostring(rsicrossdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if rsicrossdown ? na : 1
    table.clear(statuswindow, 2, 6)

//MACD Status
if macddivup ? 1 : na
    table.cell(statuswindow, 2, 7, text=tostring(macddivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if macddivup ? na : 1
    table.clear(statuswindow, 2, 7)
if macddivdown ? 1 : na
    table.cell(statuswindow, 2, 8, text=tostring(macddivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if macddivdown ? na : 1
    table.clear(statuswindow, 2, 8)
if histpivotup ? 1 : na
    table.cell(statuswindow, 2, 9, text=tostring(histpivotupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if histpivotup ? na : 1
    table.clear(statuswindow, 2, 9)
if histpivotdown ? 1 : na
    table.cell(statuswindow, 2, 10, text=tostring(histpivotdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if histpivotdown ? na : 1
    table.clear(statuswindow, 2, 10)
if macdcrosssignalup ? 1 : na
    table.cell(statuswindow, 2, 11, text=tostring(macdcrosssignalupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if macdcrosssignalup ? na : 1
    table.clear(statuswindow, 2, 11)
if macdcrosssignaldown ? 1 : na
    table.cell(statuswindow, 2, 12, text=tostring(macdcrosssignaldownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if macdcrosssignaldown ? na : 1
    table.clear(statuswindow, 2, 12)

//Wave Trend Status
if wtdivup ? 1 : na
    table.cell(statuswindow, 2, 13, text=tostring(wtdivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if wtdivup ? na : 1
    table.clear(statuswindow, 2, 13)
if wtdivdown ? 1 : na
    table.cell(statuswindow, 2, 14, text=tostring(wtdivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if wtdivdown ? na : 1
    table.clear(statuswindow, 2, 14)
if wtcrosssignalup ? 1 : na
    table.cell(statuswindow, 2, 15, text=tostring(wtcrosssignalupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if wtcrosssignalup ? na : 1
    table.clear(statuswindow, 2, 15)
if wtcrosssignaldown ? 1 : na
    table.cell(statuswindow, 2, 16, text=tostring(wtcrosssignaldownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if wtcrosssignaldown ? na : 1
    table.clear(statuswindow, 2, 16)
    
//Stochastic Status
if sdivup ? 1 : na
    table.cell(statuswindow, 2, 17, text=tostring(sdivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if sdivup ? na : 1
    table.clear(statuswindow, 2, 17)
if sdivdown ? 1 : na
    table.cell(statuswindow, 2, 18, text=tostring(sdivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if sdivdown ? na : 1
    table.clear(statuswindow, 2, 18)
if scrosssignalup ? 1 : na
    table.cell(statuswindow, 2, 19, text=tostring(scrosssignalupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if scrosssignalup ? na : 1
    table.clear(statuswindow, 2, 19)
if scrosssignaldown ? 1 : na
    table.cell(statuswindow, 2, 20, text=tostring(scrosssignaldownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if scrosssignaldown ? na : 1
    table.clear(statuswindow, 2, 20)

    
//Volatility Status/////////////////////////////////////////////////////////////////

txt3 = "🡇         VOLATILITY         🡇"
table.cell(statuswindow, 1, 0, text=txt3, bgcolor=color.new(#000000, 50), text_color=color.white, text_size=size.small)

//Bollinger Bands Status
if bbcontup ? 1 : na
    table.cell(statuswindow, 1, 1, text=tostring(bbcontupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if bbcontup ? na : 1
    table.clear(statuswindow, 1, 1)
if bbcontup ? 1 : na
    table.cell(statuswindow, 1, 2, text=tostring(bbcontdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if bbcontdown ? na : 1
    table.clear(statuswindow, 1, 2)
    
//ATR Status
if atrrevup ? 1 : na
    table.cell(statuswindow, 1, 3, text=tostring(atrrevupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if atrrevup ? na : 1
    table.clear(statuswindow, 1, 3)
if atrrevdown ? 1 : na
    table.cell(statuswindow, 1, 4, text=tostring(atrrevdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if atrrevdown ? na : 1
    table.clear(statuswindow, 1, 4)
    
//RVI Status
if rviposup ? 1 : na
    table.cell(statuswindow, 1, 5, text=tostring(rviposupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if rviposup ? na : 1
    table.clear(statuswindow, 1, 5)
if rviposdown ? 1 : na
    table.cell(statuswindow, 1, 6, text=tostring(rviposdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if rviposdown ? na : 1
    table.clear(statuswindow, 1, 6)
if rvidivup ? 1 : na
    table.cell(statuswindow, 1, 7, text=tostring(rvidivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if rvidivup ? na : 1
    table.clear(statuswindow, 1, 7)
if rvidivdown ? 1 : na
    table.cell(statuswindow, 1, 8, text=tostring(rvidivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if rvidivdown ? na : 1
    table.clear(statuswindow, 1, 8)

//Support and Resistance Status
if srcrossup ? 1 : na
    table.cell(statuswindow, 1, 9, text=tostring(srcrossupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if srcrossup ? na : 1
    table.clear(statuswindow, 1, 9)
if srcrossdown ? 1 : na
    table.cell(statuswindow, 1, 10, text=tostring(srcrossdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if srcrossdown ? na : 1
    table.clear(statuswindow, 1, 10)
    
    
//Volume Status/////////////////////////////////////////////////////////////////

txt4 = "🡇           VOLUME           🡇"
table.cell(statuswindow, 0, 0, text=txt4, bgcolor=color.new(#000000, 50), text_color=color.white, text_size=size.small)

//On Balance Volume Status
if obvdivup ? 1 : na
    table.cell(statuswindow, 0, 1, text=tostring(obvdivupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if obvdivup ? na : 1
    table.clear(statuswindow, 0, 1)
if obvdivdown ? 1 : na
    table.cell(statuswindow, 0, 2, text=tostring(obvdivdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if obvdivdown ? na : 1
    table.clear(statuswindow, 0, 2)
    
//Chaikin Money Flow Status
if cmfcrossup ? 1 : na
    table.cell(statuswindow, 0, 3, text=tostring(cmfcrossupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if cmfcrossup ? na : 1
    table.clear(statuswindow, 0, 3)
if cmfcrossdown ? 1 : na
    table.cell(statuswindow, 0, 4, text=tostring(cmfcrossdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if cmfcrossdown ? na : 1
    table.clear(statuswindow, 0, 4)
if cmflevup ? 1 : na
    table.cell(statuswindow, 0,5, text=tostring(cmflevupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if cmflevdown ? 1 : na
    table.cell(statuswindow, 0, 5, text=tostring(cmflevdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
    
//VWAP Status
if vwapcrossup ? 1 : na
    table.cell(statuswindow, 0, 6, text=tostring(vwapcrossupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if vwapcrossup ? na : 1
    table.clear(statuswindow, 0, 6)
if vwapcrossdown ? 1 : na
    table.cell(statuswindow, 0, 7, text=tostring(vwapcrossdownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if vwapcrossdown ? na : 1
    table.clear(statuswindow, 0, 7)
if vwaptrendup ? 1 : na
    table.cell(statuswindow, 0,8, text=tostring(vwaptrendupstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if vwaptrenddown ? 1 : na
    table.cell(statuswindow, 0, 8, text=tostring(vwaptrenddownstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
    
//Candle Pattern Status
if bulleng ? 1 : na
    table.cell(statuswindow, 0, 9, text=tostring(bullengstatus), bgcolor=color.new(#00bcd4, 50), text_color=color.white, text_size=size.small)
if bulleng ? na : 1
    table.clear(statuswindow, 0, 9)
if beareng ? 1 : na
    table.cell(statuswindow, 0, 10, text=tostring(bearengstatus), bgcolor=color.new(#e91e63, 50), text_color=color.white, text_size=size.small)
if beareng ? na : 1
    table.clear(statuswindow, 0, 10)


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
//STOP LOSS WARNINGS▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

//Stop Loss Criteria
longstoploss = strategy.position_avg_price * (1 + stoplosspercent)
shortstoploss = strategy.position_avg_price * (1 - stoplosspercent)
printstoplong = longstoploss > close and longstoploss[1] < close[1] and strategy.position_size > 0
printstopshort = shortstoploss < close and shortstoploss[1] > close[1] and strategy.position_size < 0

//Stop Loss Lines
plot(strategy.position_size > 0 ? longstoploss : na, style=plot.style_line, color=color.new(color.yellow, 50), linewidth=1, title="Stop Long Line", display=display.none)
plot(strategy.position_size < 0 ? shortstoploss : na, style=plot.style_line, color=color.new(color.yellow, 50), linewidth=1, title="Stop Short Line", display=display.none)

//Stop Loss Labels
plotshape(printstoplong, title="Stop Long Label", style=shape.labelup, location=location.belowbar, color=color.yellow, text="𝐒𝐓𝐎𝐏", textcolor=color.black, size=size.tiny)
plotshape(printstopshort, title="Stop Short Label", style=shape.labeldown, location=location.abovebar, color=color.yellow, text="𝐒𝐓𝐎𝐏", textcolor=color.black, size=size.tiny)


//END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
////////////////////////////////////////////////////////////////////////////////
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
