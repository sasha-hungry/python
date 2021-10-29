#!/usr/bin/env python

raw_time = input('input time in second: ')

hours = int(raw_time) // 3600
minutes = (int(raw_time) % 3600) // 60
seconds = (int(raw_time) % 3600) % 60


out_time = print(f"{hours:02d}:{minutes:02d}:{seconds:02d}" )
