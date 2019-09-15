# __author__ == "Priya"
import webbrowser


URLS = {'GMAIL':"https://gmail.com",'FACEBOOK':"https://facebook.com",'LINKEDIN':"https://linkedin.com",'TWITTER':'https://twitter.com',
        'INSTAGRAM':'https://instagram.com', 'GITHUB':'https://github.com'}

for each in URLS.keys():
    webbrowser.open_new_tab(URLS[each])

#Writing "python3 <path of chrome_tabs.py>" in /etc/rc.local which will run this script when your machine starts