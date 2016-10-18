import numpy
import csv

def get_mlb_data_from_csv(): 
  stat_dictionary = {}
  with open('baseballDatabank/Batting.csv','r') as f:
    skipFirstLine = True
    reader = csv.reader(f)
    for row in reader:
      line2 = []
      if skipFirstLine:
        skipFirstLine = False
        continue
      try:
        for i, x in enumerate(row):
          if len(x.strip())< 1:
            x = row[i] = '-999'
          line2.append(str(x))
        playerID, year, stint, teamID, lgID, g, ab, r, h, x2b, x3b, hr, rbi, sb, cs, bb, so, ibb, hbp, sh, sf, gidp = line2
      except:
        print "Bad Line, Skipping!\n"
        continue
      playerID = playerID.lower()
      year = int(year)
      stint = int(stint)
      teamID = teamID.lower()
      lgID = lgID.lower()
      g = int(g)
      ab = int(ab)
      r = int(r)
      h = int(h)
      x2b = int(x2b)
      x3b = int(x3b)
      hr = int(hr)
      rbi = int(rbi)
      sb = int(sb)
      cs = int(cs)
      bb = int(bb)
      so = int(so)
      ibb = int(ibb)
      hbp = int(hbp)
      sh = int(sh)
      sf = int(sf)
      gidp = int(gidp)

      if playerID not in stat_dictionary:
        stat_dictionary[playerID]={}
      stat_dictionary[playerID][year] = {
          "stint": stint,
          "teamID": teamID,
          "lgID": lgID,
          "G": g,
          "AB": ab,
          "R": r,
          "H": h,
          "X2B": x2b,
          "X3B": x3b,
          "HR": hr,
          "RBI": rbi,
          "SB": sb,
          "CS": cs,
          "BB": bb,
          "SO": so,
          "IBB": ibb,
          "HBP": hbp,
          "SH": sh,
          "SF": sf,
          "GIDP": gidp,
          "PA": ab+bb+hbp,
      }
  return stat_dictionary

if __name__ == "__main__":
  stat_dictionary = get_mlb_data_from_csv()
  for player in stat_dictionary:
    for year in stat_dictionary[player]:
      if year == 2009 and stat_dictionary[player][year]["teamID"] == "cin":
        print player
        print stat_dictionary[player][year]
        print
          
