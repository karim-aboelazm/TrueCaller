# Auther : Karim Mohammed Aboelazm
# date  : 31-1-2022
# library used : phonenumbers
# pip install phonenumbers 
# -------------------------------------------------------
import phonenumbers
from phonenumbers import carrier, geocoder , timezone
def truecaller(mob_num:str):
    mob_num = phonenumbers.parse(mob_num)
    print(timezone.time_zones_for_number(mob_num))
    print(carrier.name_for_number(mob_num,'en'))
    print(geocoder.description_for_number(mob_num,'en'))
    print('Valid Mobile Number : ',phonenumbers.is_valid_number(mob_num))
    print('Checking Possibilty of number : ',phonenumbers.is_possible_number(mob_num))

if __name__ == '__main__':
    truecaller('+201278789685')
