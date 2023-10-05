from bottles import bottle_song, bottle_song_recursive
import pytest


def test_bottle_song_2(capsys):
    bottle_song(2)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 2 bottles of beer on the wall.
"""
    )


def test_bottle_song_recursive_1(capsys):
    bottle_song_recursive(1)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""
    )
