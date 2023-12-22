hindiDic = {
        "thik hai":"ok",
        "raat":"night",
        "ladka":"boy"
}

print("options are :",hindiDic.keys())
inputword = input("enter your hindi words\n")
print("your english word is :", hindiDic.get(inputword))