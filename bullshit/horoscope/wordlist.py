import sys

from . import dirtywords

this_module = sys.modules[__name__]


def _setup():
    """Create lists in this module with both "clean" & dirty words."""
    for name in dir(dirtywords):
        if name[:1] == "_":
            continue

        named_object = getattr(dirtywords, name)
        if isinstance(named_object, list):
            clean_list = getattr(this_module, name)
            dirty_list = clean_list + named_object
            dirty_name = "dirty_" + name
            setattr(this_module, dirty_name, dirty_list)


def wordlist(name, dirty=False, prefix=""):
    """Get a word list by name, with optional filth."""
    name = prefix + name
    dirty_name = "dirty_" + name
    if dirty and hasattr(this_module, dirty_name):
        return getattr(this_module, dirty_name)
    return getattr(this_module, name)


# Astrological words
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus",
           "Neptune", "Pluto"]

stars = ["Proxima Centauri", "Barnard's Star", "Sirius A", "Epsilon Eridani"]

aspects = ["conjunction", "sextile", "square", "trine", "opposition"]

wanky_events = ["a large Electromagnetic disturbance", "Quantum Flux",
                "the upcoming Solar eclipse", "Unusual planetary motion"]

# Time words
beginnings = ["arrival", "beginning", "start"]
endings = ["end", "death", "passing"]

time_periods = ["interlude", "period", "week", "day"]

# Feeling adjectives
good_feeling_adjs = [
    "stable",
    "bugs free",
    "up and running",
    "safe and sound",
    "problems free",
    "errors free",
    "normal",
    "on INFO level",
    "clean reports",
    "all green",
    "green"
]

bad_feeling_adjs = [
    "down",
    "full of errors",
    "on full logs",
    "glitching",
    "buggy",
]

good_emotive_adjs = ["cathartic", "healing", "mystical"]

bad_emotive_adjs = ["anti-climactic"]

# Intensifiers for use in front of feeling adjectives
good_degrees = ["ridiculously", "surprisingly"]
neutral_degrees = ["practically", "fairly", "pretty", "curiously", "basically"]
bad_degrees = ["worringly", "distressingly"]

# Emotive nouns
good_feeling_nouns = [
    "fixing technical debt",
    "refactoring",
    "bugfixes",
    "days off",
    "conference tickets",
    "good uptime",
    "successful deployment"
]

good_emotive_nouns = [
    "lulz",
    "catharsis",
    "mysticism",
    "transcendence",
    "metamorphisis"
]

bad_feeling_nouns = ["bitterness", "disappointment", "sadness", "frustration",
                     "anger", "failure", "boredom", "tension"]

bad_emotive_nouns = ["bad luck", "misfortune", "déjà vu"]

# Misc
prediction_verbs = ["heralds", "marks", "foreshadows", "signifies"]

# You would be well advised to avoid...
avoid_list = [
    "querying the production DB",
    "hotfixes",
    "java developers",
    "recruiters",
    "interns",
    "garbage collection",
    "reinstalling OS",
    "updates",
    "team events",
    "online dating",
    "ssh to production",
    "database optimizations",
    "refactoring",
    "database migrations",
    "drinking beer",
    "playing playstation",
    "hiring managers",
    "organic food",
    "e-commerse startups",
    "cryptocurrency",
    "crawling",
    "scrum",
    "architectural meetings",
]

# People you may meet
familiar_people = [
    "your teamlead",
    "your frontend dev",
    "your backend dev",
    "the CEO",
    "the CTO",
    "a scrum master",
]

strange_people = [
    "a javascript developer",
    "a devops engineer",
    "a haskell adept",
    "an open source fan",
    "a ruby hacker",
    "a data scientist",
    "a product owner",
    "a project manager",
    "a c++ adept",
    "a crypto apologist",
    "Linus Torvalds",
    "Vitalik Buterin",
    "a Russian hacker",
    "a security specialist",
    "a data protection officer",
    "a gentoo adept",
    "a vim user",
    "an emacs user",
    "a ex-coworker",
    "a django girl",
    "a servlets pensioner",
    "a hackinstosh user",
    "an AI specialist",
    "a docker fan",
    "a Turing-Machine",
    "a robot",
    "a ghost in the shell",
    "a hardware nerd",
    "an iPhone user",
    "an Android user"
]

# Locations for various events
locations = [
    ("in", "the office"),
    ("in", "your data center"),
    ("in", "the kitchen"),
    ("in", "a coffee lounge"),
    ("at", "a hackaton"),
    ("in", "your dev room"),
    ("while", "the standup meeting"),
    ("while", "a retrospective meeting"),
    ("in", "the grooming meeting"),
    ("on", "a team event"),
    ("at", "friday beers"),
    ("on", "a conference"),
    ("on", "a meetup"),
    ("while", "home office"),
    ("while", "pair programming"),
    ("in", "a playroom"),
    ("in", "a meeting room"),
    ("at", "yoga courses"),
    ("at", "a smoothie stand"),
    ("at", "a coffee machine"),
    ("at", "a coffee shop")
]

# Types of discussions
neutral_discussions = [
    "discussion",
    "talk",
    "conversation",
    "debate"
]

good_discussions = [
    "chat",
    "intimate conversation",
    "chin wag"
]

bad_discussions = [
    "argument",
    "fight",
    "altercation",
    "terse chat",
    "misunderstanding"
]

# Conversation topics (good or bad)
conversation_topics = [
    "data science",
    "database optimizations",
    "refactoring",
    "downtime",
    "bugs",
    "upcoming features",
    "programming paradigms",
    "programming languages",
    "mobile platforms",
    "operational systems",
    "holy war",
    "salary"
]

# Run the setup function once all names have been loaded
_setup()
