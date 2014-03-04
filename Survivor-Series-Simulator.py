##############################################################


###
# WRESTLER DETAILS
# Contains - 
# 1. List of wrestlers
# 2. Wrestler rating
# 3. Wrestler finisher set
# 4. Ratings of the finishers
# 5. Ratings for the non-finisher moves
###

# Complete list of wrestlers
# Given as :
# Wrestler's name, Rating, Finishers

wrestlers = {
			1:["CM Punk",10.0,["GTS", "Anaconda Vice"], "Punk"], 
			2:["Daniel Bryan",10.0,["YES! Lock", "Running Knee"], "Bryan"], 
			3:["Chris Jericho",9.7,["Liontamer", "CodeBreaker"], "Jericho"], 
			4:["Dean Ambrose",9.5,["Headlock Driver"], "Ambrose"], 
			5:["Seth Rollins",9.2,["Blackout"], "Rollins"], 
			6:["Roman Reigns",9.3,["Spear"], "Reigns"],
			7:["John Cena",9.8,["Attitude Adjustment", "STF"], "Cena"], 
			8:["Randy Orton",9.6,["RKO", "Punt Kick"], "Orton"], 
			9:["Big Show",9.3,["WMD", "Choke Slam"], "Big Show"],
			10:["Dolph Ziggler",9.1,["Zig Zag", "FameAsser"], "Ziggler"], 
			11:["Rob Van Dam",9.0,["Five Star Frog Splash"], "RVD"], 
			12:["Kane",9.3,["Choke Slam"], "Kane"],
			13:["Cody Rhodes",8.9,["Cross Rhodes"], "Rhodes"], 
			14:["Goldust",8.5,["Curtain Call", "Final Cut"], "Goldust"], 
			15:["Alberto Del Rio",8.7,["Cross Armbreaker"], "Del Rio"],
			16:["Bray Wyatt",8.7,["Sister Abigail"], "Wyatt"], 
			17:["Erik Rowan",8.1,["Running Splash"], "Rowan"], 
			18:["Luke Harper",8.3,["Truckstop"], "Harper"],
			19:["Jack Swagger",8.2,["Ankle Lock", "Gutwrench Powerbomb"], "Swagger"], 
			20:["Antonio Cesaro",9.0,["Neutralizer", "Giant Swing"], "Cesaro"], 
			21:["Damien Sandow",8.4,["You're Welcome", "Terminus"], "Sandow"],
			22:["Jimmy Uso",8.1,["Superkick", "Samoan Drop"], "Uso"], 
			23:["Jey Uso",8.1,["Superkick", "Samoan Drop"], "Uso"], 
			24:["Big E Langston",8.9,["Big Ending"], "Big E"],
			25:["Rey Mysterio",8.8,["619"], "Mysterio"], 
			26:["Kofi Kingston",8.5,["Trouble In Paradise"], "Kofi"], 
			27:["Ryback",9.2,["ShellShocked"], "Ryback"],
			28:["The Miz",7.8,["Skull Crushing Finale"], "Miz"], 
			29:["Sheamus",9.1,["Brogue Kick", "High Cross"], "Sheamus"], 
			30:["Mark Henry",9.0,["World's Strongest Slam"], "Mark Henry"],
			31:["Curtis Axel",7.7,["Perfectplex"], "Axel"], 
			32:["Wade Barrett",7.6,["BullHammer"], "Barrett"], 
			33:["Fandango",7.4,["Beauty In Motion"], "Fandango"],
			34:["Heath Slater",7.1,["Smash Hit"], "Slater"], 
			35:["Drew McIntyre",7.3,["Double Underhook DDT"], "McIntyre"], 
			36:["Jinder Mahal",7.0,["Karachi Valley Driver"], "Jinder"],
			37:["The Great Khali",7.9,["Punjabi Plunge"], "Khali"], 
			38:["Brodus Clay",7.4,["Splat!"], "Brodus Clay"], 
			39:["Tensai",7.6,["Baldo Bomb"], "Tensai"],
			40:["Bo Dallas",6.8,["Bo Dallas Spear"], "Bo Dallas"], 
			41:["Santino Marella",7.0,["Cobra"], "Santino"], 
			42:["Zack Ryder",6.9,["Rough Ryder"], "Ryder"],
			43:["David Otunga",6.8,["Verdict"], "Otunga"], 
			44:["Justin Gabriel",6.9,["450 Splash"], "Justin Gabriel"], 
			45:["Sin Cara",7.0,["Moonsault Side Slam"], "Sin Cara"],
			46:["R-Truth",7.4,["Lie Detector"], "Truth"], 
			47:["John Morrison",7.7,["Starship Pain"], "Morrison"], 
			48:["Primo",6.8,["Backstabber"], "Primo"],
			49:["Epico",6.7,["Backstabber"], "Epico"], 
			50:["Evan Bourne",6.8,["Shooting Star Press"], "Bourne"], 
			51:["AJ Styles",9.6,["Styles Clash", "Calf Slicer"], "Styles"], 
			52:["Bully Ray",9.5,["Bully Bomb"], "Bully"], 
			53:["Jeff Hardy",9.4,["Swanton Bomb", "Twist Of Fate"], "Hardy"],
			54:["Mr.Anderson",8.8,["Mic Check"], "Anderson"], 
			55:["Austin Aries",9.4,["Brainbuster"], "Aries"], 
			56:["Bobby Roode",9.3,["Crossface", "Pay Off"], "Roode"],
			57:["Christopher Daniels",9.1,["Best Moonsault Ever"], "Daniels"], 
			58:["Kazarian",9.1,["Fade To Black"], "Kaz"], 
			59:["James Storm",9.0,["Last Call Superkick"], "Storm"],
			60:["Magnus",8.8,["Mag Daddy Driver"], "Magnus"], 
			61:["Kurt Angle",9.2,["Angle Slam", "Ankle Lock"], "Angle"], 
			62:["Samoa Joe",9.3,["Musclebuster"], "Joe"],
			63:["Rob Terry",8.4,["Freakbuster"], "Rob T"], 
			64:["Abyss",8.9,["Black Hole Slam"], "Abyss"], 
			65:["Robbie E",7.4,["Spinning Lifting DDT"], "Robbie E"],
			66:["Alex Shelley",8.6,["Sliced Bread #2"], "Shelley"], 
			67:["Chris Sabin",9.1,["All Hail Sabin"], "Sabin"], 
			68:["Manik",7.9,["Double Chickenwing Gutbuster"], "Manik"],
			69:["Sting",8.9,["Scorpion Death Drop", "Scorpion Death Lock"], "Sting"], 
			70:["Devon",8.4,["Thrust Spinebuster"], "Devon"], 
			71:["DOC",7.7,["One Percenter"], "DOC"],
			72:["Kenny King",7.6,["Royal Flush"], "King"], 
			73:["Chavo Guerrero",7.6,["Frog Splash"], "Chavo"], 
			74:["Hernandez",7.9,["Border Toss"], "Hernandez"],
			75:["Chuck Taylor",8.7,["Awful Waffle"], "Taylor"], 
			76:["Johnny Gargano",8.4,["Garga-No Escape"], "Gargano"], 
			77:["Ricochet",8.5,["Double Rotation Moonsault"], "Ricochet"], 
			78:["Kevin Steen",8.8,["F-Cinq"], "Steen"], 
			79:["El Generico",8.9,["BRAINBUSTAAHHH!!"], "El Generico"], 
			80:["Colt Cabana",8.7,["Billy Goat's Curse", "Chicago Skyline"], "Cabana"], 
			81:["Chris Hero",8.7,["Hero's Welcome"], "Hero"], 
			82:["Matt Jackson",8.5,["Worst Case Scenario"], "Jackson"], 
			83:["Nick Jackson",8.5,["450 Splash"], "Jackson"], 
			84:["PAC",8.6,["Corkscrew 450 Splash"], "PAC"], 
			85:["Jigsaw",8.0,["Jig 'n Tonic", "Cancun Tornado"], "Jigsaw"], 
			86:["Lince Dorado",7.9,["Chikara Special", "Lynxsault"], "Lince Dorado"], 
			87:["Dragon Kid",8.2,["Dragonrana", "Ultra Hurricanrana"], "Dragon Kid"], 
			88:["Arik Cannon",7.8,["Total Anarchy"], "Cannon"], 
			89:["Brian Kendrick",7.7,["Sliced Bread"], "Kendrick"], 
			90:["Icarus",7.8,["Wings Of Icarus"], "Icarus"], 
			91:["Mike Quackenbush",7.5,["QuackenDriver", "Chikara Special"], "Quackenbush"], 
			92:["Fire ANT",7.9,["Beach Break", "Burning Hammer"], "Fire ANT"], 
			93:["AssailANT",7.9,["AssailANT's Cross", "GTS - Get The Sugar"], "AssailANT"], 
			94:["Matt Hardy",7.9,["Twist Of Fate"], "Hardy"], 
			95:["Zema Ion",7.6,["Submission Impossible"], "Zema Ion"],
			96:["Stone Cold Steve Austin",10.0,["Stunner"], "Austin"], 
			97:["The Rock",10.0,["Rock Bottom", "People's Elbow"], "Rock"], 
			98:["The Undertaker",10.0,["Tombstone", "Choke Slam", "Last Ride", "Hell's Gate"], "Taker"],
			99:["Shawn Michaels",10.0,["Sweet Chin Music"], "Michaels"], 
			100:["Edge",10.0,["Spear"], "Edge"], 
			101:["Christian",8.9,["Killswitch"], "Christian"],
			102:["Mick Foley",9.1,["Mandible Claw", "Bionic Elbow"], "Foley"], 
			103:["Eddie Guerrero",9.4,["Frog Splash"], "Guerrero"], 
			104:["Chris Benoit",9.3,["Crippler Crossface"], "Benoit"],
			105:["Hulk Hogan",9.0,["Hogan Leg Drop"], "Hogan"], 
			106:["Kevin Nash",8.5,["Jackknife Powerbomb"], "Nash"], 
			107:["Razor Ramon",8.8,["Razor's Edge"], "Ramon"],
			108:["Goldberg",9.3,["Spear", "Jackhammer"], "Goldberg"], 
			109:["Brock Lesnar",9.5,["F5", "Kimura Lock"], "Lesnar"], 
			110:["Triple H",9.3,["Pedigree"], "Triple H"],
			111:["Shane McMahon",8.6,["Elbow Drop", "Coast to Coast"], "Shane O'Mac"], 
			112:["Vince McMahon",8.2,["Pedigree", "People's Elbow", "Stunner", "Hogan Leg Drop"], "Mr.McMahon"], 
			113:["JBL",8.8,["Clothesline from Hell"], "JBL"],
			114:["Diamond Dallas Page",8.0,["Diamond Cutter"], "DDP"], 
			115:["Bret Hart",9.0,["Sharpshooter"], "Hitman"], 
			116:["Ric Flair",9.0,["Figure 4 Leg Lock"], "Nature Boy"],
			117:["Booker T",8.8,["Scissor Kick"], "Booker"], 
			118:["Dean Malenko",8.5,["Texas Cloverleaf"], "Malenko"], 
			119:["Roddy Piper",8.4,["Sleeper Hold"], "'Rowdy' Roddy Piper"],
			120:["Umaga",8.3,["Samoan Drop", "Samoan Spike"], "Umaga"], 
			121:["Rikishi",8.3,["Banzai Drop", "StinkFace"], "Rikishi"], 
			122:["Andre The Giant",8.7,["Double Underhook Suplex"], "Andre"],
			123:["Batista",9.2,["Batista Bomb"], "Batista"], 
			124:["Bobby Lashley",9.1,["Dominator", "Spear"], "Lashley"], 
			125:["Farooq",8.1,["Dominator", "Thrust Spinebuster"], "Farooq"]
			}

