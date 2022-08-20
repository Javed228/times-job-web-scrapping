#Python program to scrape 1000 job data from website

def scrap_data():
    #first url is link before page no
    first_url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence="
    #second url is link after page no
    second_url = "&startPage=1"
    lst_url = []
    for i in range(1,41):
        lst_url.append(first_url+str(i)+second_url)      #complete 40 url's

    '''pip install requests
    import requests for getting html code in string'''
    import requests

    '''pip install bs4
    import BeautifulSoup for converting html string to html code'''
    from bs4 import BeautifulSoup

    lst_data = []   #using blank list for add all dictionary data
    for url in lst_url:
        #getting url html data in string
        all_url = requests.get(url).text

        #convert html string data to html code
        soup_data = BeautifulSoup(all_url,"html.parser")

        #find one page job information
        one_page_data = soup_data.find_all("li",class_="clearfix job-bx wht-shd-bx")
        for l in one_page_data:  #using loop one job all information

            #fetch company_title
            company_title = l.find("h2").text.strip()
            #print(company_title)

            #fetch company_name
            company = l.find("h3",class_="joblist-comp-name").text.strip()
            company_name = company.replace('(More Jobs)','')  #using replace for replace (more job) to space
            #print(company_name)

            #fetch experience
            exp = l.find("li").text.strip()
            experience = exp.replace('card_travel','')   #using replace for replace (card_travel) to space
            #print(experience)

            #fetch company_location
            company_location = l.find("span").text.strip("(More Jobs)")
            #print(company_location)

            #fetch descreption
            des = l.find("ul",class_="list-job-dtl clearfix").text.strip()
            descreption = des.splitlines()[1]   #using splitlines for split line by line and take index
            #print(descreption)

            #fetch keyskills
            keyskills = l.find("span",class_="srp-skills").text.strip()
            #print(keyskills)

            #fetch job_url
            job_url = l.find("a")["href"]
            #print(job_url)

            #add all data in dictionary
            dict = {
                "job_title": company_title,
                "company_name": company_name,
                "Experience": experience,
                "Company_location": company_location,
                "Descreption": descreption,
                "Keyskill": keyskills,
                "Job_url": job_url
            }
            lst_data.append(dict)     #add all dict data in lst_data
            #print(lst_data)

    '''pip install pandas 
    import pandas for convert data to framework'''
    import pandas as pd

    '''pip install openpyxl
    import load_workbook for convert DataFrame to excel'''
    from openpyxl import load_workbook
    dataframe = pd.DataFrame(lst_data)
    dataframe.to_excel("web-scrap-jobdata.xlsx")
scrap_data()
