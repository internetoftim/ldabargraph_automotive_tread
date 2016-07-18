line = "topicid,word,count"
for i in ["AIR BAG", "BRAKES", "CHILD SEAT", "ELECTRICAL SYSTEM", "ENGINE", "EQUIPMENT", "FUEL", "LIGHTS", "OTHER", "POWER TRAIN", "SEAT AND SEAT BELTS", "STEERING", "STRUCTURE", "SUSPENSION", "VEHICLE SPEED CONTROL", "VISIBILITY", "WHEELS AND TIRES"]:
    tblname = i.lower().replace(" ","")
    with open(tblname + "_ngram_3T.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)
    with open(tblname + "_ngram_5T.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)        
    with open(tblname + "_ngram_7T.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)
    with open(tblname + "_ngram_3T_TFIDF.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)
    with open(tblname + "_ngram_5T_TFIDF.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)        
    with open(tblname + "_ngram_7T_TFIDF.csv", "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)        