# The number of wrestlers available is -

wrestler_count = len(wrestlers)

# Gives the ratings for every impact finisher used

impact_ratings = {
#				  '',0, 
				  '450 Splash':8.6, 
				  '619':8.5, 
				  'All Hail Sabin':8.9,
				  'Angle Slam':8.6, 
				  "AssailANT's Cross":8.5,
				  'Attitude Adjustment':9.5,
				  'Awful Waffle':9.1, 
				  'BRAINBUSTAAHHH!!':9.1,
				  'Backstabber':8.4,
				  'Baldo Bomb':8.0, 
				  'Banzai Drop':7.7, 
				  'Batista Bomb':9.0, 
				  'Beach Break':8.6,
				  'Beauty In Motion':8.7,
				  'Best Moonsault Ever':9.0,
				  'Bo Dallas Spear':7.9,
				  'Big Ending':8.9, 
				  'Bionic Elbow':6.4, 
				  'Black Hole Slam':8.3, 
				  'Blackout':8.1, 
				  'Border Toss':7.9,
				  'Brainbuster':9.2, 
				  'Brogue Kick':9.4,
				  'BullHammer':8.6,
				  'Bully Bomb':8.7, 
				  'Burning Hammer':8.7,
				  'Cancun Tornado':8.8,
				  'Chicago Skyline':8.7,
				  'Choke Slam':9.1, 
				  'Clothesline from Hell':8.5, 
				  'Coast to Coast':6.6, 
				  'Cobra':6.7, 
				  'CodeBreaker':8.3, 
				  'Corkscrew 450 Splash':9.1, 
				  'Cross Rhodes':8.5,
				  'Curtain Call':7.8, 
				  'Diamond Cutter':9.1,
				  'Dragonrana':8.8,
				  'Dominator':8.8,
				  'Double Chickenwing Gutbuster':8.5,
				  'Double Rotation Moonsault':9.2, 
				  'Double Underhook DDT':7.6, 
				  'Double Underhook Suplex':8.3,
				  'Elbow Drop':8.4, 
				  'F-Cinq':8.9,
				  'F5':9.4, 
				  'Fade To Black':9.0,
				  'FameAsser':8.1, 
				  'Final Cut':8.6,
				  'Five Star Frog Splash':9.1, 
				  'Freakbuster':8.5,
				  'Frog Splash':9.0, 
				  'GTS':9.6, 
				  'GTS - Get the Sugar':8.7,
				  'Giant Swing':8.8,
				  'Gutwrench Powerbomb':8.1, 
				  'Headlock Driver':8.8,
				  "Hero's Welcome":8.9, 
				  'Hogan Leg Drop':8.2,
				  'High Cross':8.5, 
				  'Jackhammer':9.3,
				  'Jackknife Powerbomb':8.6,
				  "Jig 'n Tonic":8.7,
				  'Karachi Valley Driver':7.8, 
				  'Killswitch':8.4, 
				  'Last Call Superkick':8.8, 
				  'Last Ride':9.2, 
				  'Lie Detector':7.9, 
				  'Lynxsault':8.9,
				  'Mag Daddy Driver':8.7,
				  'Mic Check':8.1, 
				  'Moonsault Side Slam':8.6, 
				  'Musclebuster':9.1,
				  'Neutralizer':9.5,
				  'One Percenter':8.1,
				  'Pay Off':8.8, 
				  'Pedigree':9.3, 
				  "People's Elbow":7.6, 
				  'Perfectplex':8.5,  
				  'Punjabi Plunge':8.5, 
				  'Punt Kick':9.0,
				  'QuackenDriver':8.0, 
				  'RKO':9.7, 
				  "Razor's Edge":8.9,
				  'Rock Bottom':9.0, 
				  'Rough Ryder':7.5,
				  'Royal Flush':7.8, 
				  'Running Knee':9.3,
				  'Running Splash':8.2, 
				  'Samoan Drop':8.2, 
				  'Samoan Spike':8.6, 
				  'Scissor Kick':8.1, 
				  'Scorpion Death Drop':8.5, 
				  'ShellShocked':9.1, 
				  'Shooting Star Press':9.0,
				  'Sister Abigail':9.0, 
				  'Skull Crushing Finale':8.9, 
				  'Sliced Bread':7.8,
				  'Sliced Bread #2':8.2,
				  'Smash Hit':7.7,
				  'Splat':7.9, 
				  'Spear':9.6, 
				  'Spinning Lifting DDT':7.8,
				  'Starship Pain':9.1,  
				  'Stunner':9.8, 
				  'Styles Clash':9.1, 
				  'Superkick':9.0, 
				  'Swanton Bomb':9.1, 
				  'Sweet Chin Music':9.7,
				  'Terminus':8.3,
				  'Thrust Spinebuster':8.1, 
				  'Tombstone':9.9,  
				  'Total Anarchy':8.3,
				  'Trouble In Paradise':8.5,
				  'Truckstop':8.2, 
				  'Twist Of Fate':8.7,
				  'Ultra Hurricanrana':8.2, 
				  'Verdict':7.8,
				  'WMD':9.5, 
				  'Wings Of Icarus':8.5, 
				  "World's Strongest Slam":9.3,
				  'Worst Case Scenario':8.5,
				  "You're Welcome":8.6, 
				  'Zig Zag':9.0
				 }

