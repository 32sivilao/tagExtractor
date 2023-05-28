tagToModel = {["grabbing own breast"]: ["https://civitai.com/api/download/models/29860"],
              ["grabbing another's breast"]: ["https://civitai.com/api/download/models/23040"],
              ["grabbing from behind"]: ["https://civitai.com/api/download/models/50847"],
              ["paizuri invitation"]: ["https://civitai.com/api/download/models/64849"],
              ["paizuri"]: ["https://civitai.com/api/download/models/14996"]}

# tags to identify:, tags to put, tags to remove if exist
tagToLora = {["grabbing own breast"]: [["breast grab", "breast lift", "sbg", "<lora:SelfBreastGrab:0.8>"],
                                       [""]],
             ["grabbing another's breast"]: [["breast grab", "povbreastgrab", "pov hands", "<lora:POVBGV2:0.85>"],
                                             [""]],
             ["grabbing from behind"]: [
                 ["breast grab", "grabbing from behind", "<lora:qqq-grabbing_from_behind-v2-000006:0.7>"],
                 ["povbreastgrab", "pov hands", "<lora:POVBGV2:0.85>"]],
             ["paizuri invitation"]: [["paizuriinvitation", "cleavage", "partially unbuttoned", "button gap",
                                       "(hands on own chest,deep skin:1.2)", "looking at viewer",
                                       "<lora:paizuriinvitation-12:0.8>"],
                                      [""]],
             ["paizuri"]: [["1boy", "breasts", "paizuri", "penis", "<lora:POVPaizuri:1>"],
                           [""]]}


def parse(tags):  # recevice a list of tags
    global tagToLora
    keys = tagToLora.keys()

    tagsToAdd = []
    tagsToNotAdd = []
    neededLoras = []

    for tag in tags:
        for key in keys:
            counter = 0
            if tag in key[0]:
                for string in key:
                    if string in tags:
                        counter += 1
                if counter == len(key):
                    tagsToAdd += tagToLora[key][0]
                    tagsToNotAdd += tagToLora[key][1]
                    tagsToNotAdd += key
                    neededLoras += tagToModel[key]

    # remove tags from the tags list
    if tagsToNotAdd:
        for tagToRemove in tagsToNotAdd:
            if tagToRemove in tags:
                tags.remove(tagToRemove)

    # remove the possibility for duped tags
    if tagsToAdd:
        for tagToAdd in tagsToAdd:
            if tagToAdd in tags:
                tagsToAdd.remove(tagToAdd)
    
    print(neededLoras)
    tags += tagsToAdd
    return tags
