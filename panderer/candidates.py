class Candidate(object):
    def __init__(self,surname,full_name,handles,hashtags,party):
        self.surname=surname
        self.full_name=full_name
        self.handles=handles
        self.hashtags=hashtags
        self.party=party

biden=Candidate('biden', 'Joe Biden', ['JoeBiden'], ['Biden2016', 'JoeBiden2016'],"Democrat")
chafee=Candidate('chafee', 'Lincoln Chafee', ['LincolnChafee'], ['Chafee2016'],"Democrat")
clinton=Candidate('clinton','Hillary Clinton',['HillaryClinton'],['Hillary2016', 'ImWithHer', 'HillaryClinton2016', 'Hillary', 'HillYes', 'Clinton2016', 'ReadyForHillary', 'IStandWithHillary', 'TeamHillary'],"Democrat")
omalley=Candidate('omalley', "Martin O'Malley",['MartinOMalley'], ["O'Malley2016", "MartinO'Malley2016","OMalley2016", "MartinOMalley2016"],"Democrat")
sanders=Candidate('sanders','Bernie Sanders',['BernieSanders','SenSanders'],['Sanders2016', 'Bernie2016', 'FeelTheBern', 'LetItBern', 'BernieSanders2016', 'IStandWithBernie', 'WeEndorseBernie', 'BernBabyBern', 'TeamBernie'],"Democrat")
webb=Candidate('webb', 'Jim Webb', ['JimWebbUSA'], ['Webb2016', 'JimWebb2016'],"Democrat")

bush=Candidate('bush','Jeb Bush',['JebBush'],['Bush2016', 'Jeb2016', 'JebBush2016', 'AllInForJeb'],"Republican")
carson=Candidate('carson','Ben Carson',['RealBenCarson'],['Carson2016', 'BenCarson2016', 'America4Ben', 'Ben4Potus', 'WinBenWin', 'DrBenCarson2016'],"Republican")
christie=Candidate('christie','Chris Christie',['ChrisChristie'],['Christie2016', 'ChrisChristie2016', 'TellingItLikeItIs'],"Republican")
cruz=Candidate('cruz','Ted Cruz',['tedcruz'],['Cruz2016', 'TedCruz2016','CruzCrew'],"Republican")
fiorina=Candidate('fiorina','Carly Fiorina',['CarlyFiorina'],['Fiorina2016', 'CarlyFiorina2016', 'Carly2016', 'AmericasIronLady', 'BeLikeCarly', 'TeamCarly'],"Republican")
gilmore=Candidate('gilmore','Jim Gilmore',['gov_gilmore'], ['Gilmore2016', 'FeelTheGil', 'JimGilmore2016'],"Republican")
graham=Candidate('graham','LindseyGraham',['LindseyGrahamSC','GrahamBlog'],['Graham2016', 'LindseyGraham2016', 'StandWithGraham', 'GrahamForPresident'],"Republican")
huckabee=Candidate('huckabee','Mike Huckabee',['GovMikeHuckabee'],['Huckabee2016', 'MikeHuckabee2016', 'ImWithHuck','ILikeMike'],"Republican")
jindal=Candidate('jindal','Bobby Jindal',['BobbyJindal'],['Jindal2016', 'BobbyJindal2016'],"Republican")
kasich=Candidate('kasich','John Kasich',['JohnKasich'],['Kasich2016', 'JohnKasich2016', 'KasichForPresident'],"Republican")
pataki=Candidate('pataki','George Pataki',['GovernorPataki'],['Pataki2016', 'GeorgePataki2016'],"Republican")
paul=Candidate('paul','Rand Paul',['RandPaul'],['Paul2016', 'StandWithRand', 'RandPaul2016'],"Republican")
perry=Candidate('perry','Rick Perry',['GovernorPerry'],['Perry2016', 'RickPerry2016'],"Republican")
rubio=Candidate('rubio','Marco Rubio',['marcorubio'],['Rubio2016', 'MarcoRubio2016', 'TeamMarco'],"Republican")
santorum=Candidate('santorum','Rick Santorum',['RickSantorum'],['Santorum2016', 'RickSantorum2016'],"Republican")
trump=Candidate('trump','Donald Trump',['realDonaldTrump'],['Trump2016', 'DonaldTrump2016', 'DonaldTrumpForPresident', 'TrumpWillTriumph', 'Trump2k16', 'DonaldTrump2k16', 'TrumpForPresident', 'MakeAmericaGreatAgain', 'TrumpTrain'],"Republican")
walker=Candidate('walker','Scott Walker',['ScottWalker'],['Walker2016, ScottWalker2016'],"Republican")

all_candidates={'clinton': clinton, 'omalley': omalley, 'sanders':sanders, 'bush':bush, 'carson':carson, 'christie':christie, 'cruz':cruz, 'fiorina':fiorina,
     'huckabee': huckabee, 'kasich': kasich, 'paul': paul, 'rubio': rubio, 'trump':trump}

#all_candidates={'omalley': omalley, 'bush':bush, 'carson':carson, 'christie':christie, 'fiorina':fiorina,
#      'huckabee': huckabee, 'kasich': kasich}