# Gives the ratings for every submission finishers used

submission_ratings = {
#				  '',0, 
				  'Anaconda Vice':9.5, 
				  'Ankle Lock':9.2, 
				  "Billy Goat's Curse":8.7,
				  'Calf Slicer':8.5,
				  'Chikara Special':9.2, 
				  'Crippler Crossface':9.5, 
				  'Crossface':8.9,
				  'Cross Armbreaker':9.0, 
				  'Figure 4 Leg Lock':8.5, 
				  'Garga-No Escape':8.9,
				  "Hell's Gate":9.8, 
				  'Kimura Lock':9.5, 
				  'Liontamer':9.7, 
				  'Mandible Claw':8.8, 
				  'STF':9.3, 
				  'Scorpion Death Lock':8.8,
				  'Sharpshooter':9.2, 
				  'Sleeper Hold':8.1,
				  'StinkFace':8.3,
				  'Submission Impossible':8.9, 
				  'Texas Cloverleaf':9.1,
				  'YES! Lock':9.5, 
				 }

# Gives the ratings for the basic moves

basic_ratings = {
#				['':0],
				0:['Punch',0.2],
				1:['Backhand Chop',0.5],
				2:['Knife Edge Chop',0.6],
				3:['Forearm',0.3],
				4:['Knee Strike',0.4],
				5:['Knee to the midsection',0.4],
				6:['Kick',0.4],
				7:['Kick to the midsection',0.4],
				8:['Kick to the head',0.7],
				9:['Jab',0.3],
				10:['Tackle',0.4],
				11:['Running takedown',0.4],
				12:["Fireman's carry",0.3],
				13:['Drop Toe Hold',0.3],
				14:['Irish Whip',0.5],
				15:['Big Boot',0.8],
				16:['Dropkick',0.7],
				17:['Enzuigiri',0.7],
				18:['Battering Ram',0.6],
				19:['Headbutt',0.4],
				20:['Hiptoss',0.4],
				21:['Arm Drag',0.4],
				22:['Double Axe Handle',0.4],
				23:['Elbow Strike',0.3],
				24:['Crossbody',0.6],
				25:['Clothesline',0.5],
				26:['Shoulder Block',0.4],
				27:['Back Rake',0.2],
				28:['Uppercut',0.7],
				29:['Slap',0.1],
				30:['Lariat',0.4],
				31:['Snapmare',0.3]
				}

