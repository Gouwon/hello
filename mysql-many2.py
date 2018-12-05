import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
alphas = list('abcdefghijklmnopqrstuvwxyz' * 3)
nums = list("0123456789" * 4)

m30 = [4,6,9,11]
years = list(range(70, 99))
monthes = list(range(1, 13))
days = list(range(1, 32))
days30 = list(range(1, 31))
days28 = list(range(1, 29))

def nr(n = 4):
    return "".join(random.sample(nums, n))

def ar(n = 4):
    return "".join(random.sample(alphas, n))

def make_birth():
    y = random.choice(years)
    m = random.choice(monthes)
    d = random.choice(days)
    if m in m30 and d > 30:
        d = random.choice(days30)
    elif m == 2 and d > 28:
        d = random.choice(days28)
    return "{}{:02d}{:02d}".format(y,m,d)

def make_data():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))

    tel = "010-{}-{}".format(nr(), nr())
    email = "{}@gmail.com".format(random.randrange(3, 9))
    
    return (sung + name, tel, email, make_birth() )

