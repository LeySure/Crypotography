import string
import random


def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon


def two_hundred_coupons():
    data = ''
    digit = 4
    for count in range(200):
        data +=  coupon_creator(digit)+'\n'
    return data


coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
coupondata.close()
