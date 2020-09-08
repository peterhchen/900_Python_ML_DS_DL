# Setup regex
import re

format_pat= re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

# Here's the path to the log file I'm analyzing
logPath = "access_log.txt"

UserAgents = {}

# Filter out by 'user_agent'
with open(logPath, "r") as f:
    for line in (li.rstrip() for li in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if agent in UserAgents:
                UserAgents[agent] = UserAgents[agent] + 1
            else:
                UserAgents[agent] = 1

results = sorted(UserAgents, key=lambda i: int(UserAgents[i]), reverse=True)

for result in results:
    print(result + ": " + str(UserAgents[result]))

# URLCounts = {}

# with open(logPath, "r") as f:
#     for line in (l.rstrip() for l in f):
#         match= format_pat.match(line)
#         if match:
#             access = match.groupdict()
#             request = access['request']
#             fields = request.split()
#             if (len(fields) == 3):
#                 (action, URL, protocol) = fields
#                 if (action == 'GET'):
#                     if URL in URLCounts:
#                         URLCounts[URL] = URLCounts[URL] + 1
#                     else:
#                         URLCounts[URL] = 1

# results = sorted(URLCounts, key=lambda i: int(URLCounts[i]), reverse=True)

# for result in results[:20]:
#     print(result + ": " + str(URLCounts[result]))