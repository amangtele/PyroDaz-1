# Create Modules By @xtsea
from pyrogram import *
from config import CMD_HANDLER as cmd

PREFIX = ["^", "?", "-", "+"]

cmd = [f"{cmd}"] # cmd custom

command = filters.command

dont_know = -1001640257827
