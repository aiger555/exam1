from datetime import date
group = {
    'names':{
        'Madina': {
            'role':'gitarist',
            'date': date(1994, 10, 20)
        },

        'Sina': {
            'role':'dramer',
            'date': date(1995, 12, 22)
        },

        'Hina':{
            'role':'singer',
            'date': date(1997, 11, 15)
        },
    },
    'concerts':{
        'Tokio':{
            'concert_date':date(2022, 12, 10),
            'expences':[760, 400, 200],
            'income': 22000
        },

        'Pekin':{
            'concert_date':date(2022, 12, 12),
            'expences':[234, 433, 120],
            'income': 22000
        },
        'Bishkek':{
            'concert_date':date(2022, 12, 14),
            'expences':[390, 300, 100],
            'income': 22000
        },
        'Lodz':{
            'concert_date':date(2022, 12, 17),
            'expences':[434, 463, 100],
            'income': 22000
        },
        'Brasilia':{
            'concert_date':date(2022, 12, 23),
            'expences':[254, 733, 180],
            'income': 22000
        },

    }
}

# 1
def rem():
    del group['names']['Madina']
    return group

print(rem())

# 2
new_name = {'Meerim':{ 
            'role':'dramer',
            'date': date(1995, 12, 22)
            }
        }
def add(dd):
    group['names'].update(dd) 
    return group

print(add(new_name))

# 3
new_concert = {'Seul':{
            'concert_date':date(2022, 11, 6),
            'expences':[234, 433, 120],
            'income': 22000
        }
}

 def add_concert(dg):
    group['concerts'].update(dg) 
    return group

print(add_concert(new_concert))

# 4
def spendings():
   sum(group['concerts']['Tokio']['expences'])
   sum(group['concerts']['Lodz']['expences'])
   sum(group['concerts']['Bishkek']['expences'])
   sum(group['concerts']['Pekin']['expences'])
   sum(group['concerts']['Brasilia']['expences'])
print(spendings())

# 5
def differences():
   group['concerts']['Tokio']['income'] - sum(group['concerts']['Tokio']['expences']) 
   group['concerts']['Lodz']['income'] - sum(group['concerts']['Lodz']['expences'])
   group['concerts']['Bishkek']['income'] - sum(group['concerts']['Bishkek']['expences'])
   group['concerts']['Pekin']['income'] - sum(group['concerts']['Pekin']['expences'])
   group['concerts']['Brasilia']['income'] - sum(group['concerts']['Brasilia']['expences'])
print(differences())