basic_count = len(basic_ratings)  # The number of basic moves

# Gives the ratings for grapple moves

grapple_ratings = {
#				  ['',0],
				  0:['Scoop Slam',0.7],
				  1:['Suplex',0.8],
				  2:['Snap Suplex',0.8],
				  3:['German Suplex',1.2],
				  4:['Northern Lights Suplex',1.1],
				  5:['Belly to Belly Suplex',0.7],
				  6:['Belly to Back Suplex',0.9],
				  7:['DDT',1.0],
				  8:['Inverted DDT',1.1],
				  9:['Tornado DDT',1.4],
				  10:['Bodyslam',0.7],
				  11:['Back Body Drop',0.9],
				  12:['Atomic Drop',1.0],
				  13:['Gutwrench Suplex',1.2],
				  14:['Elevated DDT',1.5],
				  15:['Reverse Suplex',1.4],
				  16:['Falcon Arrow',1.7],
				  17:['Neckbreaker',0.9],
				  18:['Backbreaker',0.9],
				  19:['Thesz Press',0.7],
				  20:['Spinebuster',1.2],
				  21:['Facebuster',0.9],
				  22:['Bulldog',1.0],
				  23:['Jawbreaker',1.0],
				  24:['Sleeper Hold Drop',1.1],
				  25:['Electric Chair Drop',1.3],
				  26:['Leg Sweep',0.7],
				  27:['Monkey Toss',0.8],
				  28:['Powerbomb',1.4],
				  29:['Sidewalk Slam',0.9],
				  30:['Power Slam',1.2]	
				  }

grapple_count = len(grapple_ratings)  # The number of grapple moves

# Gives the ratings for holds and locks

hold_ratings = {
#			   ['',0],
			   0:['Front Facelock',-1.2],
			   1:['Headlock',-1.2],
			   2:['Hammerlock',-1.1],
			   3:['Wristlock',-1.0],
			   4:['Reverse Chinlock',-1.3],
			   5:['Surfboard',1.2],
			   6:['Armbar',1.8],
			   7:['Kneebar',1.9],
			   8:['Sleeper Hold',2.0],
			   9:['Abdominal Stretch',0.8],
			   10:['Full Nelson',-0.8],
			   11:['Half Nelson',-0.4],
			   }

hold_count = len(hold_ratings)  # The number of hold moves

# Gives the ratings for aerial moves

aerial_ratings = {
#				 ['',0],
				 0:['Leg Drop',2.5],
				 1:['Elbow Drop',2.5],
				 2:['Diving Axehandle',2.0],
				 3:['Diving Shoulder Strike',2.0],
				 4:['Flying Crossbody',2.4],
				 5:['Missile Dropkick',2.8],
				 6:['Moonsault',2.9],
				 7:['Diving Clothesline',2.1],
				 8:['Top Rope Hurricanrana',3.2],
				 9:['Diving Headbutt',2.4],
				 10:['Superplex',3.7]
				 }

aerial_count = len(aerial_ratings)  # The number of aerial moves


# Assign the upper limit for the rating total in the team				 			 

maxlimit = 43.5

final_save_location = "Match_commentaries/"


####################################################################

from Tkinter import *
import random
import itertools
from hashlib import md5
import os

####################################


