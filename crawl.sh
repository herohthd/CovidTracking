cd "/home/huydq/ITSS Linux/CovidTracking/provinces"
scrapy crawl province -O province.json
scrapy crawl vaccine -O vaccine.json
scrapy crawl dose -O dose.json
scrapy crawl case -O case.json
scrapy crawl caseByDay -O caseByDay.json
scrapy crawl deathByDay -O deathByDay.json
scrapy crawl caseProvince -O caseProvince.json
