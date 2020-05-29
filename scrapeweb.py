#! /usr/bin/python3
import re
from bs4 import BeautifulSoup
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.HEADER+"SCRAPEWEB"+ bcolors.ENDC)
print(bcolors.HEADER+"(c)Vijay Sahu"+ bcolors.ENDC)
print(
'''
#ScrapeWeb
@fb.com/vijaysahuofficialpage

This Tool is for Educational Purpose Only
''')
print(bcolors.FAIL+ 'USE AT YOUR OWN RISK' + bcolors.ENDC)
user_permission = ""
while user_permission != 'n':
    user_permission = input(bcolors.WARNING +'Do you Want to Continue? (Y/N)\n>> '+ bcolors.ENDC).lower()
    collected_final_links = []
    collected_final_emails = []
    if user_permission == 'y':
        print(bcolors.OKGREEN +'Welcome'+ bcolors.ENDC + '\n')

        url = input(bcolors.BOLD + bcolors.HEADER + 'Enter Url\n>> ' + bcolors.ENDC)
        print(bcolors.WARNING+"Please Enter Naked Domain eg: website.com" + bcolors.ENDC)
        if 'http' in url:
            pass
        else:
            print(bcolors.FAIL + "[-]URL Error" + bcolors.ENDC + "\n")
            print(bcolors.WARNING+ "[-]http Missing in Url " + bcolors.ENDC + "\n")
            print(bcolors.OKGREEN+ "[*]Adding http in url" + bcolors.ENDC + "\n")
            url = f'http://{url}'
            print(bcolors.OKGREEN+ "[+]Successfully Added http" + bcolors.ENDC + "\n")
            print ("Target Url >> "+ url)        
        try:
            user_selected_option = int(input("Please Select the number\n1. Email\n2. Links\n>> "))


            def email():
                try:
                    email_data = requests.get(url, timeout=1).content
                except:
                    print(bcolors.FAIL + "[-]Connection TimeOut" + bcolors.ENDC) 

                htmldata = BeautifulSoup(email_data,"html.parser")
                email_data = htmldata.prettify()
                search_email = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email_data)
                for emails in search_email:
                    collected_final_emails.append(emails)
                    filename = url.split('//')
                    savefilename = filename[1]
                    semail = open(f"email{savefilename}.txt",'a')
                    semail.write(emails+'\n')
                    semail.close()
                    
                
            def links():
                try:
                    links_data = requests.get(url, timeout=1).content
                except:
                    print(bcolors.FAIL + "[-]Connection TimeOut" + bcolors.ENDC) 
                link_html_data = BeautifulSoup(links_data, "html.parser")
                for link_list in link_html_data.find_all('a'):
                    collected_links = link_list.get('href')
                    collected_final_links.append(collected_links)  
                    for all_links in collected_final_links:
                        filename = url.split('//')
                        savefilename = filename[1]
                        slinks = open(f"foundlinks{savefilename}.txt", 'a')
                        slinks.write(all_links+'\n')
                        slinks.close()
                
            if user_selected_option == 1:
                email()
                print(bcolors.OKBLUE+'Saving Emails' + bcolors.ENDC)
                print(bcolors.OKGREEN+'Saved Successfully' + bcolors.ENDC)
                print('Found Email Saved at root folder of this tool as foundemails.txt')
                    
            elif user_selected_option == 2:
                links()
                print(bcolors.OKBLUE+'Saving Links' + bcolors.ENDC)
                print(bcolors.OKGREEN+'Saved Successfully' + bcolors.ENDC)
                print('Found Email Saved at root folder of this tool as foundlinks.txt')
                            
            else:
                print("[-]Error")
        except:
            print(bcolors.FAIL + "[-]Error"+ bcolors.ENDC)
            print(bcolors.WARNING + 'Please Select a Number' + bcolors.ENDC)     
    elif user_permission == 'n':
        print(bcolors.WARNING + 'Thanks for using ScrapeWeb' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "[-]Error.........\n Unknown Error Occured"+ bcolors.ENDC) 