class SurvivorSeriesGame(object):

	"""	This class defines -
		* The team lists
		* The stat maintainers - non-eliminated members, member currently in the ring, power meter
		* The random number based operations :
			> Selecting which particular move of a certain type is being performed
			> Probability of successfully performing the move
			> Updating the power meters after the move
			> Who should start the match
			> Who to tag in when a tag is made 
			> Who should continue the match after an elimination
		* Functions to perform each type of move
			> The subclass has a move_perform() method that uses getattr() to select which function to use
			> Possible functions :
				# do_matchstart()
				# do_basic()
				# do_grapple()
				# do_hold()
				# do_aerial()
				# do_finisher()
				# do_tag()
				# do_elimination()
		* Functions to retrieve move lists

	"""
	teams = []
	match_teams = [[],[]]
	in_control = 0
	currently_1 = 0
	currently_2 = 0
	commentary_text = ""
	move_list = {}
	move_count = 0

	fail_prob_basic = 0.27
	fail_prob_grapple = 0.37
	fail_prob_hold = 0.21
	fail_prob_aerial = 0.57

	match_finished = False

	ko = False

	def __init__(self):
		self.setup_teams()
		self.filename_setup()
		return


	def __repr__(self):
		output_message = ""
		output_message = "The teams are : \n"
		for team_no in xrange(len(self.teams)):
			output_message += "\nTEAM %d - \n" % (team_no+1)
			for member in self.teams[team_no]:
				output_message += "%s \n" % (member[0])
		return output_message
		

	def setup_teams(self):
		for team_no in {0,1}:
			wr_team = self.teams[team_no]
			for wrestler in wr_team:
				self.match_teams[team_no].append([wrestler[0], wrestler[1], wrestler[2], 100.0, wrestler[3]])


	def filename_setup(self):
		global final_save_location

		if not final_save_location[:-1] in os.listdir('.'):
			os.mkdir(final_save_location)

		filename = ""
		for team_no in {0,1}:
			wr_team = self.teams[team_no]
			for wrestler in wr_team:
				filename += wrestler[3] + "_"
			if team_no == 0:
				filename += "_vs__"

		final_save_location += filename


	def text_display(self, finished = False):
		team_msg = ["", ""]

		for team_no in {0,1}:
			wr_team = self.match_teams[team_no]
			for wrestler in wr_team:
				txt = "%s \n" % (wrestler[0])
				team_msg[team_no] += (txt)

		
		self.team1msg.delete(0.0, END)
		self.team1msg.insert(0.0, team_msg[0])

		self.team2msg.delete(0.0, END)
		self.team2msg.insert(0.0, team_msg[1])

		currently_in_the_ring = ""

		if not finished or not self.match_finished:
			currently_in_the_ring = "\n\nCurrently in the ring - "+ self.match_teams[0][self.currently_1][0] \
									+ "\nAND\n" + self.match_teams[1][self.currently_2][0]
		
		self.currently_in.delete(0.0, END)
		self.currently_in.insert(0.0, currently_in_the_ring)


	def in_control_display(self):
		if self.in_control == 0:
			current_wr = self.currently_1
		else:
			current_wr = self.currently_2
		in_control_msg = self.match_teams[self.in_control][current_wr][0] + " is currently in control of the match"
		self.currently_in.insert(0.0, in_control_msg)


	def commentary_start(self):
		text_arg = "\nLILIAN GARCIA : Ladies and Gentlemen, this is the traditional Survivor Series elimination match !\n\n" 
		self.commentary_update(text_arg)
		text_arg = ""
		for n, wr_team in enumerate(self.match_teams):
			if n==0:
				text_arg += "LILIAN GARCIA : Introducing the team of "
			else:
				text_arg += "\nAnd introducing their opponents, the team of "
			for i, wrestler in enumerate(wr_team):
				if i == 0:
					text_arg += wrestler[0]
				elif i == 4:
					text_arg += " and " + wrestler[0] + " !! " 
				else:
					text_arg += ", " + wrestler[0]
		text_arg += "\n\n"
		self.commentary_update(text_arg)
		text_arg = "\nJIM ROSS : The match gets underway !\n*BELL RINGS*\nMICHAEL COLE : " \
				   + self.match_teams[0][self.currently_1][0] + " and " + self.match_teams[1][self.currently_2][0] \
				   + " start the match\n\n"
		self.commentary_update(text_arg)
		text_arg = "The two of them lock up to start us off.\n"
		self.commentary_update(text_arg)

	
	def commentary_update(self, text_arg):
		self.commentary_text += text_arg
		self.commentary.insert(0.0, text_arg)	


	def retrieve_basic(self):
		return (basic_ratings, basic_count)


	def retrieve_grapple(self):
		return (grapple_ratings, grapple_count)
	

	def retrieve_hold(self):
		return (hold_ratings, hold_count)
	

	def retrieve_aerial(self):
		return (aerial_ratings, aerial_count)


	def retrieve_finisher(self):
		return ("Perform finisher", 1)


	def retrieve_tag(self):
		return ("Tag in a teammate", 2)


	def default_retrieve(self):
		return ("DEFAULT", 0)


	def make_move(self, arg):
		move_list = {}
		move_count = 0
		selected_function = arg
#		print "\n", selected_function
		try:
			func = getattr(self, ("retrieve_" + selected_function))
		except AttributeError:
			func = self.default_retrieve
		except KeyError:
			func = self.default_retrieve
		self.move_list, self.move_count = func()
