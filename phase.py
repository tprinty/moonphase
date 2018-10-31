#!/usr/bin/env python
"""

Modified code so that I could pass in a Month Day and Year on the command line.


This is modified code from.  
	moonphase.py - Calculate Lunar Phase
	Author: Sean B. Palmer, inamidst.com
	Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import math, decimal, datetime, sys, getopt
dec = decimal.Decimal

def position(month, day, year): 

   diff = datetime.datetime(year, month, day) - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = dec("0.20439731") + (days * dec("0.03386319269"))

   return lunations % dec(1)

def phase(pos): 
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "New Moon", 
      1: "Waxing Crescent", 
      2: "First Quarter", 
      3: "Waxing Gibbous", 
      4: "Full Moon", 
      5: "Waning Gibbous", 
      6: "Last Quarter", 
      7: "Waning Crescent"
   }[int(index) & 7]

def main(argv): 
   month = 0 
   day = 0
   year = 0

   try:
      opts, args = getopt.getopt(argv,"hm:d:y:",["month=","day=","year="])
   except getopt.GetoptError:
      print 'phase.py -m <month> -d <day> -y <year>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'phase.py -m <month> -d <day> -y <year>'
         sys.exit()
      elif opt in ("-m", "--month"):
         month = arg
      elif opt in ("-d", "--day"):
         day = arg
      elif opt in ("-y", "--year"):
         year = arg


   pos = position(int(month), int(day), int(year))
   phasename = phase(pos)

   roundedpos = round(float(pos), 3)
   print "%s (%s)" % (phasename, roundedpos)

if __name__=="__main__": 
	main(sys.argv[1:])
