from pandas import read_csv, merge
from warnings import filterwarnings
filterwarnings("ignore", 'This pattern is interpreted as a regular expression, and has match groups')

# Load
data = read_csv("data/sentences.csv")

# AI
print("AI...")
rows = (
    data.Text.str.contains(r'(?i)\bcomputer to be') |
    data.Text.str.contains(r'(?i)\bAI\b') |
    data.Text.str.contains(r'(?i)\balgorithm') |
    data.Text.str.contains(r'(?i)\bmachinery') |
    data.Text.str.contains(r'(?i)\bartificial intelligence') |
    data.Text.str.contains(r'(?i)\bcomputer.*?\bcorrect') |
    data.Text.str.contains(r'(?i)\bcomputer.*?\brecommend') |
    data.Text.str.contains(r'(?i)\bcomputer put') |
    data.Text.str.contains(r'(?i)\bcomputer.*?\bteach') |
    data.Text.str.contains(r'(?i)\bcomputer does'))

data["AI"] = 0
data.loc[rows, "AI"] = 1

# Compare
print("Compare...")
rows = (
    data.Text.str.contains(r'(?i)(?=.*(student|kid|apple))(?=.*comparing)') |
    data.Text.str.contains(r'(?i)compare.*other people') |
    data.Text.str.contains(r'(?i)compare to\b.*others') |
    data.Text.str.contains(r'(?i)\bcompare group') |
    data.Text.str.contains(r'(?i)\bcompares\b') |
    data.Text.str.contains(r'(?i)\blower than') |
    data.Text.str.contains(r'(?i)location.*on the grid') |
    data.Text.str.contains(r'(?i)placed.*into') |
    data.Text.str.contains(r'(?i)(organize).*(according to)') |
    data.Text.str.contains(r'(?i)where (he|she|they|students|the student) ?(are|is|\'re|\'s) (at|landing)') |
    data.Text.str.contains(r'(?i)\bto the average') |
    data.Text.str.contains(r'(?i)\bmore than average') |
    data.Text.str.contains(r'(?i)kids.*doing well') |
    data.Text.str.contains(r'(?i)\bpoorly') |
    data.Text.str.contains(r'(?i)\bdo well') |
    data.Text.str.contains(r'(?i)student.*into.*alert') |
    data.Text.str.contains(r'(?i)look.*multiple.*student') |
    data.Text.str.contains(r'(?i)kid.*doing well') |
    data.Text.str.contains(r'(?i)high\b.*score') |
    data.Text.str.contains(r'(?i)score.*low') |
    data.Text.str.contains(r'(?i)score.*high\b') |
    data.Text.str.contains(r'(?i)higher.*score') |
    data.Text.str.contains(r'(?i)score.*higher') |
    data.Text.str.contains(r'(?i)person.*does more') |
    data.Text.str.contains(r'(?i)(high\b|higher).*rating') |
    data.Text.str.contains(r'(?i)\bmiddle range') |
    data.Text.str.contains(r'(?i)far.*from the line') |
    data.Text.str.contains(r'(?i)falling in.*spot') |
    data.Text.str.contains(r'(?i)compare.*student') |
    data.Text.str.contains(r'(?i)started.*ended') |
    data.Text.str.contains(r'(?i)higher than.*average') |
    data.Text.str.contains(r'(?i)higher than.*student') |
    data.Text.str.contains(r'(?i)student.*least') |
    data.Text.str.contains(r'(?i)student completed.*most') |
    data.Text.str.contains(r'(?i)\blow.*score'))

data["Compare"] = 0
data.loc[rows, "Compare"] = 1

# Construct
print("Construct...")
rows = (
    data.Text.str.contains(r'(?i)\bmisconception') |
    data.Text.str.contains(r'(?i)\bmisunderst') |
    data.Text.str.contains(r'(?i)\bpersisten') |
    data.Text.str.contains(r'(?i)\bkept going') |
    data.Text.str.contains(r'(?i)\bkept trying') |
    data.Text.str.contains(r'(?i)\bkeep trying') |
    data.Text.str.contains(r'(?i)\bkeep going') |
    data.Text.str.contains(r'(?i)^(?:(?!\bloud).)*\bvolume(?!.*\bloud)') |
    data.Text.str.contains(r'(?i)\bsurface area') |
    data.Text.str.contains(r'(?i)\bspatial reasoning') |
    data.Text.str.contains(r'(?i)\bdo the math') |
    data.Text.str.contains(r'(?i)\bproblem-solving') |
    data.Text.str.contains(r'(?i)\blife skill'))

data["Construct"] = 0
data.loc[rows, "Construct"] = 1

