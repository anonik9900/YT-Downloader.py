#!/usr/bin/env python3
import random
import string
import subprocess #Process commands
import socket #Process socket data
import pyfiglet
import sys
import os
import time
import pytube
from pytube import YouTube


ascii_banner = pyfiglet.figlet_format("YT-Downloader")
print(ascii_banner)
print ("{< Devoled By Anonik V 0.1>}")
print("")



def MenuShell():
	choice = input("Type...\n {1} to download video with audio \n {2} to only video \n {3} to only audio \n \n")
	if choice == str("1"):
		
		link = input("Enter the video link:")
		yt = YouTube(link)
		#Title of video
		print("Title: ",yt.title)#Number of views of video
		print("Number of views: ",yt.views)#Length of the video
		print("Length of video: ",yt.length,"seconds")#Description of video
		print("Description: ",yt.description)#Rating
		print("Ratings: ",yt.rating)
		#print(yt.streams.filter(progressive=True))
		#ys = yt.streams.get_by_itag('137')
		time.sleep(0.2)
		ys = yt.streams.get_highest_resolution()
		ys.download()
		contatore =0
		while contatore <= 99:
			contatore = contatore + 1
			#time.sleep(0.4)			
			print ("Download Video: [" +str(contatore)+"%]")
			time.sleep(0.4)
			os.system("clear")
		print("")
		print ("Download of ",yt.title, " Completed")
		#print(yt.streams)
		
	
	if choice == str("2"):
		link = input("Enter the video link:")
		yt = YouTube(link)
		#Title of video
		print("Title: ",yt.title)#Number of views of video
		print("Number of views: ",yt.views)#Length of the video
		print("Length of video: ",yt.length,"seconds")#Description of video
		print("Description: ",yt.description)#Rating
		print("Ratings: ",yt.rating)
		#print(yt.streams.filter(progressive=True))
		time.sleep(0.2)
		ys = yt.streams.get_by_itag('137')
		ys.download()
		contatore =0
		while contatore <= 99:
			contatore = contatore + 1
			#time.sleep(0.4)			
			print ("Download Video: [" +str(contatore)+"%]")
			time.sleep(0.3)
			os.system("clear")
		print("")
		print ("Download of ",yt.title, " Completed")
		#print(yt.streams)
		
		
	
	if choice == str("3"):
		link = input("Enter the video link:")
		yt = YouTube(link)
		#Title of video
		print("Title: ",yt.title)#Number of views of video
		print("Number of views: ",yt.views)#Length of the video
		print("Length of video: ",yt.length,"seconds")#Description of video
		print("Description: ",yt.description)#Rating
		print("Ratings: ",yt.rating)
		time.slepp(0.2)
		ys = yt.streams.get_by_itag('140')
		ys.download()
		contatore =0
		while contatore <= 99:
			contatore = contatore + 1
			#time.sleep(0.4)			
			print ("Download Audio: [" +str(contatore)+"%]")
			time.sleep(0.4)
			os.system("clear")
		print("")
		print ("Download of ",yt.title, " Completed")
		#print(yt.streams)
	
	
	else:
		sys.exit()




print (MenuShell())
