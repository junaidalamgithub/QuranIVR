# -*- coding: utf-8 -*-
"""
Created on Tue Jul  21 23:57:35 2021

@author: Junaid Alam
"""
import ai_config as ai

male_voice = 0
female_voice = 1
ai.set_voice(female_voice)
ai.set_audio_directory("\\recitations\\")
# ai.get_surahs_from("surahs.json")
ai.set_silence_duration(2)
ai.greet()
while True:
    ai.run_ai()