# Groups
print("Groups...")
rows = (
    data.Text.str.contains(r'(?i)\bclass level') |
    data.Text.str.contains(r'(?i)\bclass-level') |
    data.Text.str.contains(r'(?i)\bmajority') |
    data.Text.str.contains(r'(?i)\bclass result') |
    data.Text.str.contains(r'(?i)class.*data') |
    data.Text.str.contains(r'(?i)\ball at once') |
    data.Text.str.contains(r'(?i)students.*average') |
    data.Text.str.contains(r'(?i)average.*class') |
    data.Text.str.contains(r'(?i)(?=.*class)(?=.*whole)') |
    data.Text.str.contains(r'(?i)(?=.*(spectrum|(?<!came )across(?!.*(the top|graphs|anything))))(?=.*(students|class))') |
    data.Text.str.contains(r'(?i)(?=.*\b(?<!at )all(?! (the way|that|their))\b)(?=.*kids)'))

data["Groups"] = 0
data.loc[rows, "Groups"] = 1

# Manipulate
print("Manipulate...")
rows = (
    data.Text.str.contains(r'(?i)\bsorting') |
    data.Text.str.contains(r'(?i)\bmanual analysis') |
    data.Text.str.contains(r'(?i)\bdrill down') |
    data.Text.str.contains(r'(?i)\bfilter by') |
    data.Text.str.contains(r'(?i)\bclick on.*?\bclass') |
    data.Text.str.contains(r'(?i)\bclick on.*?\bgroup') |
    data.Text.str.contains(r'(?i)\bdig in') |
    data.Text.str.contains(r'(?i)((.*?\bclick.*?\bselect.*?)|(.*?\bselect.*?\bclick.*?))') |
    data.Text.str.contains(r'(?i)\bselect.*?\bstudent') |
    data.Text.str.contains(r'(?i)\bsort value') |
    data.Text.str.contains(r'(?i)\bdig.*?\bdata') |
    data.Text.str.contains(r'(?i)\bclick.*?\bstudent') |
    data.Text.str.contains(r'(?i)\bmerging') |
    data.Text.str.contains(r'(?i)\bclick.*?\bexplore') |
    data.Text.str.contains(r'(?i)\bsift') |
    data.Text.str.contains(r'(?i)((.*?\bidentif.*?\bstudent.*?)|(.*?\bstudent.*?\bidentif.*?))') |
    data.Text.str.contains(r'(?i)\bgroup my students') |
    data.Text.str.contains(r'(?i)\bclick on them') |
    data.Text.str.contains(r'(?i)\bfilter through') |
    data.Text.str.contains(r'(?i)\bpick\b.*?\bstudent') |
    data.Text.str.contains(r'(?i)\banalyz.*?\bdata') |
    data.Text.str.contains(r'(?i)\bsort(?!.*?\bof\b)') |
    data.Text.str.contains(r'(?i)\bfilter'))

data["Manipulate"] = 0
data.loc[rows, "Manipulate"] = 1

# Teach
print("Teach...")
rows = (
    data.Text.str.contains(r'(?i)\bhelp them') |
    data.Text.str.contains(r'(?i)((.*?\bteach.*?\blesson.*?)|(.*?\blesson.*?\bteach.*?))') |
    data.Text.str.contains(r'(?i)\bassign\b') |
    data.Text.str.contains(r'(?i)\bintervene') |
    data.Text.str.contains(r'(?i)((.*?\bhelp them.*?\bwork.*?)|(.*?\bwork.*?\bhelp them.*?))') |
    data.Text.str.contains(r'(?i)\bhow to help') |
    data.Text.str.contains(r'(?i)\bpull student') |
    data.Text.str.contains(r'(?i)\bcan I help') |
    data.Text.str.contains(r'(?i)\baddress misconception') |
    data.Text.str.contains(r'(?i)\boffer suggestion') |
    data.Text.str.contains(r'(?i)\bclass discussion') |
    data.Text.str.contains(r'(?i)\breteach') |
    data.Text.str.contains(r'(?i)\bcheck in with them') |
    data.Text.str.contains(r'(?i)\bplan.*?\blesson') |
    data.Text.str.contains(r'(?i)\blesson plan') |
    data.Text.str.contains(r'(?i)\binform\b.*?\binstruction') |
    data.Text.str.contains(r'(?i)\bdirect instruction') |
    data.Text.str.contains(r'(?i)\bcheck.*?\bwith student') |
    data.Text.str.contains(r'(?i)\bhelp.*?\bstudent'))

data["Teach"] = 0
data.loc[rows, "Teach"] = 1

# Performance
print("Performance...")
rows = (
    data.Text.str.contains(r'(?i)\bgot right') |
    data.Text.str.contains(r'(?i)\bachieve') |
    data.Text.str.contains(r'(?i)\bmeasure') |
    data.Text.str.contains(r'(?i)\bperform') |
    data.Text.str.contains(r'(?i)\bscore') |
    data.Text.str.contains(r'(?i)\bscoring') |
    data.Text.str.contains(r'(?i)\btotal\b') |
    data.Text.str.contains(r'(?i)\btotals\b') |
    data.Text.str.contains(r'(?i)\bnumbers you see') |
    data.Text.str.contains(r'(?i)(?=.*(how many|how much))(?=.*made)'))

