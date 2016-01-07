#! /usr/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import smtplib


NEWEST_TITLE = ""

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_newest_post(url):
    soup = make_soup(url)
    NEWEST_TITLE = soup.find("span", "title").string
    artist = soup.find("span", "artist").string
    return str(artist) + " " + str(NEWEST_TITLE)

def main():
    title = get_newest_post("http://www.pitchfork.com/reviews/best/tracks/1/")
    print(str(title))
    with open("song_name.txt", 'r') as myfile:
        print("reading file")
	old_title = myfile.read()
    if (title != old_title): 
      print("title != old_title")
      f = open("song_name.txt", 'w') 
      f.write(str(title))
      f.close()
      # send email 
      print ("sending email now")
      fromaddr = 'email@gmail.com'
      toaddrs = 'email@gmail.com'
      msg = ("There was a new post on pitchfork about " + str(title) +
      'Read more about it here: http://pitchfork.com/reviews/best/tracks/1/')

      username = 'username' 
      password = 'password'

      try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.close()
        print ("done")
      except: 
        print("fail")

if __name__ == '__main__':
    main()
