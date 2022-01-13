# CovidTracking
1. Overview
- Covid Tracking is a Linux application displaying Covid19 information in Vietnam for Linux users.
- Covid Tracking app is built by using Gnome platform and Python libraries to crawl data and visualize it.

2. Architecture design
![image](https://user-images.githubusercontent.com/62065172/149268593-ed3052a5-a380-48dd-9b6a-fa7d46d3c195.png)

3. GUI design
- News: showing all the news related to Covid-19 pandemic

- Cases: showing information related to Covid-19 cases (e.g num of cases, num of death, maps and tables visualize the information ,…)

- Vaccines: showing information related to Covid19 vaccines (e.g num of vaccines, num of fully vaccinated people, maps and tables visualize the information, …)

4. Technologies:
- Gnome platform:
+ Gnome's dedicated IDE: Gnome builder
+ Gnome framework for distribution: flatpak
- Programming language: Python + GTK3
- GUI design app: Glade
- Scraping tools: Scrapy + Splash
- Data visualization: numpy, pandas, matplotlib
- Auto crawl data using Cron job scheduler

5. Video demo:

https://www.youtube.com/watch?v=8-5wNtzmUkM
