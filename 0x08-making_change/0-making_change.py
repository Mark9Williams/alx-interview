#!/usr/bin/python3
"""Maing change classical programming problem"""


def biggest_possible(coins, remainder):
    """Calclates the best possible denomination for accumulating the total"""
    for coin in coins:
        if coin <= remainder:
            return coin

    return 0


def makeChange(coins, total):
    """returns fewest number of coins required to meet the total"""
    if total <= 0:
        return 0
    cumulative = 0
    divisor = total
    remainder = total
    num_coins = 0
    coins = sorted(coins, reverse=True)
    while remainder > 0:
        biggest = biggest_possible(coins, remainder)
        if biggest == 0:
            return -1

        num_coins += remainder // biggest
        remainder %= biggest

    return num_coins
