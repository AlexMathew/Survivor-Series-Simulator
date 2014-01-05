# SURVIVOR SERIES SIMULATOR #
### github.com/AlexMathew/Survivor-Series-Simulator ###

Bringing together my love for pro-wrestling and programming.

## THE INSPIRATION : ##
	I've been learning Python for about 6 months now, and I started working with the Tkinter module for GUI programming about a month back. I wanted to put what I learnt to a little work, so I began thinking of something to work on. That's when it struck me. I've always loved pro-wrestling. And I've always imagined my Dream Teams for 5-on-5 Survivor Series Elimination matches. Why not build something to simulate matches between those Dream Teams ? And that's how this came to being.

## THE PROGRAM RUN : ##
	Run the program through your command prompt. 
	I made this while working on Windows, so I'm not sure how well it works with other OS's. (If you try running it on another OS and have a problem, do let me know. Or if you can find a fix, send a pull request. I'll merge it in !)
	Initially, you are prompted to enter the directory where you would like to save the final match commentary. (Again, a lot to work on with this. Make sure you enter an existing directory. I'll try to fix the program to accomodate for creating new directories.)
	Once you've entered the directory path, a Tkinter window opens, with a list of 125 wrestlers to choose from for your teams. I've allotted a rating for each of them. (Pro-wrestling purists may argue with me about some of the ratings. But my program, my ratings) Pick your team of 5, such that it doesn't exceed the maximum rating total of 43.5.
	Once you've picked both your teams, and confirmed them, a new Tkinter window opens for the match run. The team selection window stays open, but idle, in the background. You can close it if you want to.
	In the match run, use one of the 6 buttons to pick the type of moves. 
	> + Basic
	> + Grapple
	> + Hold
	> + Aerial
	> + Finisher
	> + Tag 
	To eliminate the opponent, use the "Finisher" button to perform the wrestler's finisher.
	The match continues until one of the teams is completely eliminated.
	Once the match is finished, use the "Import Commentary and Close Game" button to save the commentary into a text file, in the directory you initially specified. Otherwise, hit "Close Game" to just close the game.


*** Comments, suggestions and fixes are welcome ! ***