#		print self.move_list
#		print self.move_count


	def do_basic(self):
		self.make_move('basic')
		fail_prob = getattr(self, ('fail_prob_' + 'basic'))
		self.move_perform(fail_prob)

		
	def do_grapple(self):
		self.make_move('grapple')
		fail_prob = getattr(self, ('fail_prob_' + 'grapple'))
		self.move_perform(fail_prob)

		
	def do_hold(self):
		self.make_move('hold')
		fail_prob = getattr(self, ('fail_prob_' + 'hold'))
		self.move_perform(fail_prob)


	def do_aerial(self):
		self.make_move('aerial')
		fail_prob = getattr(self, ('fail_prob_' + 'aerial'))
		self.move_perform(fail_prob)

		
	def do_finisher(self):
		self.make_move('finisher')
		self.finisher_perform()

		
	def do_tag(self):
		self.make_move('tag')
		self.tag_perform()


	def do_elimination(self, eliminated):
		if eliminated == 0:
			t = 0
			el = self.currently_1
		else:
			t = 1
			el = self.currently_2
		el_team = self.match_teams.pop(t)
		person = el_team.pop(el)
		el_msg = "LILIAN GARCIA : " + person[0] + " has been eliminated !\n\n**************\n\n"
		self.commentary_update(el_msg)

		if len(el_team) != 0:	
			self.match_teams.insert(t, el_team)
			new_control = random.randrange(0, len(self.match_teams[t]))
			el_msg = "COLE : " + self.match_teams[t][new_control][0] + " comes in.\n\n"
			self.commentary_update(el_msg)
			if t == 0:
				self.currently_1 = new_control
			else:
				self.currently_2 = new_control
			self.in_control = random.randrange(0, 2)
			self.text_display()
			self.in_control_display()


		else:
			self.match_teams.insert(t, el_team)
			el_msg = "LILIAN GARCIA : And the winners of this match, the team of "
			wr_team = self.teams[(t + 1)%2]

			for i, wrestler in enumerate(wr_team):
				if i == 0:
					el_msg += wrestler[0]
				elif i == 4:
					el_msg += " and " + wrestler[0] + " !! " 
				else:
					el_msg += ", " + wrestler[0]

			el_msg += "\n\n"		
			self.match_finished = True
			self.text_display(finished = True)
			self.commentary_update(el_msg)
			self.finish_game()		


	def power_update(self, powers):
		ko_msg = ""

		wr1_p, wr2_p = powers
		
		self.match_teams[0][self.currently_1][3] -= wr1_p
		if self.match_teams[0][self.currently_1][3] >= 100.0:
			self.match_teams[0][self.currently_1][3] = 99.0
		if self.match_teams[0][self.currently_1][3] < 5.0:
			ko_msg = "COLE : Look JR, " + self.match_teams[0][self.currently_1][0] + " is struggling to get back on his feet\n"
			ko_msg += "JR: You're right Cole. He looks like he's out. Yeah, the ref's calling for the bell\n"
			ko_msg += "COLE: That's the end of him in this match.\n\n"
			self.ko = True
			self.text_display()
			self.in_control_display()
			self.commentary_update(ko_msg)
			self.do_elimination(0)
		
		self.match_teams[1][self.currently_2][3] -= wr2_p
		if self.match_teams[1][self.currently_2][3] >= 100.0:
			self.match_teams[1][self.currently_2][3] = 99.0
		if self.match_teams[1][self.currently_2][3] < 5.0:
			ko_msg = "COLE : Look JR, " + self.match_teams[1][self.currently_2][0] + " is struggling to get back on his feet\n"
			ko_msg += "JR: You're right Cole. He looks like he's out. Yeah, the ref's calling for the bell\n"
			ko_msg += "COLE: That's the end of him in this match.\n\n"
			self.ko = True
			self.text_display()
			self.in_control_display()
			self.commentary_update(ko_msg)
			self.do_elimination(1)


	def move_perform(self, fail_prob):
		move_msg = ""
		exec_move_key = random.randrange(0, self.move_count)
		exec_move, exec_stat = self.move_list[exec_move_key]
