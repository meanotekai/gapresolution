from neuthink import metagraph as m
#from neuthink.textviews import SentenceView
from neuthink.graph.basics import Graph
import torch
import os
graph = Graph()
path = os.path.dirname(os.path.abspath(__file__))
print(path)
model = m.dNodeList(graph)
model.classes = [x.strip() for x in open(path+'/'+'model3000x2x20482.cls','r').readlines()]
import json
model.resources = json.loads(open(path+'/'+'model3000x2x20482.res','r').read())
model.Text.VectorizeLookupChars(source="chunk",target="chunk_tensor",alphabet="alphabetchunk_tensor")
model.Lookup(source="chunk_tensor",target="Lookup1",size=50)
model.LSTM(size=3192,source="Lookup1",target="LSTM1",input_size=50,state_vector="default",carry_state="no")
model.LSTM(size=2048,source="LSTM1",target="LSTM2",input_size=3192,state_vector="default",carry_state="no")
model.LSTM(size=2048,source="LSTM2",target="LSTM3",input_size=2048,state_vector="default",carry_state="no")
model.Classify(target="Classify1",class_target="_seq_model",cmode="Normal",source="LSTM3",input_size=2048)

model.load_state_dict(torch.load(path +'/'+'model3000x2x20482.mod'))
model.mode='predict'
model3000x2x20482 = lambda x: model.predict(x)
