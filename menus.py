"""
Menus definitions 

"""


from collections import OrderedDict


PUBS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/publication/{}") , 
    ('DOI' , "https://app.dimensions.ai/discover/publication?search_mode=content&search_text={}&search_type=kws&search_field=doi"),
    ('PubmedID' , "https://app.dimensions.ai/discover/publication?search_mode=content&search_text=pmid%3A{}&search_type=kws&search_field=full_search"),
    # ('ISBN' , "https://app.dimensions.ai/details/publication/{}"),
])

GRANTS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/grant/{}") , 
])

PATENTS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/patent/{}") , 
])

POLICY_DOCUMENTS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/policy_documents/{}") , 
])

CLINICAL_TRIALS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/clinical_trial/{}") , 
])

DATASETS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/details/data_set/{}") , 
])

RESEARCHERS_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/publication?and_facet_researcher={}") , 
])

GRID_MENU = OrderedDict([
    ('DimensionsID' , "https://app.dimensions.ai/discover/publication?and_facet_research_org={}") , 
])



CATEGORIES_MENU = OrderedDict([
            ("Pomodoro", 25),
            ("40 minutes", 40),
            ("1 hour", 60),
            ("2 hours", 120),
            ("Custom...", None),
        ])
