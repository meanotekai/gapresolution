'''converts result output file to agrr (csv) format'''

import neuthink.metatext as Text

def annotate_term(sent,tokens,term_name):

   if ":" in sent[term_name]:
    ranges = sent[term_name].split(" ")
    for rang in ranges:
        cvRange = rang.split(":")
        start = int(cvRange[0])
        end = int(cvRange[1])
        if term_name=="V":
            end = end + 1
            print("V")

        words = tokens.Text.GetWordsInSpan(start,end)
     #   print("---", words, term_name, start, end)
        for x in words:
            x["term"] = term_name
            if term_name=="V":
                x['vterm'] = "V"
   return tokens

def reverse(filename,outname):
    data = Text.LoadColumn(filename)
    data_orig = Text.LoadWords("diff_test.csv",separator="\t")
    data.Text.GetEntities(classname="dMap1")
    newf = open(outname,"w")
    for i,sentence in enumerate(data):
        sent = data_orig[i]["text"]
        terms = ["cV","cR1","cR2","V","R1","R2"]
        string = ""
        positive = "0"
        for term in terms:
            if term=="V":
                ent_terms = sentence.Children({'entity_subtype':"R2"})
                for x in ent_terms:
                    x["pos_end2"] = x["pos_start"]
            else:
                    ent_terms = sentence.Children({'entity_subtype':term})
            if len(ent_terms)>0 and term=="R2":
                positive = "1"
            print(ent_terms)
            for ent_term in ent_terms:
                start = ent_term["pos_start"]
                if term=="V":
                   end = ent_term["pos_end2"]
                else:
                   end = ent_term["pos_end"]
                string = string + str(start)+":"+str(end) + " "
            if len(string)>0 and string[-1]==" ":
                 string=string.strip()
                  
            string = string + '\t'
        string = sent + "\t" + positive + "\t" + string
        newf.write(string.strip()+"\n")

reverse("diff_test_result.txt","diff_test_result.csv")

