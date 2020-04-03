from structural_design_patterns.bridge.articles import articles
from structural_design_patterns.bridge.free_web_page import FreeWebPage
from structural_design_patterns.bridge.paid_web_page import PaidWebPage
from structural_design_patterns.bridge.sport_fetcher import SportFetcher
from structural_design_patterns.bridge.war_fetcher import WarFetcher

art1 = articles[0]
art2 = articles[1]

fetcher1 = SportFetcher(art1)
fetcher2 = WarFetcher(art2)

free_website = FreeWebPage(fetcher1)
paid_website = PaidWebPage(fetcher1)

free_website2 = FreeWebPage(fetcher2)
paid_website2 = PaidWebPage(fetcher2)

free_website.show_page()
print('/////////////////////////')
paid_website.show_page()
print('/////////////////////////')

free_website2.show_page()
print('/////////////////////////')
paid_website2.show_page()
print('/////////////////////////')

print(free_website2)
