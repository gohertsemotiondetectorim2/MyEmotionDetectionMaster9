# -*- coding: cp1252 -*-
import re

string = "ðŸ”ŠPODCASTðŸ”Š@theanalyst and @Cricket_Mann discuss the Australia-India series, Derek Pringle's book and the strange câ€¦ https://t.co/A11fCO8d64"

#string.text.encode("utf-8")
tweet = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", string)
print tweet