#		print exec_move, ' ', exec_stat
		
		if self.in_control == 0:
			cur_wr, other_wr = self.currently_1, self.currently_2
		else:
			cur_wr, other_wr = self.currently_2, self.currently_1
		
		move_exec = random.random()
		if move_exec < fail_prob:
			move_msg = "JR : " + self.match_teams[self.in_control][cur_wr][0] + " tried to go for a " + exec_move \
					 + ", but " + self.match_teams[(self.in_control + 1)%2][other_wr][0] + " managed to counter it.\n\n"
			self.in_control = (self.in_control + 1) % 2
		else:
			z = self.match_teams[self.in_control][cur_wr][1] - (self.match_teams[(self.in_control + 1)%2][other_wr][1] / 1.5)
			damage = (z * exec_stat) + (move_exec / 4.0)
			move_msg = "JR : " + self.match_teams[self.in_control][cur_wr][0] + " with the " + exec_move +".\n\n"
			power_modifications = [0.0, 0.0]
			if exec_stat > 0.0:
				power_modifications[self.in_control] = 0.0
				power_modifications[(self.in_control + 1) % 2] = damage / 1.5
			else:
				power_modifications[self.in_control] = damage/1.5
				power_modifications[(self.in_control + 1) % 2] = damage/3
			self.power_update(power_modifications)

		if not self.match_finished:
			self.text_display()
			self.in_control_display()
		self.commentary_update(move_msg)


	def finisher_perform(self):
		fin_msg = ""

		if self.in_control == 0:
			cur_wr, other_wr = self.currently_1, self.currently_2
		else:
			cur_wr, other_wr = self.currently_2, self.currently_1

		fin_track = random.randrange(0, len(self.match_teams[self.in_control][cur_wr][2]))
		fin_move = self.match_teams[self.in_control][cur_wr][2][fin_track]
		
		if fin_move in impact_ratings:
			fin_stat = impact_ratings[fin_move]
		else:
			fin_stat = submission_ratings[fin_move]

		fin_msg = "COLE : " + self.match_teams[self.in_control][cur_wr][0] + " goes for the " + fin_move

		z = self.match_teams[self.in_control][cur_wr][1] - (self.match_teams[(self.in_control + 1)%2][other_wr][1] / 1.5)
		
		if (random.random() * 10.0) > z:
			cur_control = self.in_control
			new_control = random.randrange(0, 2)
			
			if cur_control == new_control:
				fin_msg += ", but " + self.match_teams[(self.in_control + 1)%2][other_wr][0] + " manages to slip away.\n\n"
			else:
				fin_msg += ", but " + self.match_teams[(self.in_control + 1)%2][other_wr][0] + " counters !\n\n"

			self.in_control = new_control
			if not self.match_finished:
				self.text_display()
				self.in_control_display()
			self.commentary_update(fin_msg)

		else:
			power_modifications = [0.0, 0.0]
			
			if fin_move in impact_ratings:
				fin_msg += ". And IT CONNECTS ! \n\n" 
				self.commentary_update(fin_msg)
				damage = (z+0.2) * fin_stat
				power_modifications[self.in_control] = 0.0
				power_modifications[(self.in_control + 1) % 2] = damage
				self.power_update(power_modifications)
				
				try:
					power_cur = self.match_teams[self.in_control][cur_wr][3]
					power_other = self.match_teams[(self.in_control + 1)%2][other_wr][3]
					power = power_other - (power_cur - power_other)
				except IndexError:
					print ""
				
				if not self.ko:
					fin_msg = "He goes for the cover.. 1 !! 2 !!..\n\n"
					self.commentary_update(fin_msg)
					
					if (random.random() * 100.0) > power:
						fin_msg = "3 !!!\n\n"
						self.commentary_update(fin_msg)
						fin_msg = "JR : He gets the pin !\nCOLE : Vintage " + self.match_teams[self.in_control][cur_wr][4] + " !\n\n"
						self.commentary_update(fin_msg)
						power_modifications = [0.0, 0.0]
						power_modifications[self.in_control] = -12.5
						self.power_update(power_modifications)
						self.do_elimination((self.in_control + 1)%2)
					else:
						fin_msg = ".. KICK OUT !!\n\n"
						self.commentary_update(fin_msg)
						fin_msg = "JR : How close was that !\nCOLE : He kicks out at two and stays alive in this match\n\n"
						self.commentary_update(fin_msg)
						power_modifications[self.in_control] = 1.5
						power_modifications[(self.in_control + 1) % 2] = -15.0
						self.power_update(power_modifications)
					
				else:
					self.ko = False

			else:
				fin_msg += ". He's got it locked in !! " + self.match_teams[(self.in_control + 1)%2][other_wr][0] \
							+ " is struggling !!\n\n"
				self.commentary_update(fin_msg) 
				damage = (z+0.2) * fin_stat
				power_cur = self.match_teams[self.in_control][cur_wr][3]
				power_other = self.match_teams[(self.in_control + 1)%2][other_wr][3] - (damage)
				power = power_other - (power_cur - power_other)
				
				if (random.random() * 100.0) > power:
					fin_msg = "JR : HE TAPS OUT !! HE TAPS OUT !!\n\n"
					self.commentary_update(fin_msg)
					power_modifications = [0.0, 0.0]
					power_modifications[self.in_control] = -12.5
					self.power_update(power_modifications)
					self.do_elimination((self.in_control + 1) % 2)
				else:
					fin_msg = "COLE : He's slowly crawling towards the ropes... He makes it ! \nJR: The ref ordering to break the hold. " \
							  + "That was a really close call.\n\n"
					power_modifications[self.in_control] = 0.0
					power_modifications[(self.in_control + 1) % 2] = damage/2.0 - 7.5
					self.power_update(power_modifications)
					self.in_control = random.randrange(0, 2)
					self.commentary_update(fin_msg)
				
			if not self.match_finished:
				self.text_display()
				self.in_control_display()
				

	def tag_perform(self):
		tag_msg = ""
		
		if self.in_control == 0:
			cur_wr = self.currently_1
		else:
			cur_wr = self.currently_2
		
		if len(self.match_teams[self.in_control]) == 1:
			tag_msg = "COLE : " + self.match_teams[self.in_control][cur_wr][0] + " tries to make a tag, but no one's there.\n" \
					+ "JR : I think he forgot that he's on his own out there !\n\n"
			self.in_control = (self.in_control + 1) % 2
		else:
			tag_msg = self.match_teams[self.in_control][cur_wr][0] + " with the tag.\n"
			for i, wrestler in enumerate(self.match_teams[self.in_control]):
				if i != cur_wr:
					if wrestler[3] < 90.0:
						self.match_teams[self.in_control][i][3] += 8.0	
			team_shuffle = range(len(self.match_teams[self.in_control]))
			team_shuffle.pop(cur_wr)
			random.shuffle(team_shuffle)
			cur_wr = team_shuffle[0]
			if self.in_control == 0:
				self.currently_1 = cur_wr
			else:
				self.currently_2 = cur_wr
			tag_msg += "COLE : " + self.match_teams[self.in_control][cur_wr][0] + " enters the match.\n\n"
			self.in_control = random.randrange(0, 2)
		
		self.text_display()
		self.in_control_display()
		self.commentary_update(tag_msg)


	def finish_game(self):
		self.import_button = Button(
									self,
									text = "IMPORT COMMENTARY AND CLOSE GAME",
									width = 60,
									padx = 5,
									command = self.import_comm
									).grid(row = 6, column = 2, columnspan = 9, sticky = W)

		self.just_quit = Button(
								self,
								text = "CLOSE GAME",
								width = 60,
								padx = 5,
								command = self.close_game
								).grid(row = 6, column = 6, columnspan = 9, sticky = W)
			

	def import_comm(self):
		global final_save_location

		filename = ""

		random_md5_hash = md5(self.commentary_text.encode('utf8')).hexdigest()

		filename += random_md5_hash

		filename += ".txt"

		final_save_location += filename

		commentary_file = open(final_save_location,"w")
		commentary_file.truncate()
		file_to_write = self.commentary_text
		try:
			commentary_file.write(file_to_write)
		except:
			for char in file_to_write:
				commentary_file.write(char)
		commentary_file.close()
		self.quit()


	def close_game(self):
		self.quit()


##############################################

class MatchRun(Frame, SurvivorSeriesGame):
	"""	GUI class for running the match
		Creates the required widgets -
			* Buttons for every action of the wrestler 
			* A text area to display who is currently in control (performing the next move)
			* Text areas to display the non-eliminated members of each team
			* Commentary text area  

		We have a method move_perform() for dynamic dispatch
		############## Think of a proper way to use move_perform()

	"""
	
	functions = {1:'basic', 2:'grapple', 3:'hold', 4:'aerial', 5:'finisher', 6:'tag'}

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()


	def __repr__(self):
		return "The MatchRun class handles the GUI that displays the progress of the match." 


	def create_widgets(self):
		# Creates the required widgets	
		self.intro = Label(self, text = "Ladies and Gentlemen. This is the traditional Survivor Series 5-on-5 elimination match !")
		self.intro.grid(row = 0, column = 2, columnspan = 8, sticky = W)

		
		self.currently_in = Text(self, width = 25, height = 15, wrap = WORD)
		self.currently_in.grid(row = 2, column = 0, columnspan = 5, sticky = W)

		self.team1display = Label(self, text = "TEAM 1 - ")
		self.team1display.grid(row = 1, column = 5, columnspan = 3, sticky = W)

		self.team1msg = Text(self, width = 25, height = 15, wrap = WORD)
		self.team1msg.grid(row = 2, column = 5, columnspan = 5, sticky = W)
		
		self.team2display = Label(self, text = "TEAM 2 - ")
		self.team2display.grid(row = 1, column = 11, columnspan = 3, sticky = W)

		self.team2msg = Text(self, width = 25, height = 15, wrap = WORD)
		self.team2msg.grid(row = 2, column = 11, columnspan = 5, sticky = W)
		
		self.currently_1 = random.randrange(0,len(self.match_teams[0]))
		self.currently_2 = random.randrange(0,len(self.match_teams[1]))
		self.in_control = random.randrange(0, 2)
		
		self.text_display()
		self.in_control_display()

		self.instruction = Label(self, text = "Select the type of move for the wrestler in control to perform ")
		self.instruction.grid(row = 4, column = 1, columnspan = 6, sticky = W)

		self.button_set = []

		for i, key in enumerate(self.functions):
			med = Button(
				  		self, 
				 	  	text = self.functions[key].upper(), 
			 	  		width = 10, 
			 	  		padx = 5, 
			 	  		command = getattr(self, "do_" + self.functions[key])
			 	  		).grid(row = 6, column = i + 2, columnspan = 3, sticky = W)
			self.button_set.append(med)
			
		self.commentary = Text(self, width = 75, height = 50, wrap = WORD)
		self.commentary.grid(row = 8, column = 2, columnspan = 6, sticky = W)

		self.commentary_start()

		
