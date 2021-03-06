stopset = frozenset([
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "her",
    "hers",
    "herself",
    "it",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "r",
    "b",
    "can",
    "will",
    "just",
    "don",
    "should",
    "now",
    "ain't",
    "aren't",
    "can't",
    "could've",
    "couldn't",
    "didn't",
    "doesn't",
    "don't",
    "gonna",
    "hadn't",
    "hasn't",
    "haven't",
    "he'd",
    "he'll",
    "he's",
    "how'd",
    "how'll",
    "how's",
    "I'd",
    "I'll",
    "I'm",
    "I've",
    "isn't",
    "it'd",
    "it'll",
    "it's",
    "let's",
    "ma'am",
    "mightn't",
    "might've",
    "mustn't",
    "must've",
    "needn't",
    "o'clock",
    "oughtn't",
    "shan't",
    "she'd",
    "she'll",
    "she's",
    "should've",
    "shouldn't",
    "somebody'll",
    "somebody's",
    "someone'd",
    "someone'll",
    "someone's",
    "something's",
    "that'll",
    "that's",
    "there'd",
    "there's",
    "they'd",
    "they'll",
    "they're",
    "they've",
    "'tis",
    "'twas",
    "wanna",
    "wasn't",
    "we'd",
    "we'll",
    "we're",
    "we've",
    "weren't",
    "what'll",
    "what're",
    "what's",
    "where'd",
    "where's",
    "who'd",
    "who'll",
    "who're",
    "who's",
    "who've",
    "won't",
    "would've",
    "wouldn't",
    "y'all",
    "you'd",
    "you'll",
    "you're",
    "you've",
    "http",
    "https",
    "above",
    "also",
    "finally",
    "meanwhile",
    "actually",
    "automatically",
    "first",
    "second",
    "third",
    "moreover",
    "afterward",
    "foremost",
    "next",
    "accordingly",
    "another",
    "arguably",
    "furthermore",
    "otherwise",
    "however",
    "paradoxically",
    "incidentally",
    "presently",
    "presumably",
    "regrettably",
    "similarly",
    "still",
    "strangely",
    "then",
    "therefore",
    "too",
    "consequently",
    "ultimately",
    "ironically",
    "another",
    "both",
    "all",
    "anybody",
    "anyone",
    "anything",
    "each",
    "either",
    "everybody",
    "everyone",
    "everything",
    "little",
    "much",
    "neither",
    "nobody",
    "noone",
    "nothing",
    "one",
    "other",
    "somebody",
    "someone",
    "something",
    "few",
    "many",
    "others",
    "several",
    "any",
    "more",
    "most",
    "none",
    "some",
    "yesterday",
    "today",
    "tomorrow",
    "day",
    "week",
    "month",
    "year",
    "tonight",
    "night",
    "morning",
    "afternoon",
    "evening",
    "hour",
    "minute",
    "lincoln",
    "chafee",
    "lincolnchafee",
    "hillary",
    "clinton",
    "hillaryclinton",
    "martin",
    "o'malley",
    "omalley",
    "martinomalley",
    "martino'malley",
    "bernie",
    "sanders",
    "berniesanders",
    "jim",
    "webb",
    "jimwebb",
    "jeb",
    "bush",
    "jebbush",
    "ben",
    "carson",
    "bencarson",
    "dr",
    "drbencarson",
    "dr.",
    "chris",
    "christie",
    "chrischristie",
    "ted",
    "cruz",
    "tedcruz",
    "cruzcrew",
    "carly",
    "fiorina",
    "carlyfiorina",
    "gilmore",
    "jimgilmore",
    "lindsey",
    "graham",
    "lindseygraham",
    "mike",
    "huckabee",
    "mikehuckabee",
    "huck",
    "bobby",
    "jindal",
    "bobbyjindal",
    "john",
    "kasich",
    "johnkasich",
    "george",
    "pataki",
    "georgepataki",
    "rand",
    "paul",
    "randpaul",
    "rick",
    "perry",
    "rickperry",
    "marco",
    "rubio",
    "marcorubio",
    "santorum",
    "ricksantorum",
    "donald",
    "trump",
    "donaldtrump",
    "scott",
    "walker",
    "scottwalker",
    "jimwebbusa",
    "realbencarson",
    "gov_gilmore",
    "lindseygrahamsc",
    "grahamblog",
    "govmikehuckabee",
    "governorpataki",
    "governorperry",
    "realdonaldtrump",
    "hillary2016",
    "imwithher",
    "I'mwithher",
    "hillaryclinton2016",
    "hillyes",
    "clinton2016",
    "readyforhillary",
    "istandwithhillary",
    "teamhillary",
    "o'malley2016",
    "omalley2016",
    "martino'malley2016",
    "martinomalley2016",
    "sensanders",
    "sanders2016",
    "bernie2016",
    "feelthebern",
    "letitbern",
    "berniesanders2016",
    "istandwithbernie",
    "weendorsebernie",
    "bernbabybern",
    "teambernie",
    "webb2016",
    "jimwebb2016",
    "bush2016",
    "jeb2016",
    "jebbush2016",
    "allinforjeb",
    "carson2016",
    "bencarson2016",
    "america4ben",
    "ben4potus",
    "winbenwin",
    "drbencarson2016",
    "christie2016",
    "chrischristie2016",
    "tellingitlikeitis",
    "cruz2016",
    "tedcruz2016",
    "fiorina2016",
    "carlyfiorina2016",
    "carly2016",
    "americasironlady",
    "belikecarly",
    "teamcarly",
    "gilmore2016",
    "feelthegil",
    "jimgilmore2016",
    "graham2016",
    "lindseygraham2016",
    "standwithgraham",
    "grahamforpresident",
    "huckabee2016",
    "mikehuckabee2016",
    "imwithhuck",
    "ilikemike",
    "jindal2016",
    "bobbyjindal2016",
    "kasich2016",
    "johnkasich2016",
    "kasichforpresident",
    "pataki2016",
    "georgepataki2016",
    "paul2016",
    "standwithrand",
    "randpaul2016",
    "perry2016",
    "rickperry2016",
    "rubio2016",
    "marcorubio2016",
    "teammarco",
    "santorum2016",
    "ricksantorum2016",
    "trump2016",
    "donaldtrump2016",
    "donaldtrumpforpresident",
    "trumpwilltriumph",
    "trump2k16",
    "donaldtrump2k16",
    "trumpforpresident",
    "makeamericagreatagain",
    "trumptrain",
    "alabama",
    "alaska",
    "arizona",
    "arkansas",
    "california",
    "colorado",
    "connecticut",
    "delaware",
    "florida",
    "georgia",
    "hawaii",
    "idaho",
    "illinois",
    "indiana",
    "iowa",
    "kansas",
    "kentucky",
    "louisiana",
    "maine",
    "maryland",
    "massachusetts",
    "michigan",
    "minnesota",
    "mississippi",
    "missouri",
    "montana",
    "nebraska",
    "nevada",
    "hampshire",
    "jersey",
    "york",
    "carolina",
    "dakota",
    "ohio",
    "oklahoma",
    "oregon",
    "pennsylvania",
    "rhode",
    "island",
    "tennessee",
    "texas",
    "utah",
    "vermont",
    "virginia",
    "washington",
    "wisconsin",
    "wyoming",
    "al",
    "ak",
    "az",
    "ar",
    "ca",
    "co",
    "ct",
    "de",
    "fl",
    "ga",
    "hi",
    "id",
    "il",
    "in",
    "ia",
    "ks",
    "ky",
    "la",
    "me",
    "md",
    "ma",
    "mi",
    "mn",
    "ms",
    "mo",
    "mt",
    "ne",
    "nv",
    "nh",
    "nj",
    "nm",
    "ny",
    "nc",
    "nd",
    "oh",
    "ok",
    "or",
    "pa",
    "ri",
    "sc",
    "sd",
    "tn",
    "tx",
    "ut",
    "vt",
    "va",
    "wa",
    "wv",
    "wi",
    "wy",
    "mt",
    "rt",
    "retweet",
    "retweets",
    "retweeted",
    "rts",
    "mention",
    "mentions",
    "mentioned",
    "tweet",
    "tweeted",
    "tweets",
    "tweep",
    "tweeps",
    "am",
    "pm",
    "a.m.",
    "p.m.",
    "2g1c",
    "acrotomophilia",
    "anal",
    "anilingus",
    "anus",
    "apeshit",
    "arsehole",
    "ass",
    "asshole",
    "assmunch",
    "autoerotic",
    "babeland",
    "bang",
    "bangbros",
    "bareback",
    "barenaked",
    "bastardo",
    "bastinado",
    "bbw",
    "bdsm",
    "beaner",
    "beaners",
    "beaver",
    "bestiality",
    "bimbos",
    "birdlock",
    "bitch",
    "bitches",
    "blowjob",
    "blumpkin",
    "bollocks",
    "bondage",
    "boner",
    "boner",
    "boob",
    "boobs",
    "booty",
    "breasts",
    "bukkake",
    "bulldyke",
    "bullshit",
    "bunghole",
    "busty",
    "butt",
    "buttcheeks",
    "butthole",
    "cameltoe",
    "camgirl",
    "camslut",
    "camwhore",
    "carpetmuncher",
    "circlejerk",
    "clit",
    "clitoris",
    "clusterfuck",
    "cock",
    "cocks",
    "coon",
    "coons",
    "coprolagnia",
    "coprophilia",
    "cornhole",
    "creampie",
    "cum",
    "cumming",
    "cunnilingus",
    "cunt",
    "damn",
    "darkie",
    "daterape",
    "deepthroat",
    "dendrophilia",
    "dick",
    "dildo",
    "doggiestyle",
    "doggystyle",
    "dolcett",
    "domination",
    "dominatrix",
    "dommes",
    "donkeypunch",
    "dp",
    "dvda",
    "ecchi",
    "ejaculation",
    "erotic",
    "erotism",
    "escort",
    "eunuch",
    "faggot",
    "fat",
    "fecal",
    "felch",
    "fellatio",
    "feltch",
    "femdom",
    "fetish",
    "figging",
    "fingerbang",
    "fingering",
    "fisting",
    "footjob",
    "frotting",
    "fuck",
    "fuckin",
    "fucking",
    "fucktards",
    "fudgepacker",
    "futanari",
    "g-spot",
    "gangbang",
    "genitals",
    "goatcx",
    "goatse",
    "goddamn",
    "gokkun",
    "goo",
    "goodpoop",
    "goregasm",
    "grope",
    "guro",
    "handjob",
    "hardcore",
    "hentai",
    "homoerotic",
    "honkey",
    "hooker",
    "hump",
    "humping",
    "incest",
    "intercourse",
    "jack-off",
    "jackoff",
    "jailbait",
    "jerkoff",
    "jigaboo",
    "jiggaboo",
    "jiggerboo",
    "jizz",
    "juggs",
    "kike",
    "kinbaku",
    "kinkster",
    "kinky",
    "knobbing",
    "knockers",
    "lolita",
    "lovemaking",
    "masturbate",
    "menage",
    "milf",
    "motherfucker",
    "muff",
    "muffdiving",
    "nambla",
    "nawashi",
    "negro",
    "neonazi",
    "nig",
    "nigga",
    "nigger",
    "nimphomania",
    "nipple",
    "nipples",
    "nsfw",
    "nude",
    "nudity",
    "nympho",
    "nymphomania",
    "octopussy",
    "omorashi",
    "orgasm",
    "orgy",
    "paedophile",
    "paki",
    "panties",
    "panty",
    "pedobear",
    "pedophile",
    "pegging",
    "penis",
    "piss",
    "pissing",
    "pisspig",
    "playboy",
    "pole",
    "ponyplay",
    "poof",
    "poon",
    "poontang",
    "poop",
    "poopchute",
    "porn",
    "porno",
    "pornography",
    "pthc",
    "pubes",
    "punany",
    "pussy",
    "queaf",
    "queef",
    "quim",
    "raghead",
    "rape",
    "raping",
    "rapist",
    "rectum",
    "rimjob",
    "rimming",
    "s&m",
    "sadism",
    "scat",
    "schlong",
    "scissoring",
    "semen",
    "sexo",
    "sexy",
    "shaved",
    "shemale",
    "shibari",
    "shit",
    "shits",
    "shitty",
    "shota",
    "shrimping",
    "skeet",
    "slanteye",
    "slut",
    "sluts",
    "smut",
    "snatch",
    "snowballing",
    "sodomize",
    "sodomy",
    "spic",
    "splooge",
    "spooge",
    "spunk",
    "squirting",
    "strap-on",
    "strapon",
    "strappado",
    "strip",
    "suck",
    "sucks",
    "swastika",
    "swinger",
    "taint",
    "teabagging",
    "threesome",
    "throating",
    "tit",
    "tits",
    "titties",
    "titty",
    "tongue",
    "topless",
    "tosser",
    "towelhead",
    "tranny",
    "tribadism",
    "trois",
    "tubgirl",
    "tushy",
    "twat",
    "twink",
    "twinkie",
    "undressing",
    "upskirt",
    "urethra",
    "urophilia",
    "vagina",
    "vibrator",
    "vorarephilia",
    "voyeur",
    "vulva",
    "wank",
    "wetback",
    "yaoi",
    "yiffy",
    "zoophilia"
    ])
