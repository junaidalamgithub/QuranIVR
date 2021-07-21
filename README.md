# QuranIVR - Speech Recognition IVR based verse recitation

QuranIVR is a python speech recognition based application that accepts a load and clear voice in a particular order of sentence to query for the chapter name or number along with the verse number by the user and in response it recites the queried chapter and verse or surah's if the voice input is accepted by the system.

Here is a small demo in the given video below:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/8NOEJHle_U8/0.jpg)](https://www.youtube.com/embed/8NOEJHle_U8 "Python Speech recognition API - Listening to Quran for the Visually Impaired")

## Installation

You first need to install the following:
Install python 3.6 or greater
pip install speech_recognition
pip install pyttsx3

The verse used in this application for demo was download from the following site:(https://everyayah.com/data/AbdulSamad_64kbps_QuranExplorer.Com/)
However you can place your own audio of the verse if you wish to do so.

## Usage
You can run the file 'quran_ai.py'. this uses the module 'ai_config.py' which will later be seperated into further modules and packages.

Following are the sets of commands in the inital draft version that this application accepts:

* `Query by chapter number and verse number`:
    * `Chapter x verse y`: e.g. chapter 1 verse 2
* `Query by chapter / surah name`:
    * `Surah <surah name>`: e.g. surah al ikhlaas
    * `Surah <surah name> verse x till / to verse y (y>x)`: e.g. Surah al ikhlaas verse 2 till 4
* `Query by surah name and translation language`:
    * `Translate Surah <surah name> in <language>`: e.g. translate surah al fatiha in english / urdu
*Please Note*: At the moment very few surah's and verse are taken, though the application is complete and can pick from complete set of Surah's but that would require to update the surahs.json file and download the remaining audio od all surah's remaing which will increase the sixe of application download. However if any user wish to then they can download the verses from any site that provides the audio and they need to rename the audio file in a particular pattern which is chapter number concatenated with verse number in a 3 digit form each.

## Scope for future enhancements

There are many features and error handlings that needs to be implemented, some of them are listed below:
- Speak out the error if verse no x | y exceeds the total verse of that chapter
- There should be a command to stop and once the command is issued, it stops after completing the immediate surah, rather than stopping abruptly.
- command to get list of verses audio
- make it more interactive
- Train the model for better text recognition for similar type of pronounciation but with varying spelling.
- Refactor the code into OOPS and package it into seperate set of modules , so that in future it can be ported as a REST API for integration with Web Applications and Mobile applications.

## License

It is open source and any developer who wish to refactor and enhance it are free to clone the repository, add enhancements and if they wish to contribute in enhancing it can raise the PR against this branch. Once the PR is reviewed we will review and merge it if found suitable.
Please note that this codebase is free, but it is still in its draft form and hence not optimized, so we do not serve any warranty or support.
