from bs4 import BeautifulSoup
import requests

def read_lyrics(song): 
  beatles = ''
  with open(song, 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')    
  lyrics = soup.find('p', class_= 'verse')
  verse = lyrics.text
   
  for words in verse:
     beatles += words      
   
  return beatles 
  
 