"""	def move_perform(self, cmd, arg):
		# Dynamic dispatch function to run when a move is performed.
		# Called from the corresponding buttons in the GUI
		
		try:
			func = getattr(self, "do_", cmd)
		except AttributeError:
			self.default(cmd)
		return func(arg) 
"""	

##############################################


class WrestlerSelect(Frame):
	""" GUI class for team selection menu 
		This class creates the GUI, with the required widgets -
			* Checkbuttons for all the wrestlers in the list
			* Text area to display the currently selected team, rating total, and other messages
			* Confirmation Button
		The GUI stays active until both the teams are confirmed, after which, it can be closed
	"""

	team_set = False
	team_being_set = 0
	selected_team = []

	def __init__(self, master, team_being_set):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.team_being_set = team_being_set

	def create_widgets(self):
		# Creates the required widgets
		global maxlimit

		self.intro = Label(self, text = "SURVIVOR SERIES ELIMINATION MATCH - TEAM SELECTION MENU")
		self.intro.grid(row = 0, column = 0, columnspan = 16, sticky = W)

		self.instruction = Label(self, text = "Select your team of 5 wrestlers, without exceeding the maximum rating total of " + str(maxlimit))
		self.instruction.grid(row = 2, column = 0, columnspan = 16, sticky = W)

		self.selection = []

		for i, key in enumerate(wrestlers):
			med = BooleanVar()
			Checkbutton(self, text = str(wrestlers[key][0]) + "," + str(wrestlers[key][1]), variable = med, command = self.team_display).grid(row = 3 + int(i/7), column = (i%7), columnspan = 1, sticky = W)
			self.selection.append(med)

		self.team = Text(self, width = 90, height = 10, wrap = WORD)
		self.team.grid(row = 5 + int(len(wrestlers)/7), column = 0, columnspan = 10, sticky = W)
		self.team.delete(0.0, END)
		self.team.insert(0.0, "Select the team of 5 for Team 1")
	
		self.confirm = Button(self, text = "CONFIRM" , command = self.confirm_team)
		self.confirm.grid(row = 7 + int(len(wrestlers)/7), column = 3, columnspan = 3, sticky = W)
	

	def remove_widgets(self):
		self.intro.destroy()
		self.instruction.destroy()
		self.confirm.destroy()

	def team_display(self):
		# To display the selected team
		team_list = ""
		team_rating_total = 0
		count = 0
		completed = False
		overlap = False

		self.team_set = False

		global maxlimit

		for i, key in enumerate(wrestlers):
			if self.selection[i].get():
				team_list += (" ** " + str(wrestlers[key][0]))
				team_rating_total += wrestlers[key][1]
				count += 1

		if team_rating_total > maxlimit:
			team_list += "\nMAXLIMIT EXCEEDED !! Modify your team"
		elif count > 5:
			team_list += "\nMAX TEAM SIZE EXCEEDED !! Modify your team"
		else:
			completed = True

		if completed and count == 5:
			self.selected_team = []
			for i, key in enumerate(wrestlers):
				if self.selection[i].get():
					if self.team_being_set == 1:
						if wrestlers[key] in SurvivorSeriesGame.teams[0]:
							overlap = True
							team_list += "\nYou have selected a wrestler already selected by Player 1" 
							break
					self.selected_team.append(wrestlers[key])

			if not overlap:
				team_list += "\nYOUR TEAM HAS BEEN SET !!"
				self.team_set = True

		if not self.team_set:
			team_list += "\nRating Total for current selected team : " + str(team_rating_total)

		if not self.team_being_set > 1:
			self.team.delete(0.0, END)
			self.team.insert(0.0, team_list)

	def confirm_team(self):
		# Event handler for button click
		message = ""

		if self.team_set:
			SurvivorSeriesGame.teams.append(self.selected_team)
			self.team_being_set += 1
			if self.team_being_set > 1:
				self.quit()
			if self.team_being_set == 1:
				message = "Now select the team of 5 for Team " + str(self.team_being_set + 1)
			else:
				self.remove_widgets()
				message = "You can now close this window"
			for i, key in enumerate(wrestlers):
				self.selection[i].set(False)
		else:
			message = "Complete selecting your team before continuing"

		self.team.delete(0.0, END)
		self.team.insert(0.0, message)


##################

# To run the GUI to set the two teams

def gui_caller_for_team_set():

	root1 = Tk()
	root1.title("Survivor Series Team Selection")
	root1.geometry("1050x700")

	WS1 = WrestlerSelect(root1, 0)

	root1.mainloop()
#	root1.geometry("0x0")
	root1.destroy()

##################

# To run the GUI to run the game

def gui_caller_for_game_run():

	ss1 = SurvivorSeriesGame()
#	print ss1
	root1 = Tk()
	root1.title("The Match")
	root1.geometry("1050x700")

	MR1 = MatchRun(root1)

	root1.mainloop()


##################

# The main function starts the execution of the program

def main():	
	gui_caller_for_team_set()
	gui_caller_for_game_run()


# Boilerplate
if __name__ == '__main__':
	main()