data["Performance"] = 0
data.loc[rows, "Performance"] = 1

# Sequence
print("Sequence...")
rows = (
    data.Text.str.contains(r'(?i)\brevisit') |
    data.Text.str.contains(r'(?i)\bskip') |
    data.Text.str.contains(r'(?i)\breattempt') |
    data.Text.str.contains(r'(?i)com(e|ing) back to try') |
    data.Text.str.contains(r'(?i)ones.*attempted') |
    data.Text.str.contains(r'(?i)\babandon') |
    data.Text.str.contains(r'(?i)(?=.*\bfail)(?=.*\btr(y|ied|ying)\b)(?=.*\b(he|she|they|students|the student)\b)') |
    data.Text.str.contains(r'(?i)\bsubmit again') |
    data.Text.str.contains(r'(?i)(?=.*(complete|abandon|mov(e|ing) on|many|went to))(?=.*(puzzle))') |
    data.Text.str.contains(r'(?i)\btr(y|ied).*\btimes'))

data["Sequence"] = 0
data.loc[rows, "Sequence"] = 1

# Thinking
print("Thinking...")
rows = (
    data.Text.str.contains(r'(?i)process.*learn') |
    data.Text.str.contains(r'(?i)how they.*(solved|got)') |
    data.Text.str.contains(r'(?i)they did.*(rotat|check solution)') |
    data.Text.str.contains(r'(?i)they\'re(rotat|snapshot|checking)') |
    data.Text.str.contains(r'(?i)kid.*game tool') |
    data.Text.str.contains(r'(?i)student.*game tool') |
    data.Text.str.contains(r'(?i)tool.*they have') |
    data.Text.str.contains(r'(?i)\bchecked it') |
    data.Text.str.contains(r'(?i)\bbunch of actions') |
    data.Text.str.contains(r'(?i)chang.*perspective') |
    data.Text.str.contains(r'(?i)their use\b.*\btool') |
    data.Text.str.contains(r'(?i)\bsnapshot tool') |
    data.Text.str.contains(r'(?i)tool.*strateg') |
    data.Text.str.contains(r'(?i)what they.*do a lot') |
    data.Text.str.contains(r'(?i)student.*\bstaring') |
    data.Text.str.contains(r'(?i)\bwhat students did') |
    data.Text.str.contains(r'(?i)\buse.*\bgame tool') |
    data.Text.str.contains(r'(?i)student.*stuck') |
    data.Text.str.contains(r'(?i)\bspend their time') |
    data.Text.str.contains(r'(?i)player.*checking') |
    data.Text.str.contains(r'(?i)what they.*did(?!n\'t)') |
    data.Text.str.contains(r'(?i)move.*made') |
    data.Text.str.contains(r'(?i)\bwhat\b.*\bgot\b.*\bstuck\b') |
    data.Text.str.contains(r'(?i)\befficient way') |
    data.Text.str.contains(r'(?i)\bknowledgeable way') |
    data.Text.str.contains(r'(?i)way.*to have gotten there') |
    data.Text.str.contains(r'(?i)student.*struck') |
    data.Text.str.contains(r'(?i)\bmovement tool') |
    data.Text.str.contains(r'(?i)\bkid\b.*(rotating|snapshot)') |
    data.Text.str.contains(r'(?i)\bstudent is thinking') |
    data.Text.str.contains(r'(?i)\btheir thinking') |
    data.Text.str.contains(r'(?i)\btook a break') |
    data.Text.str.contains(r'(?i)\bwrong shape') |
    data.Text.str.contains(r'(?i)they.*bored') |
    data.Text.str.contains(r'(?i)behave.*during') |
    data.Text.str.contains(r'(?i)stuck.*student') |
    data.Text.str.contains(r'(?i)time.*spent.*spinning') |
    data.Text.str.contains(r'(?i)\bmathematical thinking') |
    data.Text.str.contains(r'(?i)\bmathematical practice') |
    data.Text.str.contains(r'(?i)put.*shape'))

data["Thinking"] = 0
data.loc[rows, "Thinking"] = 1

# Trust
print("Trust...")
rows = (
    data.Text.str.contains(r'(?i)\btrust') |
    data.Text.str.contains(r'(?i)\bequit') |
    data.Text.str.contains(r'(?i)\bbias') |
    data.Text.str.contains(r'(?i)\back box') |
    data.Text.str.contains(r'(?i)\bvalid') |
    data.Text.str.contains(r'(?i)\beasonable') |
    data.Text.str.contains(r'(?i)\btake\b.*?\bon faith\b'))

data["Trust"] = 0
data.loc[rows, "Trust"] = 1

# Metadata
meta = read_csv("data/session_metadata.csv", sep="\t")
merged = merge(data, meta, on=["Session", "Activity"])

# Done!
merged.to_csv("data/preprocessed.csv", index=False)
print("Done!")

