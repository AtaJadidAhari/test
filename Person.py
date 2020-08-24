import random
import math
import sys

#print("Person")
death_probs_male = [0 for i in range(99)]
with open('./Data/deathprobmale.txt', 'r') as f:
    lines = f.readlines()
    for i in range(99):
        death_probs_male[i] = (float(lines[i]))

death_probs_female = [0 for i in range(99)]
with open('./Data/deathprobfemale.txt', 'r') as f:
    lines = f.readlines()
    for i in range(99):
        death_probs_female[i] = (float(lines[i]))



marriage_probs = []
with open('./Data/MarriageProb.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        marriage_probs.append(list(map(float, line.split('\t'))))

age_marriage_probs = []
with open('./Data/AgeMarriageProbs.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        age_marriage_probs.append(list(map(float, line.split('\t'))))



def get_age(raw_age):
    ages.append(2020 - int(raw_age.split('-')[0]))
    return 2020 - int(raw_age.split('-')[0])



class Family:

    def __init__(self, id, parent_id, father, mother, childnum, children, maxChildAge, minChildAge):
        self.family_id = id
        self.father = father
        self.mother = mother
        self.childnum = childnum
        self.children = children
        self.maxChildAge = maxChildAge
        self.minChildAge = minChildAge
        self.parent_id = parent_id
        self.alive = True

class Person:

    def __init__(self, index, Id, ParentId, Gender, BirthDate, PostalCode, IsUrban, ProvinceName, CountyName,
                 Trip_AirNonPilgrimageCount_95, Trip_AirNonPilgrimageCount_96, Trip_AirNonPilgrimageCount_97,
                 Trip_AirNonPilgrimageCount_98, Cars_Count, CarPrice_Sum, Bardasht95, Variz95, MandehAval95,
                 MandehAkhar95, Sood95, Bardasht96, Variz96, MandehAval96, MandehAkhar96, Sood96, Bardasht97,
                 Variz97, MandehAval97, MandehAkhar97, Sood97, Card9801, Card9802, Card9803, Card9804,
                 Card9805, Card9806, IsBehzisti_Malool, IsBimarkhas, SenfName, IsTamin_Karfarma, Tamin_KargarCount,
                 IsBazneshaste_Sandoghha, IsBimePardaz_Sandoghha, Daramad_Total_Rials):
        self.id = Id
        self.parent_id = ParentId
        self.gender = 0 #man

        if Gender == 'زن':
            self.gender = 1
        self.age = get_age(BirthDate)
        self.PostalCode = PostalCode
        self.IsUrban = IsUrban
        self.ProvinceName = ProvinceName
        self.ProvinceId = 0
        self.get_provinceId()
        self.CountyName = CountyName
        self.Trip_AirNonPilgrimageCount_95 = Trip_AirNonPilgrimageCount_95
        self.Trip_AirNonPilgrimageCount_96 = Trip_AirNonPilgrimageCount_96
        self.Trip_AirNonPilgrimageCount_97 = Trip_AirNonPilgrimageCount_97
        self.Trip_AirNonPilgrimageCount_98 = Trip_AirNonPilgrimageCount_98
        self.Cars_Count = Cars_Count
        self.CarPrice_Sum = CarPrice_Sum
        self.Bardasht95 = Bardasht95
        self.Variz95 = Variz95
        self.MandehAval95 = MandehAval95
        self.MandehAkhar95 = MandehAkhar95
        self.Sood95 = Sood95
        self.Bardasht96 = Bardasht96
        self.Variz96 = Variz96
        self.MandehAval96 = MandehAval96
        self.MandehAkhar96 = MandehAkhar96
        self.Sood96 = Sood96
        self.Bardasht97 = Bardasht97
        self.Variz97 = Variz97
        self.MandehAval97 = MandehAval97
        self.MandehAkhar97 = MandehAkhar97
        self.Sood97 = Sood97
        self.Card9801 = Card9801
        self.Card9802 = Card9802
        self.Card9803 = Card9803
        self.Card9804 = Card9804
        self.Card9805 = Card9805
        self.Card9806 = Card9806
        self.IsBehzisti_Malool = IsBehzisti_Malool
        self.IsBimarkhas = IsBimarkhas
        self.SenfName = SenfName
        self.IsTamin_Karfarma = IsTamin_Karfarma
        self.Tamin_KargarCount = Tamin_KargarCount
        self.IsBazneshaste_Sandoghha = IsBazneshaste_Sandoghha
        self.IsBimePardaz_Sandoghha = IsBimePardaz_Sandoghha
        self.Daramad_Total_Rials = Daramad_Total_Rials

        self.religion = random.randint(0, 7)
        self.education = random.randint(0, 5)
        self.alive = True
        self.x = self.ProvinceId//5
        self.y = self.ProvinceId - (self.ProvinceId//5 * 5)
        self.IE = 0 #intended education
        self.w = 0
        self.married = False
        self.family_id = -1

        self.index = index



    def get_provinceId(self):
        if self.ProvinceName == 'آذربایجان غربی':
            self.ProvinceId = 0

        elif self.ProvinceName == 'آذربایجان شرقی':
            self.ProvinceId = 1
        elif self.ProvinceName == 'اردبیل':
            self.ProvinceId = 2
        elif self.ProvinceName == 'گیلان':
            self.ProvinceId = 3
        elif self.ProvinceName == 'کردستان':
            self.ProvinceId = 4
        elif self.ProvinceName == 'زنجان':
            self.ProvinceId = 5
        elif self.ProvinceName == 'قزوین':
            self.ProvinceId = 6
        elif self.ProvinceName == 'تهران' or self.ProvinceName == 'البرز':
            self.ProvinceId = 7
        elif self.ProvinceName == 'مازندران':
            self.ProvinceId = 8
        elif self.ProvinceName == 'گلستان':
            self.ProvinceId = 9
        elif self.ProvinceName == 'خراسان شمالی':
            self.ProvinceId = 10
        elif self.ProvinceName == 'خراسان رضوی':
            self.ProvinceId = 11
        elif self.ProvinceName == 'کرمانشاه':
            self.ProvinceId = 12
        elif self.ProvinceName == 'همدان':
            self.ProvinceId = 13
        elif self.ProvinceName == 'مرکزی':
            self.ProvinceId = 14
        elif self.ProvinceName == 'قم':
            self.ProvinceId = 15
        elif self.ProvinceName == 'سمنان':
            self.ProvinceId = 16
        elif self.ProvinceName == 'ایلام':
            self.ProvinceId = 17
        elif self.ProvinceName == 'لرستان':
            self.ProvinceId = 18
        elif self.ProvinceName == 'اصفهان':
            self.ProvinceId = 19
        elif self.ProvinceName == 'یزد':
            self.ProvinceId = 20
        elif self.ProvinceName == 'خراسان جنوبی':
            self.ProvinceId = 21
        elif self.ProvinceName == 'خوزستان':
            self.ProvinceId = 22
        elif self.ProvinceName == 'چهارمحال وبختیاری':
            self.ProvinceId = 23
        elif self.ProvinceName == 'کهگیلویه و بویراحمد':
            self.ProvinceId = 24
        elif self.ProvinceName == 'بوشهر':
            self.ProvinceId = 25
        elif self.ProvinceName == 'فارس':
            self.ProvinceId = 26
        elif self.ProvinceName == 'کرمان':
            self.ProvinceId = 27
        elif self.ProvinceName == 'سیستان و بلوچستان':
            self.ProvinceId = 28
        elif self.ProvinceName == 'هرمزگان':
            self.ProvinceId = 29

        else:

            return 30





def add_ages(age):
    if age <= 5:
        ages[0] += 1
    elif age <= 10:
        ages[1] += 1
    elif age <= 15:
        ages[2] += 1
    elif age <= 20:
        ages[3] += 1
    elif age <= 25:
        ages[4] += 1
    elif age <= 30:
        ages[5] += 1
    elif age <= 35:
        ages[6] += 1
    elif age <= 40:
        ages[7] += 1
    elif age <= 45:
        ages[8] += 1
    elif age <= 50:
        ages[9] += 1
    elif age <= 55:
        ages[10] += 1
    elif age <= 60:
        ages[11] += 1
    elif age <= 65:
        ages[12] += 1
    elif age <= 70:
        ages[13] += 1
    elif age <= 75:
        ages[14] += 1
    elif age <= 80:
        ages[15] += 1
    elif age <= 85:
        ages[16] += 1
    elif age <= 90:
        ages[17] += 1
    elif age <= 95:
        ages[18] += 1
    else:

        ages[19] += 1

families = []
family_id = 0
person_index = 0
people = []
ages = [0 for i in range(20)]

men = []
women = []

men_num = 0
women_num = 0


def set_parent_to_orphans(family):
    max_age = 0
    max_age_index = -1
    for i in range(len(family.children)):
        if family.children[i].age > max_age:
            max_age = family.children[i].age
            max_age_index = i
    parent = family.children[max_age_index]

    for i in range(len(family.children)):
        family.children[i].parent_id = parent.parent_id

    if parent.gender == 0:
        family.father = parent
    else:
        family.mother = parent






def set_parent():
    to_remove = []
    children = []
    for i in range(len(families)):
        minimum_difference = 100
        index = -1

        if families[i].mother is None and families[i].father is None:
            to_remove.append(i)
            set_parent_to_orphans(families[i])
        elif families[i].mother is None:
            for j in range(len(families[i].children)):
                if families[i].children[j].gender == 1:

                    if math.fabs(families[i].children[j].age - families[i].father.age) < minimum_difference:
                        index = j
                        minimum_difference =  math.fabs(families[i].children[j].age - families[i].father.age)
            if minimum_difference < 15:
                families[i].mother = families[i].children[index]
                del(families[i].children[index])

        else:
            for j in range(len(families[i].children)):

                if families[i].children[j].gender == 0:
                    if math.fabs(families[i].children[j].age - families[i].mother.age) < minimum_difference:
                        index = j
                        minimum_difference = math.fabs(families[i].children[j].age - families[i].mother.age)
            if minimum_difference <= 15:
                families[i].father = families[i].children[index]
                del (families[i].children[index])
    """
    to_remove = [to_remove[i] - i for i in range(len(to_remove))]
    for i in to_remove:
        del (families[i])

    children = [children[i] - i for i in range(len(children))]
    for i in children:
        del (people[i])
    """


parent_ids = []
with open("Sample_AllNafar_981126.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines[1:50000]: #simulating on a part of data

        p = Person(person_index, *line.split(','))
        person_index += 1
        parent_ids.append(p.parent_id)
        #print(p.x, p.y, p.ProvinceId)
        people.append(p)

        if p.parent_id == p.id: #this person is sarparast khanevar


            if p.gender == 0:


                if len(families) == 0:

                    families.append(Family(family_id, p.id, p, None, 0, [], 0, 100))
                    family_id += 1

                elif families[-1].parent_id != p.id:
                    families.append(Family(family_id, p.id, p, None, 0, [], 0, 100))
                    family_id += 1
                else:

                    families[-1].father = p
            else:

                women_num += 1
                if len(families) == 0:
                    families.append(Family(family_id, p.id, None, p, 0, [], 0, 100))
                    family_id += 1
                elif families[-1].parent_id != p.id:
                    families.append(Family(family_id, p.id, None, p, 0, [], 0, 100))
                    family_id += 1
                else:

                    families[-1].mother = p

        else: #this person is not sarparast khanevar
            #if p.gender == 0 and p.age > 15:

            #    men.append(p)

            #else:
            #    women.append(p)

            if families[-1].parent_id != p.parent_id:


                families.append(Family(family_id, p.parent_id, None, None, 0, [], 0, 100))
                family_id += 1

            families[-1].children.append(p)

        p.family_id = families[-1].family_id
        add_ages(p.age)


set_parent()

for i in range(len(families)):
    if families[i].father is not None and families[i].mother is not None:
        families[i].father.married = True
        families[i].mother.married = True


"""
for i in range(len(families)):
    if families[i].father is not None:

        families[i].father.family_id = families[i].family_id
    if families[i].mother is not None:
        families[i].mother.family_id = families[i].family_id

    for j in range(len(families[i].children)):
        families[i].children[j].family_id = families[i].family_id
"""

