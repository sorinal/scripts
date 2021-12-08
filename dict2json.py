import json
d = {
    'ENFJ' : 2309,
    'ENFP' : 3929,
    'ENTJ' : 4257,
    'ENTP' : 3147,
    'ESFJ' : 3609,
    'ESFP' : 2942,
    'ESTJ' : 2868,
    'ESTP' : 2590,
    'INFJ' : 2594,
    'INFP' : 2776,
    'INTJ' : 2956,
    'INTP' : 2810,
    'ISFJ' : 3058,
    'ISFP' : 3771,
    'ISTJ' : 3724,
    'ISTP' : 3077
}
with open('length.json', 'w') as outfile:
    json.dump(d, outfile)
