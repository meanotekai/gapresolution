'''converts agrr (csv) format to conll-like format for sequnece tagger input/train/test'''

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

def direct(input_name, output_name):
    data = Text.LoadWords(input_name,separator="\t")
    terms = ["cV","cR1","cR2","V","R1","R2"]
    base = []
    for sentence in data:
    #  sentence = data[16403]
       # print(sentence)
        text = sentence["text"]
        tokens =Text.Tokenize(text,make_sentences=False)
        sent = tokens[0].Parent({})
        base.append(sent)
        for x in terms:
            tokens = annotate_term(sentence,tokens,x)
        

    sentences= tokens.ConvertTo(ctype='sentence')
    Text.SaveColumn(base,output_name,column_list=['word','pos_start','pos_end','term','vterm'])

#reverse("diff_test.txt","diff_test_result.csv")
direct("diff_test.csv","diff_test.txt")
